from __future__ import annotations

import os
import shutil
from pathlib import Path
from typing import TextIO

from .models import Klazz, Module, Property, Routine, RoutineParam

INDENT = 4
SPACE = " "
NEWLINE = "\n"
OUTPUT_PATH = Path.joinpath(Path(os.path.expanduser("~"))).joinpath("enabler-output")


def format_docstring(*, s: str, i: str) -> str:
    return f'''{i}"""
{NEWLINE.join([i + ss for ss in s.split(NEWLINE)])}
{i}"""'''


def write_class(*, cls: Klazz, handle: TextIO, nesting: int) -> None:
    ind = SPACE * INDENT * nesting
    member_ind = ind + SPACE * INDENT
    handle.write(f"{ind}class {cls.name}:")
    handle.write(NEWLINE)
    if cls.doc_string:
        handle.write(format_docstring(s=cls.doc_string, i=member_ind))
    handle.write(NEWLINE * 3)
    for c in cls.classes:
        write_class(cls=c, handle=handle, nesting=nesting + 1)
    for r in cls.routines:
        write_routine(routine=r, handle=handle, nesting=nesting + 1)
    for p in cls.properties:
        write_property(p=p, handle=handle, nesting=nesting + 1)
    handle.write(NEWLINE * 2)


def write_property(*, p: Property, handle: TextIO, nesting: int) -> None:
    ind = SPACE * INDENT * nesting
    member_ind = ind + SPACE * INDENT

    if isinstance(p.value, str) and p.value.startswith("<property object at"):
        return_type = "Any"
        if p.name == "clip" or p.name.endswith("clip"):
            return_type = "Clip"
        if p.name == "clips" or p.name.endswith("clips"):
            return_type = "list[Clip]"
        if p.name == "clip_slot" or p.name.endswith("clip_slot"):
            return_type = "ClipSlot"
        if p.name == "clip_slots" or p.name.endswith("clip_slots"):
            return_type = "list[ClipSlot]"
        if p.name == "track" or p.name.endswith("track"):
            return_type = "Track"
        if p.name == "tracks" or p.name.endswith("tracks"):
            return_type = "list[Track]"
        if p.name == "scene" or p.name.endswith("scene"):
            return_type = "Scene"
        if p.name == "scenes" or p.name.endswith("scenes"):
            return_type = "list[Scene]"
        if p.name == "device" or p.name.endswith("device"):
            return_type = "Device"
        if p.name == "devices" or p.name.endswith("devices"):
            return_type = "list[Device]"
        if p.name == "parameter" or p.name.endswith("parameter"):
            return_type = "DeviceParameter"
        if p.name == "parameters" or p.name.endswith("parameters"):
            return_type = "list[DeviceParameter]"
        if p.name == "tempo":
            return_type = "float"
        if p.name == "name" or p.name.endswith("name"):
            return_type = "str"
        if p.name == "value" or p.name.endswith("value"):
            return_type = "int | float"
        if p.name == "min":
            return_type = "int | float"
        if p.name == "max":
            return_type = "int | float"
        if p.name.startswith("can_") or p.name.startswith("is_") or p.name.startswith("has_"):
            return_type = "bool"

        if p.name == "view":
            return_type = "View"
        handle.write(f"{ind}@property")
        handle.write(NEWLINE)
        handle.write(f"{ind}def {p.name}(self) -> {return_type}:")
        handle.write(NEWLINE)
        if p.doc_string:
            handle.write(format_docstring(s=p.doc_string, i=member_ind))
            handle.write(NEWLINE)
        handle.write(f"{member_ind}pass")
        handle.write(NEWLINE)
        if p.doc_string:
            lower_doc = p.doc_string.lower()
            if "get/set" in lower_doc or "read/write" in lower_doc or "read, write" in lower_doc:
                handle.write(NEWLINE * 2)
                handle.write(f"{ind}@{p.name}.setter")
                handle.write(NEWLINE)
                handle.write(f"{ind}def {p.name}(self, value: {return_type}) -> None:")
                handle.write(NEWLINE)
                handle.write(f"{member_ind}pass")
                handle.write(NEWLINE)
    else:
        formatted_value = p.value
        if isinstance(formatted_value, str) and formatted_value.startswith("<attribute"):
            formatted_value = "None"
        if p.property_type == "str":
            formatted_value = f'"{formatted_value}"'
        handle.write(f"{ind}{p.name} = {formatted_value}")
    handle.write(NEWLINE)


def format_routine_param(p: RoutineParam) -> str:
    basic_values = ["int", "float", "bool", "str", "Callable", "int | float"]
    formatted = p.name
    if p.name == "self":
        return formatted
    if not p.param_type:
        formatted = f"{p.name}: Any"
    formatted = f"{p.name}: {p.param_type}" if p.param_type in basic_values else f"{p.name}: object"
    if p.default_value:
        if p.param_type == "str":
            formatted += " = ''"
        elif p.param_type == "int":
            formatted += " = 0"
        elif p.param_type == "bool":
            formatted += f" = {p.default_value}"
        else:
            formatted += " = None"
    return formatted


def write_routine(*, routine: Routine, handle: TextIO, nesting: int, is_method: bool = True) -> None:
    ind = SPACE * INDENT * nesting
    member_ind = ind + SPACE * INDENT
    if routine.name.endswith("_listener"):
        routine.parameters[-1].name = "listener"
        routine.parameters[-1].param_type = "Callable"
    return_type = routine.return_type
    if return_type and return_type != "None" and return_type[0].isupper():
        return_type = f"{return_type}"
    if is_method:
        routine.parameters = [RoutineParam(name="self", default_value=None, param_type=""), *routine.parameters]
    handle.write(
        f"{ind}def {routine.name}({', '.join([format_routine_param(p) for p in routine.parameters])}) "
        f"-> {return_type}:\n",
    )

    if routine.doc_string:
        handle.write(format_docstring(s=routine.doc_string, i=member_ind))
        handle.write(NEWLINE)
    handle.write(f"{member_ind}pass")
    handle.write(NEWLINE * 2)


def write_module(
    *,
    path: Path = OUTPUT_PATH,
    mod: Module,
    all_modules: list[Module],
    clean_path: bool = False,
) -> None:
    if clean_path:
        shutil.rmtree(path)
        Path.mkdir(path)
    module_path = path.joinpath(mod.name)
    Path.mkdir(module_path, parents=True)
    with open(module_path.joinpath("__init__.py"), "w") as out:
        if mod.doc_string:
            out.write(f'"""{mod.doc_string}"""\n')
        out.write(NEWLINE * 2)
        out.write("from __future__ import annotations")
        out.write(NEWLINE)
        out.write("from typing import Any")
        out.write(NEWLINE)
        out.write("from typing import Callable")
        out.write(NEWLINE * 2)

        written_paths: list[str] = []
        for m in mod.modules:
            write_module(path=module_path, mod=m, all_modules=all_modules)
            out.write(f"import {m.path}")
            written_paths.append(m.path)
            out.write(NEWLINE)
        for m in all_modules:
            if m.path not in written_paths and m.path != mod.path:
                out.write(f"from {m.path} import *")
                out.write(NEWLINE)
        out.write(NEWLINE * 2)

        for c in mod.classes:
            write_class(cls=c, handle=out, nesting=0)
        for r in mod.routines:
            write_routine(routine=r, handle=out, nesting=0, is_method=False)
        for p in mod.properties:
            write_property(p=p, handle=out, nesting=0)


def add_all_modules(*, module: Module) -> list[Module]:
    all_modules: list[Module] = []
    all_modules.append(module)
    for m in module.modules:
        all_modules.extend(add_all_modules(module=m))

    return all_modules

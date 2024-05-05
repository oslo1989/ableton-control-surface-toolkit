from __future__ import annotations

import enum
import inspect
import os
from types import ModuleType
from typing import Any, Callable, Generator

from .models import Enum, Klazz, Module, ProcessMemberResult, Property, Routine, RoutineParam, RoutineType


def standard_lib_names_gen(include_underscored: bool = False) -> Generator[str, None, None]:
    standard_lib_dir = os.path.dirname(os.__file__)
    for filename in os.listdir(standard_lib_dir):
        if not include_underscored and filename.startswith("_"):
            continue
        filepath = os.path.join(standard_lib_dir, filename)
        name, ext = os.path.splitext(filename)
        if filename.endswith(".py") and os.path.isfile(filepath):
            if str.isidentifier(name):
                yield name
        elif os.path.isdir(filepath) and "__init__.py" in os.listdir(filepath):
            yield name


def std_modules() -> list[str]:
    return list(standard_lib_names_gen())


def process_class(member: tuple[str, Any], path: str, doc: str | None = None) -> Klazz:
    members = [m for m in inspect.getmembers(member[1]) if not filter_member(m)]
    results: list[ProcessMemberResult] = []
    all_classes: list[Klazz] = []
    all_enums: list[Enum] = []
    all_properties: list[Property] = []
    all_routines: list[Routine] = []
    for m in members:
        results.append(process_member(m, path=f"{path}.{member[0]}"))
    for r in results:
        all_classes += r.classes
        all_enums += r.enums
        all_properties += r.properties
        all_routines += r.routines
    return Klazz(
        path=path,
        doc_string=doc,
        name=member[0],
        classes=all_classes,
        enums=all_enums,
        properties=all_properties,
        routines=all_routines,
    )


def process_routine(
    member: tuple[str, Callable],
    path: str,
    doc: str | None = None,
    process_params: bool = True,
) -> Routine:
    # if first param is self, it is a method
    return_type = "Any"
    param_type = "Any"
    routine_type = RoutineType.FUNCTION
    parameters: list[RoutineParam] = []
    if process_params:
        parameters = [
            RoutineParam(name=p, param_type=param_type, default_value=None)
            for p in inspect.signature(member[1]).parameters
        ]
        if parameters and parameters[0].name == "self":
            routine_type = RoutineType.METHOD
            if len(parameters) > 1:
                parameters = parameters[1:]
    else:
        if doc and doc.startswith(member[0]):
            first_line = doc.split("\n")[0]
            first_line = first_line[len(member[0]) + 1 :]
            [raw_params_str, return_type] = first_line.split("->")
            raw_params = raw_params_str.replace("[", "").replace("]", "").split(",")  # type: ignore[assignment]
            raw_params = [p.strip() for p in raw_params]  # type: ignore[assignment]
            raw_params[-1] = raw_params[-1][:-1]  # type: ignore[index]
            if raw_params[0] == "":
                raw_params = []
            raw_params = [p.replace("(", " ").replace(")", " ").strip() for p in raw_params]  # type: ignore[assignment]
            if raw_params and raw_params[0][0].isupper():
                routine_type = RoutineType.METHOD
                raw_params = raw_params[1:] if len(raw_params) > 1 else []
            for p in raw_params:
                splitted = p.split(" ")
                name = splitted[1]
                param_type = splitted[0]
                default_value = None
                name_split = splitted[1].split("=")

                if len(name_split) == 2:
                    name = name_split[0]
                    default_value = name_split[1]

                parameters.append(
                    RoutineParam(
                        name=name,
                        param_type=param_type,
                        default_value=default_value,
                    ),
                )
            return_type = return_type.replace(":", " ").strip()
    return Routine(
        doc_string=doc,
        name=member[0],
        routine_type=routine_type,
        parameters=parameters,
        path=path,
        return_type=return_type,
    )


def process_enum(member: tuple[str, Any], path: str, doc: str | None = None) -> Enum:
    return Enum(
        doc_string=doc,
        name=member[0],
        path=path,
        values=[m.name for m in member[1]],
    )


def process_boost_enum(member: tuple[str, Any], path: str, doc: str | None = None) -> Klazz:
    new_doc = f"Class that represent an enumeration of values for {member[0]}"
    doc = new_doc + f"\n{doc}" if doc else new_doc
    names = member[1].names
    properties: list[Property] = []
    for idx, v in enumerate(names):
        properties.append(
            Property(
                doc_string=None,
                path=f"{path}.{member[0]}",
                name=v,
                value=idx,
                property_type="int",
            ),
        )
    return Klazz(
        name=member[0],
        doc_string=doc,
        classes=[],
        properties=properties,
        enums=[],
        path=path,
        routines=[],
    )


def process_property(
    member: tuple[str, Any],
    path: str,
    ttyp: str | Any,
    doc: str | None = None,
) -> Property:
    if ttyp:
        ttyp = ttyp.__name__  # type: ignore[union-attr]
    if ttyp is None and (member[0].startswith("is_") or member[0].startswith("has_") or member[0].startswith("can_")):
        ttyp = "bool"
    return Property(
        path=path,
        name=member[0],
        value=str(member[1]),
        property_type=ttyp,
        doc_string=doc,
    )


def process_member(member: tuple[str, Any], path: str = "") -> ProcessMemberResult:
    doc = inspect.getdoc(member[1])
    # logging.info("------------------------------------------------------------------------------------")
    # logging.info(f"DOC: {doc}")
    # logging.info(f"NAME: {member[0]}")
    # logging.info(f"TYPE: {type(member[1])}")
    # logging.info(str(type(member[1])))
    # logging.info(f"MEMBERS: {inspect.getmembers(member[1])}")
    # logging.info(f"INSPECT class: {inspect.isclass(member[1])}")
    # logging.info(f"INSPECT method: {inspect.isroutine(member[1])}")

    result = ProcessMemberResult(
        routines=[],
        enums=[],
        classes=[],
        properties=[],
    )
    if str(type(member[1])) == "<class 'Boost.Python.function'>":
        result.routines.append(process_routine(member, path, doc=doc, process_params=False))
    elif str(type(member[1])) == "<class 'property'>":
        result.properties.append(process_property(member, path, None, doc=doc))
    elif inspect.ismethoddescriptor(member[1]):
        result.routines.append(process_routine(member, path, doc=doc, process_params=False))
    elif inspect.ismodule(member[1]):
        result.module = process_module(member, path=path, doc=doc)
    elif inspect.isfunction(member[1]):
        result.routines.append(process_routine(member, path, doc=doc))
    elif inspect.ismethod(member[1]):
        result.routines.append(process_routine(member, path, doc=doc))
    elif inspect.isclass(member[1]):
        if issubclass(member[1], enum.Enum):
            result.enums.append(process_enum(member, path, doc=doc))
        elif hasattr(member[1], "values") and hasattr(member[1], "names"):
            result.classes.append(process_boost_enum(member, path, doc=doc))
        else:
            result.classes.append(process_class(member, path, doc=doc))
    else:
        if member[0] == "__annotations__":
            for k in member[1]:
                result.properties.append(process_property((k, None), path, member[1][k]))
        else:
            result.properties.append(process_property(member, path, type(member[1])))
    return result


def filter_member(member: tuple[str, Any]) -> bool:
    if isinstance(member[1], str) and member[1].startswith("_"):
        return True
    if isinstance(member[0], str) and member[0].startswith("_"):
        return True
    try:
        if inspect.isbuiltin(member[1]):
            if str(type(member[1])) == "<class 'Boost.Python.function'>":
                return False
            return True
        if inspect.ismodule(member[1]) and member[1].__name__ in std_modules():
            return True
    except AttributeError:
        pass
    if member[0] == "__annotations__":
        return False
    if member[0].startswith("__"):
        return True
    return False


def process_module(
    m: tuple[str, ModuleType] | ModuleType,
    path: str = "",
    doc: str | None = None,
) -> Module:
    all_modules: list[Module] = []
    all_classes: list[Klazz] = []
    all_enums: list[Enum] = []
    all_properties: list[Property] = []
    all_routines: list[Routine] = []
    if not isinstance(m, tuple):
        m = (m.__name__, m)
    if not doc:
        doc = inspect.getdoc(m[1])
    path = m[0] if not path else f"{path}.{m[0]}"
    results: list[ProcessMemberResult] = []
    if inspect.ismodule(m[1]):
        for member in [member for member in inspect.getmembers(m[1]) if not filter_member(member)]:
            if m[1] == member[1]:
                continue
            result = process_member(member, path=path)
            results.append(result)
        for r in results:
            if r.module:
                all_modules = [*all_modules, r.module]
            all_classes += r.classes or []
            all_enums += r.enums or []
            all_properties += r.properties or []
            all_routines += r.routines or []
        return Module(
            path=path,
            name=m[0],
            doc_string=doc,
            modules=all_modules,
            classes=all_classes,
            routines=all_routines,
            properties=all_properties,
            enums=all_enums,
        )
    raise RuntimeError(f"passed object {m} is not a module")

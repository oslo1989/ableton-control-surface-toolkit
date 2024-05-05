from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Member:
    name: Any
    value: Any
    member_type: Any


@dataclass
class ObjectType:
    doc_string: str | None
    path: str
    name: str


@dataclass
class Enum(ObjectType):
    values: list[str]


class RoutineType:
    METHOD = "METHOD"
    FUNCTION = "FUNCTION"


@dataclass
class RoutineParam:
    name: str
    param_type: str
    default_value: str | None


@dataclass
class Routine(ObjectType):
    parameters: list[RoutineParam]
    routine_type: str
    return_type: str


@dataclass
class Property(ObjectType):
    value: Any
    property_type: str


@dataclass
class Klazz(ObjectType):
    routines: list[Routine]
    classes: list[Klazz]
    enums: list[Enum]
    properties: list


@dataclass
class Module(Klazz):
    modules: list[Module]


@dataclass
class ProcessMemberResult:
    classes: list[Klazz] = field(default_factory=list)
    enums: list[Enum] = field(default_factory=list)
    properties: list[Property] = field(default_factory=list)
    routines: list[Routine] = field(default_factory=list)
    module: Module | None = None

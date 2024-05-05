# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/display/type_decl.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1109 bytes
from typing import Any, Callable, NamedTuple, TypeVar

from .state import State


class Event(NamedTuple):
    name: str
    origin: Any
    value: Any


INIT_EVENT = Event(name="init", origin=None, value=None)
DISCONNECT_EVENT = Event(name="disconnect", origin=None, value=None)
ContentType = TypeVar("ContentType")
Render = Callable[([State], ContentType)]

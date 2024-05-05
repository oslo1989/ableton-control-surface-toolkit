# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/display/event_signal/core.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 524 bytes
from typing import Any

from notifications.type_decl import NOTIFICATION_EVENT_ID

from ..state import State
from ..type_decl import Event
from .type_decl import EventSignalFn


def on_notification() -> EventSignalFn[Any]:
    def signal_fn(_: State, event: Event):
        if event.name == NOTIFICATION_EVENT_ID:
            return event.value
        return None

    return signal_fn

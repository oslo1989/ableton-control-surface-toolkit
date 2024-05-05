# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/display/notifications/util.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 597 bytes
from __future__ import annotations

from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from typing_extensions import LiteralString
else:
    LiteralString = str


def toggle_text_generator(format_string: LiteralString) -> Callable[[bool], str]:
    def notification_fn(is_on):
        return format_string.format("on" if is_on else "off")

    return notification_fn

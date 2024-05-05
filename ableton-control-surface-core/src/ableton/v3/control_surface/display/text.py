# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/display/text.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 2792 bytes
from collections import UserString
from enum import Enum, auto
from typing import Callable, Tuple

from ...base import as_ascii
from ..elements import adjust_string


class Text(UserString):
    class ContentWidth:
        pass

    class Justification(Enum):
        LEFT = auto()
        CENTER = auto()
        RIGHT = auto()
        NONE = auto()

    def __init__(self, string="", justification=None, max_width=None):
        super().__init__(string)
        self.justification = justification
        self.max_width = max_width

    def as_ascii(self, adjust_string_fn: Callable[([str, int], str)] = adjust_string) -> Tuple[(int, ...)]:
        return tuple(as_ascii(self.as_string(adjust_string_fn=adjust_string_fn)))

    def as_string(self, adjust_string_fn: Callable[([str, int], str)] = adjust_string) -> str:
        max_width = self.max_width = (
            len(self) if (self.max_width is None or isinstance(self.max_width, Text.ContentWidth)) else (self.max_width)
        )
        justify = self.justification or Text.Justification.LEFT
        formatted = adjust_string_fn(str(self), max_width).rstrip() if self else ""
        if justify == Text.Justification.LEFT:
            return formatted.ljust(max_width)
        if justify == Text.Justification.CENTER:
            return formatted.center(max_width)
        if justify == Text.Justification.RIGHT:
            return formatted.rjust(max_width)
        return formatted

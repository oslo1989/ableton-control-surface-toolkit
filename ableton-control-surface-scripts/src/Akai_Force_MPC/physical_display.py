# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Akai_Force_MPC/physical_display.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 714 bytes
from itertools import chain

from ableton.v2.base import clamp
from ableton.v2.control_surface.elements import PhysicalDisplayElement as PhysicalDisplayElementBase


def message_length(message):
    length = len(message)
    return (clamp(length // 128, 0, 127), length % 128)


class PhysicalDisplayElement(PhysicalDisplayElementBase):
    def _build_display_message(self, display):
        message_string = display.display_string.strip()
        return chain(message_length(message_string), self._translate_string(message_string))

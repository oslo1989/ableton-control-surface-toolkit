# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/BLOCKS/button.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 497 bytes
from ableton.v2.base import in_range
from ableton.v2.control_surface.elements import ButtonElement as ButtonElementBase


class ButtonElement(ButtonElementBase):
    def set_light(self, value):
        if isinstance(value, int) and in_range(value, 0, 128):
            self.send_value(value)
        else:
            super().set_light(value)

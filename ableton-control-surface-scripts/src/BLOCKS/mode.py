# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/BLOCKS/mode.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 499 bytes
from ableton.v2.control_surface.control import ButtonControl
from ableton.v2.control_surface.mode import ModesComponent as ModesComponentBase


class ModesComponent(ModesComponentBase):
    cycle_mode_button = ButtonControl()

    @cycle_mode_button.pressed
    def cycle_mode_button(self, button):
        if len(self._mode_list):
            self.cycle_mode(1)

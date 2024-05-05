# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/novation/mode.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 626 bytes
from ableton.v2.control_surface.control import InputControl
from ableton.v2.control_surface.mode import ModesComponent as ModesComponentBase


class ModesComponent(ModesComponentBase):
    __events__ = ("mode_byte",)
    mode_selection_control = InputControl()

    @mode_selection_control.value
    def mode_selection_control(self, value, _):
        modes = self.modes
        if value < len(modes):
            self.selected_mode = modes[value]
            self.notify_mode_byte(value)

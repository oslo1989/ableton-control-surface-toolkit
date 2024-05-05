# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/control/sysex.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1044 bytes
from .control import Control, control_color


class ColorSysexControl(Control):
    class State(Control.State):
        color = control_color("DefaultButton.Disabled")

        def __init__(self, color=None, *a, **k):
            (super(ColorSysexControl.State, self).__init__)(*a, **k)
            if color is not None:
                self.color = color

        def set_control_element(self, control_element):
            super(ColorSysexControl.State, self).set_control_element(control_element)
            self._send_current_color()

        def update(self):
            super(ColorSysexControl.State, self).update()
            self._send_current_color()

        def _send_current_color(self):
            if self._control_element:
                self._control_element.set_light(self.color)

    def __init__(self, *a, **k):
        super().__init__(extra_args=a, extra_kws=k)

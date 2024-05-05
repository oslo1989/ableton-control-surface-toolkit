# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/novation/fixed_radio_button_group.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1151 bytes
from ableton.v2.control_surface.control import RadioButtonGroup


class FixedRadioButtonGroup(RadioButtonGroup):
    def __init__(self, control_count, *a, **k):
        (super().__init__)(a, control_count=control_count, **k)

    class State(RadioButtonGroup.State):
        @property
        def active_control_count(self):
            return self._active_control_count

        @active_control_count.setter
        def active_control_count(self, control_count):
            self._active_control_count = control_count
            for index, control in enumerate(self._controls):
                control._get_state(self._manager).enabled = index < control_count

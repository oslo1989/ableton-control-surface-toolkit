# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_MK2/InControlStatusComponent.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 713 bytes
from _Framework import ControlSurfaceComponent
from _Framework.SubjectSlot import subject_slot


class InControlStatusComponent(ControlSurfaceComponent):
    def __init__(self, set_is_in_control_on, *a, **k):
        (super().__init__)(*a, **k)
        self._set_is_in_control_on = set_is_in_control_on

    def set_in_control_status_button(self, button):
        self._on_in_control_value.subject = button

    @subject_slot("value")
    def _on_in_control_value(self, value):
        self._set_is_in_control_on(value >= 8)

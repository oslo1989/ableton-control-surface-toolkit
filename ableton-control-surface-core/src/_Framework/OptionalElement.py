# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Framework/OptionalElement.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1179 bytes
from .ComboElement import ToggleElement
from .SubjectSlot import SlotManager, subject_slot


class ChoosingElement(ToggleElement, SlotManager):
    def __init__(self, flag=None, *a, **k):
        (super().__init__)(*a, **k)
        self._on_flag_changed.subject = flag
        self._on_flag_changed(flag.value)

    @subject_slot("value")
    def _on_flag_changed(self, value):
        self.set_toggled(value)


class OptionalElement(ChoosingElement):
    def __init__(self, control=None, flag=None, value=None, *a, **k):
        on_control = control if value else None
        off_control = None if value else control
        (super().__init__)(a, on_control=on_control, off_control=off_control, flag=flag, **k)

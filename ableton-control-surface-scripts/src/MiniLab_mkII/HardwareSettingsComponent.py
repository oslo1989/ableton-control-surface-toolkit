# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/MiniLab_mkII/HardwareSettingsComponent.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1302 bytes
from _Arturia.ArturiaControlSurface import OFF_VALUE, ON_VALUE
from _Framework import ControlSurfaceComponent
from _Framework.SubjectSlot import subject_slot

LIVE_MEMORY_SLOT_INDEX = 7


class HardwareSettingsComponent(ControlSurfaceComponent):
    __subject_events__ = ("live_mode",)

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._memory_slot_selection = None
        self._hardware_live_mode_switch = None

    def set_memory_slot_selection(self, selection):
        self._memory_slot_selection = selection
        self._on_memory_slot_changed.subject = selection

    def set_hardware_live_mode_switch(self, switch):
        self._hardware_live_mode_switch = switch

    @subject_slot("value")
    def _on_memory_slot_changed(self, slot_data):
        slot_index = slot_data[0]
        in_live_mode = slot_index == LIVE_MEMORY_SLOT_INDEX
        self.notify_live_mode(in_live_mode)
        if self._hardware_live_mode_switch is not None:
            self._hardware_live_mode_switch.send_value((ON_VALUE if in_live_mode else OFF_VALUE,))

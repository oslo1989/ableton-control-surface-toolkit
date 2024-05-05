# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_Essential/hardware_settings.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1890 bytes
from ableton.v2.base import listens
from ableton.v2.control_surface import Component

from . import sysex


class HardwareSettingsComponent(Component):
    __events__ = ("daw_preset",)

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._hardware_live_mode_switch = None
        self._memory_preset_switch = None
        self._memory_preset_select_mode_switch = None
        self._selected_preset = None

    def set_hardware_live_mode_switch(self, switch):
        self._hardware_live_mode_switch = switch

    def set_memory_preset_switch(self, switch):
        self._memory_preset_switch = switch
        self._on_memory_preset_changed.subject = switch

    def set_memory_preset_select_mode_switch(self, switch):
        self._memory_preset_select_mode_switch = switch
        self._on_memory_preset_select_mode_enabled.subject = switch

    def set_hardware_live_mode_enabled(self, enable):
        if self._hardware_live_mode_switch:
            if self.is_enabled():
                self._hardware_live_mode_switch.send_value(sysex.ON_VALUE if enable else sysex.OFF_VALUE)

    def select_memory_preset(self, preset_index):
        if self._memory_preset_switch:
            if self.is_enabled():
                self._memory_preset_switch.send_value(preset_index)
                self._selected_preset = preset_index

    @listens("value")
    def _on_memory_preset_changed(self, preset_info):
        self._selected_preset = preset_info[0]

    @listens("value")
    def _on_memory_preset_select_mode_enabled(self, enabled_info):
        enabled = enabled_info[0]
        self.notify_daw_preset(not enabled and self._selected_preset == sysex.DAW_MEMORY_PRESET_INDEX)

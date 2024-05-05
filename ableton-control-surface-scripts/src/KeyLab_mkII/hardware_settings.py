# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_mkII/hardware_settings.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 829 bytes
from KeyLab_Essential import sysex
from KeyLab_Essential.hardware_settings import HardwareSettingsComponent as HardwareSettingsComponentBase


class HardwareSettingsComponent(HardwareSettingsComponentBase):
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._vegas_mode_switch = None

    def set_vegas_mode_switch(self, switch):
        self._vegas_mode_switch = switch

    def set_hardware_live_mode_enabled(self, enable):
        super().set_hardware_live_mode_enabled(enable)
        if enable:
            if self._vegas_mode_switch:
                self._vegas_mode_switch.send_value(sysex.OFF_VALUE)

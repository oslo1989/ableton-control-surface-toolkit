# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Oxygen_Pro_Mini/simple_device.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1197 bytes
from novation.simple_device import SimpleDeviceParameterComponent as SimpleDeviceParameterComponentBase

NUM_CONTROLS = 4


class SimpleDeviceParameterComponent(SimpleDeviceParameterComponentBase):
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._parameter_offset = 0

    def toggle_parameter_offset(self):
        self._parameter_offset = NUM_CONTROLS - self._parameter_offset
        self.update()

    @SimpleDeviceParameterComponentBase.selected_bank.getter
    def selected_bank(self):
        bank = self._banks[0] or []
        if self._parameter_offset:
            if len(bank) > self._parameter_offset:
                offset_bank = bank[self._parameter_offset :]
                if any(offset_bank):
                    return offset_bank
        return bank

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/device_bank_registry.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1683 bytes
from ..base import EventObject, liveobj_valid


class DeviceBankRegistry(EventObject):
    __events__ = ("device_bank",)

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._device_bank_registry = {}
        self._device_bank_listeners = []

    def compact_registry(self):
        newreg = dict(filter(lambda kv: liveobj_valid(kv[0]), self._device_bank_registry.items()))
        self._device_bank_registry = newreg

    def set_device_bank(self, device, bank):
        key = self._find_device_bank_key(device) or device
        old = self._device_bank_registry.get(key, 0)
        if old != bank:
            self._device_bank_registry[key] = bank
            self.notify_device_bank(device, bank)

    def get_device_bank(self, device):
        if hasattr(device, "bank_index"):
            return device.bank_index
        return self._device_bank_registry.get(self._find_device_bank_key(device), 0)

    def _find_device_bank_key(self, device):
        for k in self._device_bank_registry:
            if k == device:
                return k
        return None

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/OpenLabs/SpecialDeviceComponent.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1055 bytes
from _Framework import DeviceComponent


class SpecialDeviceComponent(DeviceComponent):
    def __init__(self):
        DeviceComponent.__init__(self)

    def _device_parameters_to_map(self):
        return self._device.parameters[1:]

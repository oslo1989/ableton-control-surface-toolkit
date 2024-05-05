# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_Pro/SpecialDeviceComponent.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 947 bytes
from _Framework import DeviceComponent

from .consts import DEVICE_MAP_CHANNEL, FADER_TYPE_STANDARD


class SpecialDeviceComponent(DeviceComponent):
    def set_parameter_controls(self, controls):
        if controls:
            for control in controls:
                control.set_channel(DEVICE_MAP_CHANNEL)
                control.set_light_and_type("Device.On", FADER_TYPE_STANDARD)

        super().set_parameter_controls(controls)

    def _update_parameter_controls(self):
        if self._parameter_controls is not None:
            for control in self._parameter_controls:
                control.update()

    def update(self):
        super().update()
        if self.is_enabled():
            self._update_parameter_controls()

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/spectral.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1706 bytes
from ableton.v2.base import EventObject
from ableton.v2.control_surface import LiveObjectDecorator, get_parameter_by_name

from .device_options import DeviceOnOffOption, DeviceSwitchOption


class SpectralDeviceDecorator(LiveObjectDecorator, EventObject):
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self.freeze_option = DeviceOnOffOption(name="Frozen", property_host=(get_parameter_by_name(self, "Frozen")))
        self.unit_option = DeviceSwitchOption(
            name="Unit",
            parameter=(get_parameter_by_name(self, "Unit")),
            labels=["ms", "Notes"],
        )
        self.delay_unit_option = DeviceSwitchOption(
            name="Delay Dly. Unit",
            parameter=(get_parameter_by_name(self, "Delay Dly. Unit")),
            labels=["ms", "Notes", "16th", "Tr", "Dt"],
        )
        self.fade_type_option = DeviceSwitchOption(
            name="Fade Type",
            parameter=(get_parameter_by_name(self, "Fade Type")),
            labels=["X-Fade", "Env"],
        )
        self.register_disconnectables(self.options)

    @property
    def options(self):
        return (self.freeze_option, self.unit_option, self.delay_unit_option, self.fade_type_option)

    @property
    def parameters(self):
        return tuple(self._live_object.parameters) + self._additional_parameters

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/device_decorators.py
# Compiled at: 2023-12-21 15:35:35
# Size of source mod 2**32: 3205 bytes
from ableton.v2.control_surface import DelayDeviceDecorator, LiveObjectDecorator, SimplerDeviceDecorator
from ableton.v2.control_surface import DeviceDecoratorFactory as DeviceDecoratorFactoryBase


class DeviceDecorator(LiveObjectDecorator):
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self.create_additional_parameters()
        self.register_disconnectables(self.options)

    def create_additional_parameters(self):
        raise NotImplementedError("Must implement this method to create additional parameters for the device")


class TransmuteDeviceDecorator(DeviceDecorator):
    def create_additional_parameters(self):
        self._add_non_automatable_enum_parameter(
            name="Hz/Note Mode",
            list="frequency_dial_mode_list",
            index="frequency_dial_mode",
        )
        self._add_non_automatable_enum_parameter(name="Pitch Mode", list="pitch_mode_list", index="pitch_mode")


class DriftDeviceDecorator(DeviceDecorator):
    def create_additional_parameters(self):
        self._add_non_automatable_enum_parameter(name="Voice Mode", list="voice_mode_list", index="voice_mode_index")
        self._add_non_automatable_enum_parameter(name="Voice Count", list="voice_count_list", index="voice_count_index")
        self._add_non_automatable_enum_parameter(
            name="LP Mod Src 1",
            list="mod_matrix_filter_source_1_list",
            index="mod_matrix_filter_source_1_index",
        )
        self._add_non_automatable_enum_parameter(
            name="LP Mod Src 2",
            list="mod_matrix_filter_source_2_list",
            index="mod_matrix_filter_source_2_index",
        )


class RoarDeviceDecorator(DeviceDecorator):
    def create_additional_parameters(self):
        self._add_non_automatable_enum_parameter(name="Routing", list="routing_mode_list", index="routing_mode_index")


class DeviceDecoratorFactory(DeviceDecoratorFactoryBase):
    DECORATOR_CLASSES = {
        "Delay": DelayDeviceDecorator,
        "Drift": DriftDeviceDecorator,
        "OriginalSimpler": SimplerDeviceDecorator,
        "Roar": RoarDeviceDecorator,
        "Transmute": TransmuteDeviceDecorator,
    }

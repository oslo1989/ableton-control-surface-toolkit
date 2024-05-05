# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/reverb.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 2535 bytes
from ableton.v2.base import EventObject
from ableton.v2.control_surface import LiveObjectDecorator, get_parameter_by_name

from .device_options import DeviceOnOffOption, DeviceSwitchOption


class ReverbDeviceDecorator(LiveObjectDecorator, EventObject):
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self.in_locut_option = DeviceOnOffOption(
            name="In LoCut",
            property_host=(get_parameter_by_name(self, "In LowCut On")),
        )
        self.in_hicut_option = DeviceOnOffOption(
            name="In HiCut",
            property_host=(get_parameter_by_name(self, "In HighCut On")),
        )
        self.spinOn_option = DeviceOnOffOption(
            name="ER Spin",
            property_host=(get_parameter_by_name(self, "ER Spin On")),
        )
        self.loshelf_option = DeviceOnOffOption(
            name="Lo Shelf",
            property_host=(get_parameter_by_name(self, "LowShelf On")),
        )
        self.hishelf_option = DeviceOnOffOption(
            name="Hi Filter",
            property_host=(get_parameter_by_name(self, "HiFilter On")),
        )
        self.flat_option = DeviceOnOffOption(name="Flat", property_host=(get_parameter_by_name(self, "Flat On")))
        self.cut_option = DeviceOnOffOption(name="Cut", property_host=(get_parameter_by_name(self, "Cut On")))
        self.freeze_option = DeviceOnOffOption(name="Freeze", property_host=(get_parameter_by_name(self, "Freeze On")))
        self.chorus_option = DeviceOnOffOption(name="Chorus", property_host=(get_parameter_by_name(self, "Chorus On")))
        self.diff_filter_type_option = DeviceSwitchOption(
            name="Hi Fil Type",
            parameter=(get_parameter_by_name(self, "HiFilter Type")),
        )
        self.register_disconnectables(self.options)

    @property
    def options(self):
        return (
            self.in_locut_option,
            self.in_hicut_option,
            self.spinOn_option,
            self.loshelf_option,
            self.hishelf_option,
            self.flat_option,
            self.cut_option,
            self.freeze_option,
            self.chorus_option,
            self.diff_filter_type_option,
        )

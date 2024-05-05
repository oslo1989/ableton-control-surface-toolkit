# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/redux2.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 861 bytes
from ableton.v2.base import EventObject
from ableton.v2.control_surface import LiveObjectDecorator, get_parameter_by_name

from .device_options import DeviceOnOffOption


class Redux2DeviceDecorator(LiveObjectDecorator, EventObject):
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self.postFilter_on_option = DeviceOnOffOption(
            name="Post-Filter",
            property_host=(get_parameter_by_name(self, "Post-Filter On")),
        )
        self.register_disconnectables(self.options)

    @property
    def options(self):
        return (self.postFilter_on_option,)

    @property
    def parameters(self):
        return tuple(self._live_object.parameters)

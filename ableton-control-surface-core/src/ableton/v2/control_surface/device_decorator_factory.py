# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/device_decorator_factory.py
# Compiled at: 2023-12-21 15:35:35
# Size of source mod 2**32: 1474 bytes
from ableton.v2.base import liveobj_valid
from ableton.v2.control_surface import DecoratorFactory

from .delay_decoration import DelayDeviceDecorator
from .drift_decoration import DriftDeviceDecorator
from .roar_decoration import RoarDeviceDecorator
from .simpler_decoration import SimplerDeviceDecorator
from .wavetable_decoration import WavetableDeviceDecorator


class DeviceDecoratorFactory(DecoratorFactory):
    DECORATOR_CLASSES = {
        "Delay": DelayDeviceDecorator,
        "Drift": DriftDeviceDecorator,
        "Roar": RoarDeviceDecorator,
        "OriginalSimpler": SimplerDeviceDecorator,
        "InstrumentVector": WavetableDeviceDecorator,
    }

    @classmethod
    def generate_decorated_device(cls, device, additional_properties=None, song=None, *a, **k):
        if additional_properties is None:
            additional_properties = {}
        return (cls.DECORATOR_CLASSES[device.class_name])(
            a,
            live_object=device,
            additional_properties=additional_properties,
            **k,
        )

    @classmethod
    def _should_be_decorated(cls, device):
        return liveobj_valid(device) and device.class_name in cls.DECORATOR_CLASSES

    def _get_decorated_object(self, device, additional_properties, song=None, *a, **k):
        return (self.generate_decorated_device)(device, *a, additional_properties=additional_properties, **k)

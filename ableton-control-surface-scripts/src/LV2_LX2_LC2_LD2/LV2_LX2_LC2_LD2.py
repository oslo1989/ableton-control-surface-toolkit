# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/LV2_LX2_LC2_LD2/LV2_LX2_LC2_LD2.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1149 bytes
from .consts import *
from .FaderfoxScript import FaderfoxScript
from .LV2DeviceController import LV2DeviceController
from .LV2MixerController import LV2MixerController
from .LV2TransportController import LV2TransportController


class LV2_LX2_LC2_LD2(FaderfoxScript):
    __module__ = __name__
    __doc__ = "Automap script for LV2 Faderfox controllers"
    __name__ = "LV2_LX2_LC2_LD2 Remote Script"

    def __init__(self, c_instance):
        LV2_LX2_LC2_LD2.realinit(self, c_instance)

    def realinit(self, c_instance):
        self.suffix = "2"
        FaderfoxScript.realinit(self, c_instance)
        self.mixer_controller = LV2MixerController(self)
        self.device_controller = LV2DeviceController(self)
        self.transport_controller = LV2TransportController(self)
        self.components = [self.mixer_controller, self.device_controller, self.transport_controller]

    def suggest_map_mode(self, cc_no, channel):
        return -1

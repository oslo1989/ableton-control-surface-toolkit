# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/AIRA_MX_1/__init__.py
# Compiled at: 2023-12-21 15:36:02
# Size of source mod 2**32: 718 bytes
from _Framework.Capabilities import CONTROLLER_ID_KEY, PORTS_KEY, SCRIPT, controller_id, inport, outport

from .RolandMX1 import RolandMX1


def get_capabilities():
    return {
        CONTROLLER_ID_KEY: controller_id(vendor_id=1410, product_ids=[419], model_name=["MX-1"]),
        PORTS_KEY: [inport(props=[]), inport(props=[SCRIPT]), outport(props=[]), outport(props=[SCRIPT])],
    }


def create_instance(c_instance):
    return RolandMX1(c_instance=c_instance)

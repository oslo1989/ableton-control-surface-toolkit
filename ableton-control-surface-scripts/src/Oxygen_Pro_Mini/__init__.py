# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Oxygen_Pro_Mini/__init__.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 876 bytes
from ableton.v2.control_surface.capabilities import (
    CONTROLLER_ID_KEY,
    NOTES_CC,
    PORTS_KEY,
    REMOTE,
    SCRIPT,
    controller_id,
    inport,
    outport,
)

from .oxygen_pro_mini import Oxygen_Pro_Mini


def get_capabilities():
    return {
        CONTROLLER_ID_KEY: controller_id(vendor_id=1891, product_ids=[4155], model_name=["Oxygen Pro Mini"]),
        PORTS_KEY: [
            inport(props=[NOTES_CC, REMOTE]),
            inport(props=[]),
            inport(props=[NOTES_CC, SCRIPT]),
            outport(props=[]),
            outport(props=[]),
            outport(props=[SCRIPT]),
        ],
    }


def create_instance(c_instance):
    return Oxygen_Pro_Mini(c_instance=c_instance)

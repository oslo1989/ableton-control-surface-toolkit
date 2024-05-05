# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_X/__init__.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 831 bytes
from ableton.v2.control_surface.capabilities import (
    CONTROLLER_ID_KEY,
    NOTES_CC,
    PORTS_KEY,
    REMOTE,
    SCRIPT,
    SYNC,
    controller_id,
    inport,
    outport,
)

from .launchpad_x import Launchpad_X


def get_capabilities():
    return {
        CONTROLLER_ID_KEY: controller_id(vendor_id=4661, product_ids=[259], model_name=["Launchpad X"]),
        PORTS_KEY: [
            inport(props=[NOTES_CC, SCRIPT]),
            inport(props=[NOTES_CC, REMOTE]),
            outport(props=[NOTES_CC, SYNC, SCRIPT]),
            outport(props=[REMOTE]),
        ],
    }


def create_instance(c_instance):
    return Launchpad_X(c_instance=c_instance)

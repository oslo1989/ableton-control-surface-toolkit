# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/SL_MkIII/__init__.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 920 bytes
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

from .sl_mkiii import SLMkIII


def get_capabilities():
    return {
        CONTROLLER_ID_KEY: controller_id(vendor_id=4661, product_ids=[257], model_name=["Novation SL MkIII"]),
        PORTS_KEY: [
            inport(props=[NOTES_CC, REMOTE]),
            inport(props=[NOTES_CC, SCRIPT, REMOTE]),
            inport(props=[NOTES_CC, REMOTE]),
            outport(props=[]),
            outport(props=[NOTES_CC, SCRIPT]),
            outport(props=[]),
            outport(props=[]),
        ],
    }


def create_instance(c_instance):
    return SLMkIII(c_instance=c_instance)

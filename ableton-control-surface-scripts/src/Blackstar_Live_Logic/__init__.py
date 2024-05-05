# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Blackstar_Live_Logic/__init__.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 815 bytes
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

from .blackstar_live_logic import Blackstar_Live_Logic


def get_capabilities():
    return {
        CONTROLLER_ID_KEY: controller_id(
            vendor_id=10196,
            product_ids=[4097],
            model_name=["Live Logic MIDI Controller"],
        ),
        PORTS_KEY: [inport(props=[SCRIPT, REMOTE, NOTES_CC]), outport(props=[SCRIPT, REMOTE, NOTES_CC])],
    }


def create_instance(c_instance):
    return Blackstar_Live_Logic(c_instance=c_instance)

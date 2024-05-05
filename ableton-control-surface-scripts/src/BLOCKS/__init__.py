# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/BLOCKS/__init__.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 717 bytes
from ableton.v2.control_surface import capabilities as caps

from .blocks import Blocks


def get_capabilities():
    return {
        caps.CONTROLLER_ID_KEY: caps.controller_id(
            vendor_id=10996,
            product_ids=[2304],
            model_name=["Lightpad BLOCK", "BLOCKS"],
        ),
        caps.PORTS_KEY: [
            caps.inport(props=[caps.NOTES_CC, caps.SCRIPT]),
            caps.outport(props=[caps.NOTES_CC, caps.SCRIPT]),
        ],
        caps.TYPE_KEY: "blocks",
    }


def create_instance(c_instance):
    return Blocks(c_instance=c_instance)

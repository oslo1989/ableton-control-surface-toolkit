# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/iRig_Keys_IO/__init__.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 750 bytes
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

from .irig_keys_io import IRigKeysIO


def get_capabilities():
    return {
        CONTROLLER_ID_KEY: controller_id(
            vendor_id=6499,
            product_ids=[46, 45],
            model_name=["iRig Keys IO 25", "iRig Keys IO 49"],
        ),
        PORTS_KEY: [inport(props=[NOTES_CC, SCRIPT, REMOTE]), outport(props=[SCRIPT])],
    }


def create_instance(c_instance):
    return IRigKeysIO(c_instance=c_instance)

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/APC40_MkII/__init__.py
# Compiled at: 2023-11-21 10:21:17
# Size of source mod 2**32: 767 bytes
from _Framework.Capabilities import (
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

from .APC40_MkII import APC40_MkII


def create_instance(c_instance):
    return APC40_MkII(c_instance)


def get_capabilities():
    return {
        CONTROLLER_ID_KEY: controller_id(
            vendor_id=2536,
            product_ids=[41],
            model_name=["APC40 mkII", "Akai APC40 MkII"],
        ),
        PORTS_KEY: [inport(props=[NOTES_CC, SCRIPT, REMOTE]), outport(props=[SYNC, SCRIPT, REMOTE])],
    }

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Roland_A_PRO/__init__.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 805 bytes
from _Framework.Capabilities import (
    CONTROLLER_ID_KEY,
    NOTES_CC,
    PORTS_KEY,
    REMOTE,
    SCRIPT,
    controller_id,
    inport,
    outport,
)

from .Roland_A_PRO import Roland_A_PRO


def get_capabilities():
    return {
        CONTROLLER_ID_KEY: controller_id(vendor_id=1410, product_ids=[271], model_name="A-PRO"),
        PORTS_KEY: [
            inport(props=[]),
            inport(props=[NOTES_CC, REMOTE]),
            inport(props=[NOTES_CC, SCRIPT, REMOTE]),
            outport(props=[]),
            outport(props=[SCRIPT]),
        ],
    }


def create_instance(c_instance):
    return Roland_A_PRO(c_instance)

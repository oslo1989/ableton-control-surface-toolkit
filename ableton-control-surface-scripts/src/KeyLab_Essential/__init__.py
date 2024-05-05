# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_Essential/__init__.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 900 bytes
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

from .keylab_essential import KeyLabEssential


def get_capabilities():
    return {
        CONTROLLER_ID_KEY: controller_id(
            vendor_id=7285,
            product_ids=[586, 650],
            model_name=["Arturia KeyLab Essential 49", "Arturia KeyLab Essential 61"],
        ),
        PORTS_KEY: [
            inport(props=[NOTES_CC, REMOTE]),
            inport(props=[NOTES_CC, SCRIPT, REMOTE]),
            outport(props=[]),
            outport(props=[SCRIPT]),
        ],
    }


def create_instance(c_instance):
    return KeyLabEssential(c_instance=c_instance)

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Novation_Impulse/__init__.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1163 bytes
from _Framework.Capabilities import *

from .Novation_Impulse import Novation_Impulse


def create_instance(c_instance):
    return Novation_Impulse(c_instance)


def get_capabilities():
    return {
        CONTROLLER_ID_KEY: controller_id(vendor_id=4661, product_ids=[25], model_name="Impulse 25"),
        PORTS_KEY: [
            inport(props=[NOTES_CC, REMOTE, SCRIPT]),
            inport(props=[NOTES_CC, REMOTE]),
            outport(props=[NOTES_CC, REMOTE, SCRIPT]),
        ],
    }

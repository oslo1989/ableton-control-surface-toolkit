# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Axiom_AIR_25_49_61/__init__.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 808 bytes
from _Framework.Capabilities import CONTROLLER_ID_KEY, NOTES_CC, PORTS_KEY, SCRIPT, controller_id, inport, outport

from .Axiom_AIR_25_49_61 import Axiom_AIR_25_49_61


def get_capabilities():
    return {
        CONTROLLER_ID_KEY: controller_id(vendor_id=1891, product_ids=[8243], model_name="Axiom AIR 49"),
        PORTS_KEY: [
            inport(props=[NOTES_CC]),
            inport(props=[SCRIPT]),
            inport(props=[NOTES_CC]),
            outport(props=[NOTES_CC]),
            outport(props=[SCRIPT]),
        ],
    }


def create_instance(c_instance):
    return Axiom_AIR_25_49_61(c_instance)

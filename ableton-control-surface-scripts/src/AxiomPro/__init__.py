# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/AxiomPro/__init__.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1214 bytes
from _Framework.Capabilities import *

from .AxiomPro import AxiomPro


def create_instance(c_instance):
    return AxiomPro(c_instance)


def get_capabilities():
    return {
        CONTROLLER_ID_KEY: controller_id(vendor_id=1891, product_ids=[8227], model_name="Axiom Pro 49"),
        PORTS_KEY: [
            inport(props=[NOTES_CC]),
            inport(props=[NOTES_CC, SCRIPT]),
            inport(props=[NOTES_CC]),
            inport(props=[NOTES_CC]),
            outport(props=[]),
            outport(props=[SCRIPT]),
        ],
    }

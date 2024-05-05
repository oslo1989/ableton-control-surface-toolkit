# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/MackieControl/__init__.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1277 bytes
from _Framework.Capabilities import *

from .MackieControl import MackieControl


def create_instance(c_instance):
    return MackieControl(c_instance)


def get_capabilities():
    return {
        CONTROLLER_ID_KEY: controller_id(vendor_id=2675, product_ids=[6], model_name="MCU Pro USB v3.1"),
        PORTS_KEY: [
            inport(props=[SCRIPT, REMOTE]),
            inport(props=[]),
            inport(props=[]),
            inport(props=[]),
            outport(props=[SCRIPT, REMOTE]),
            outport(props=[]),
            outport(props=[]),
            outport(props=[]),
        ],
    }

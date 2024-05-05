# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/LPD8/__init__.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1469 bytes
import Live
from _Framework.Capabilities import *
from _Generic import GenericScript

from .config import *


def create_instance(c_instance):
    return GenericScript(
        c_instance,
        Live.MidiMap.MapMode.absolute,
        Live.MidiMap.MapMode.absolute,
        DEVICE_CONTROLS,
        TRANSPORT_CONTROLS,
        VOLUME_CONTROLS,
        TRACKARM_CONTROLS,
        BANK_CONTROLS,
        CONTROLLER_DESCRIPTION,
    )


def get_capabilities():
    return {
        CONTROLLER_ID_KEY: controller_id(vendor_id=2536, product_ids=[117], model_name="LPD8"),
        PORTS_KEY: [inport(props=[NOTES_CC, REMOTE, SCRIPT]), outport(props=[SCRIPT])],
    }

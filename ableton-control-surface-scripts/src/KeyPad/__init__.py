# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyPad/__init__.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 643 bytes
from _Framework.Capabilities import CONTROLLER_ID_KEY, NOTES_CC, PORTS_KEY, SCRIPT, controller_id, inport, outport

from .KeyPad import KeyPad


def get_capabilities():
    return {
        CONTROLLER_ID_KEY: controller_id(vendor_id=9901, product_ids=[28149], model_name="Reloop KeyPad"),
        PORTS_KEY: [inport(props=[NOTES_CC, SCRIPT]), outport(props=[NOTES_CC, SCRIPT])],
    }


def create_instance(c_instance):
    return KeyPad(c_instance)

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/MiniLab_mkII/__init__.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 644 bytes
import _Framework.Capabilities as caps

from .MiniLabMk2 import MiniLabMk2


def get_capabilities():
    return {
        caps.CONTROLLER_ID_KEY: caps.controller_id(
            vendor_id=7285,
            product_ids=[649],
            model_name=["Arturia MiniLab mkII"],
        ),
        caps.PORTS_KEY: [
            caps.inport(props=[caps.NOTES_CC, caps.SCRIPT, caps.REMOTE]),
            caps.outport(props=[caps.SCRIPT]),
        ],
    }


def create_instance(c_instance):
    return MiniLabMk2(c_instance=c_instance)

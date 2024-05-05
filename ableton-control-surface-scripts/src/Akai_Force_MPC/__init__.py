# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Akai_Force_MPC/__init__.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 668 bytes
from ableton.v2.control_surface.capabilities import (
    NOTES_CC,
    PORTS_KEY,
    REMOTE,
    SCRIPT,
    SUGGESTED_PORT_NAMES_KEY,
    inport,
    outport,
)

from .akai_force_mpc import Akai_Force_MPC


def get_capabilities():
    return {
        SUGGESTED_PORT_NAMES_KEY: ["Akai Network - DAW Control"],
        PORTS_KEY: [inport(props=[NOTES_CC, SCRIPT, REMOTE]), outport(props=[NOTES_CC, SCRIPT, REMOTE])],
    }


def create_instance(c_instance):
    return Akai_Force_MPC(c_instance)

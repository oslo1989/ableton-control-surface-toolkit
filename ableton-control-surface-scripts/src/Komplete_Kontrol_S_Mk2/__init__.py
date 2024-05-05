# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Komplete_Kontrol_S_Mk2/__init__.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 458 bytes
from ableton.v2.control_surface.capabilities import SUGGESTED_PORT_NAMES_KEY

from .komplete_kontrol_s_mk2 import Komplete_Kontrol_S_Mk2


def get_capabilities():
    return {SUGGESTED_PORT_NAMES_KEY: ["Komplete Kontrol DAW - 1"]}


def create_instance(c_instance):
    return Komplete_Kontrol_S_Mk2(c_instance=c_instance)

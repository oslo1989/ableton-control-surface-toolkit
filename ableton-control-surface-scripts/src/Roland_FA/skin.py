# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Roland_FA/skin.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 607 bytes
from ableton.v2.control_surface import Skin
from ableton.v2.control_surface.elements import Color


class Colors:
    class DefaultButton:
        On = Color(127)
        Off = Color(0)
        Disabled = Color(0)

    class Transport:
        PlayOn = Color(127)
        PlayOff = Color(0)

    class Recording:
        On = Color(127)
        Off = Color(0)


def make_default_skin():
    return Skin(Colors)

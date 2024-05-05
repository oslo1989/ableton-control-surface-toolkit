# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Oxygen_Pro/colors.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 395 bytes
from ableton.v2.control_surface.elements import Color


class Basic:
    ON = Color(127)
    OFF = Color(0)


class Rgb:
    GREEN = Color(12)
    GREEN_BLINK = Color(76)
    RED = Color(3)
    RED_BLINK = Color(67)
    AMBER = Color(11)
    WHITE = Color(63)

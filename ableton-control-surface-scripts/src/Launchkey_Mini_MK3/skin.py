# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_Mini_MK3/skin.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 872 bytes
from ableton.v2.control_surface import Skin, merge_skins
from novation.colors import Mono, Rgb
from novation.skin import skin as base_skin


class Colors:
    class Recording:
        On = Mono.ON
        Off = Mono.OFF

    class TrackNavigation:
        On = Mono.HALF
        Pressed = Mono.ON

    class SceneNavigation:
        On = Mono.HALF
        Pressed = Mono.ON

    class DrumGroup:
        PadSelected = Rgb.WHITE
        PadSelectedNotSoloed = Rgb.WHITE
        PadMutedSelected = Rgb.WHITE
        PadSoloedSelected = Rgb.WHITE
        Navigation = Rgb.WHITE_HALF
        NavigationPressed = Rgb.WHITE


skin = merge_skins(base_skin, Skin(Colors) * ())

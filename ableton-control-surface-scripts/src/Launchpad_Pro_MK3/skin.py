# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_Pro_MK3/skin.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1264 bytes
from ableton.v2.control_surface import Skin, merge_skins
from novation.colors import Rgb
from novation.skin import skin as base_skin


class Colors:
    class Device:
        Navigation = Rgb.DARK_BLUE_HALF
        NavigationPressed = Rgb.WHITE

    class Mode:
        class Device:
            On = Rgb.DARK_BLUE
            Off = Rgb.WHITE_HALF

            class Bank:
                Selected = Rgb.DARK_BLUE
                Available = Rgb.WHITE_HALF

        class Sends:
            On = Rgb.VIOLET
            Off = Rgb.WHITE_HALF

            class Bank:
                Available = Rgb.WHITE_HALF

    class Recording:
        Off = Rgb.WHITE_HALF

    class Transport:
        PlayOff = Rgb.WHITE_HALF
        PlayOn = Rgb.GREEN
        ContinueOff = Rgb.AQUA
        ContinueOn = Rgb.RED_HALF
        CaptureOff = Rgb.BLACK
        CaptureOn = Rgb.CREAM
        TapTempo = Rgb.CREAM

    class Quantization:
        Off = Rgb.RED_HALF
        On = Rgb.AQUA


skin = merge_skins(base_skin, Skin(Colors) * ())

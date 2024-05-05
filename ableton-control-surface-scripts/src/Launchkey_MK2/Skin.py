# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_MK2/Skin.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1507 bytes
from _Framework import Skin

from .Colors import Rgb


class Colors:
    class Session:
        SceneTriggered = Rgb.GREEN_BLINK
        NoScene = Rgb.BLACK
        ClipStarted = Rgb.GREEN_PULSE
        ClipRecording = Rgb.RED_PULSE
        ClipTriggeredPlay = Rgb.GREEN_BLINK
        ClipTriggeredRecord = Rgb.RED_BLINK
        ClipEmpty = Rgb.BLACK
        RecordButton = Rgb.RED_HALF
        StopClip = Rgb.GREEN
        StopClipTriggered = Rgb.GREEN_BLINK
        StoppedClip = Rgb.GREEN_HALF
        Enabled = Rgb.YELLOW

    class Mode:
        DeviceMode = Rgb.PURPLE_HALF
        DeviceModeOn = Rgb.PURPLE
        PanMode = Rgb.ORANGE_HALF
        PanModeOn = Rgb.ORANGE
        Send0Mode = Rgb.DARK_BLUE_HALF
        Send0ModeOn = Rgb.BRIGHT_PURPLE
        Send1Mode = Rgb.BLUE_HALF
        Send1ModeOn = Rgb.BLUE
        Send2Mode = Rgb.LIGHT_BLUE_HALF
        Send2ModeOn = Rgb.LIGHT_BLUE
        Send3Mode = Rgb.MINT_HALF
        Send3ModeOn = Rgb.MINT
        Send4Mode = Rgb.DARK_YELLOW_HALF
        Send4ModeOn = Rgb.DARK_YELLOW
        Send5Mode = Rgb.YELLOW_HALF
        Send5ModeOn = Rgb.YELLOW
        Disabled = Rgb.BLACK

    class Device:
        Bank = Rgb.DARK_PURPLE
        BestOfBank = Rgb.PURPLE_HALF
        BankSelected = Rgb.PURPLE


def make_skin():
    return Skin(Colors)

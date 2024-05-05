# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/BLOCKS/skin.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1316 bytes
from ableton.v2.control_surface import Skin

from .colors import Rgb


class Colors:
    class DefaultButton:
        On = Rgb.WHITE
        Off = Rgb.BLACK
        Disabled = Rgb.BLACK

    class Session:
        RecordButton = Rgb.RED
        ClipTriggeredPlay = Rgb.GREEN_BLINK
        ClipTriggeredRecord = Rgb.RED_BLINK
        ClipStarted = Rgb.GREEN_PULSE
        ClipRecording = Rgb.RED_PULSE
        ClipStopped = Rgb.AMBER
        Scene = Rgb.GREEN
        SceneTriggered = Rgb.GREEN_BLINK
        NoScene = Rgb.BLACK
        StopClipTriggered = Rgb.RED_PULSE
        StopClip = Rgb.RED
        StopClipDisabled = Rgb.BLACK
        ClipEmpty = Rgb.BLACK

    class DrumGroup:
        PadEmpty = Rgb.BLACK
        PadFilled = Rgb.YELLOW
        PadSelected = Rgb.LIGHT_BLUE
        PadSelectedNotSoloed = Rgb.LIGHT_BLUE
        PadMuted = Rgb.DARK_ORANGE
        PadMutedSelected = Rgb.LIGHT_BLUE
        PadSoloed = Rgb.DARK_BLUE
        PadSoloedSelected = Rgb.LIGHT_BLUE
        PadInvisible = Rgb.BLACK
        PadAction = Rgb.RED


skin = Skin(Colors)

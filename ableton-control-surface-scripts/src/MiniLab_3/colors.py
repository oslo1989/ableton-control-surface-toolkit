# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/MiniLab_3/colors.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 2339 bytes
from ableton.v3.control_surface import BasicColors
from ableton.v3.control_surface.elements import FallbackColor, RgbColor, create_rgb_color
from ableton.v3.live import liveobj_color_to_midi_rgb_values


class Rgb:
    OFF = FallbackColor(RgbColor(0, 0, 0), BasicColors.OFF)
    WHITE = FallbackColor(RgbColor(127, 127, 127), BasicColors.ON)
    WHITE_HALF = RgbColor(20, 20, 20)
    RED = RgbColor(127, 0, 0)
    RED_HALF = RgbColor(20, 0, 0)
    RED_LOW = RgbColor(8, 0, 0)
    GREEN = FallbackColor(RgbColor(0, 127, 0), BasicColors.ON)
    GREEN_HALF = FallbackColor(RgbColor(0, 20, 0), BasicColors.OFF)
    BLUE = RgbColor(0, 0, 127)
    OCEAN = RgbColor(20, 80, 127)
    AMBER = RgbColor(127, 50, 0)
    AMBER_HALF = RgbColor(20, 5, 0)
    YELLOW = RgbColor(127, 127, 0)
    YELLOW_HALF = RgbColor(20, 20, 0)


class Skin:
    class DefaultButton:
        On = Rgb.WHITE
        Off = Rgb.OFF
        Disabled = Rgb.OFF

    class DrumGroup:
        PadEmpty = Rgb.WHITE_HALF
        PadFilled = lambda x: create_rgb_color(liveobj_color_to_midi_rgb_values(x))
        PadSelected = Rgb.OCEAN
        PadMuted = Rgb.AMBER
        PadMutedSelected = Rgb.OCEAN
        PadSoloed = Rgb.BLUE
        PadSoloedSelected = Rgb.OCEAN
        PadPressed = Rgb.WHITE

    class Transport:
        PlayOn = Rgb.GREEN
        PlayOff = Rgb.GREEN_HALF
        StopOn = Rgb.WHITE
        StopOff = Rgb.WHITE_HALF
        LoopOn = Rgb.AMBER
        LoopOff = Rgb.AMBER_HALF
        TapTempoPressed = Rgb.WHITE
        TapTempo = Rgb.WHITE_HALF

    class Recording:
        ArrangementRecordOn = Rgb.RED
        ArrangementRecordOff = Rgb.RED_HALF
        SessionRecordOn = Rgb.RED
        SessionRecordTransition = Rgb.RED_HALF
        SessionRecordOff = Rgb.RED_HALF

    class Session:
        Slot = Rgb.OFF
        SlotRecordButton = Rgb.RED_LOW
        NoSlot = Rgb.OFF
        ClipStopped = lambda x: create_rgb_color(liveobj_color_to_midi_rgb_values(x))
        ClipTriggeredPlay = Rgb.GREEN_HALF
        ClipTriggeredRecord = Rgb.RED_HALF
        ClipPlaying = Rgb.GREEN
        ClipRecording = Rgb.RED
        StopClipTriggered = Rgb.RED_HALF
        StopClip = Rgb.RED
        StopClipDisabled = Rgb.OFF

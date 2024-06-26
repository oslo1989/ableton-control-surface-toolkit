# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/novation/skin.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 4043 bytes
from ableton.v2.control_surface import Skin

from .colors import Mono, Rgb


class Colors:
    class DefaultButton:
        On = Rgb.GREEN
        Off = Rgb.BLACK
        Disabled = Rgb.BLACK

    class Recording:
        On = Rgb.RED
        Off = Rgb.RED_HALF
        Transition = Rgb.RED_BLINK
        CaptureTriggered = Rgb.WHITE

    class FixedLength:
        On = Rgb.BLUE
        Off = Rgb.WHITE_HALF
        Held = Rgb.BLUE_PULSE
        Option = Rgb.BLACK
        OptionInRange = Rgb.BLUE_PULSE
        OptionHeld = Rgb.BLUE

    class Transport:
        PlayOff = Mono.OFF
        PlayOn = Mono.ON
        ContinueOff = Mono.OFF
        ContinueOn = Mono.HALF
        CaptureOff = Mono.OFF
        CaptureOn = Mono.HALF
        MetronomeOff = Rgb.RED_HALF
        MetronomeOn = Rgb.AQUA

    class Action:
        Undo = Rgb.CREAM
        UndoPressed = Rgb.WHITE
        Redo = Rgb.CREAM
        RedoPressed = Rgb.WHITE
        Delete = Rgb.WHITE_HALF
        DeletePressed = Rgb.WHITE
        Duplicate = Rgb.WHITE_HALF
        DuplicatePressed = Rgb.WHITE
        Quantize = Rgb.WHITE_HALF
        QuantizePressed = Rgb.WHITE
        Double = Rgb.CREAM
        DoublePressed = Rgb.WHITE

    class Session:
        RecordButton = Rgb.RED_HALF
        ClipTriggeredPlay = Rgb.GREEN_BLINK
        ClipTriggeredRecord = Rgb.RED_BLINK
        ClipStarted = Rgb.GREEN_PULSE
        ClipRecording = Rgb.RED_PULSE
        ClipEmpty = Rgb.BLACK
        Scene = Rgb.BLACK
        SceneTriggered = Rgb.GREEN_BLINK
        NoScene = Rgb.BLACK
        StopClipTriggered = Rgb.RED_BLINK
        StopClip = Rgb.RED
        StopClipDisabled = Rgb.RED_HALF
        Navigation = Rgb.WHITE_HALF
        NavigationPressed = Rgb.WHITE
        Select = Rgb.WHITE_HALF
        SelectPressed = Rgb.WHITE
        Delete = Rgb.WHITE_HALF
        DeletePressed = Rgb.WHITE
        Duplicate = Rgb.WHITE_HALF
        DuplicatePressed = Rgb.WHITE
        Quantize = Rgb.WHITE_HALF
        QuantizePressed = Rgb.WHITE
        Double = Rgb.CREAM
        DoublePressed = Rgb.WHITE
        ActionTriggered = Rgb.WHITE

    class Zooming:
        Selected = Rgb.OFF_WHITE
        Stopped = Rgb.LIGHT_BLUE_HALF
        Playing = Rgb.GREEN_PULSE
        Empty = Rgb.BLACK

    class Mixer:
        SoloOn = Rgb.BLUE
        SoloOff = Rgb.BLUE_HALF
        MuteOn = Rgb.YELLOW_HALF
        MuteOff = Rgb.YELLOW
        ArmOn = Rgb.RED
        ArmOff = Rgb.RED_HALF
        EmptyTrack = Rgb.BLACK
        TrackSelected = Rgb.WHITE
        TrackNotSelected = Rgb.WHITE_HALF

    class DrumGroup:
        PadEmpty = Rgb.BLACK
        PadFilled = Rgb.YELLOW
        PadSelected = Rgb.LIGHT_BLUE
        PadSelectedNotSoloed = Rgb.LIGHT_BLUE
        PadMuted = Rgb.DARK_ORANGE
        PadMutedSelected = Rgb.LIGHT_BLUE
        PadSoloed = Rgb.DARK_BLUE
        PadSoloedSelected = Rgb.LIGHT_BLUE
        PadAction = Rgb.WHITE
        Navigation = Rgb.YELLOW_HALF
        NavigationPressed = Rgb.YELLOW

    class Mode:
        class Volume:
            On = Rgb.GREEN
            Off = Rgb.WHITE_HALF

        class Pan:
            On = Rgb.ORANGE
            Off = Rgb.WHITE_HALF

        class SendA:
            On = Rgb.VIOLET
            Off = Rgb.WHITE_HALF

        class SendB:
            On = Rgb.DARK_BLUE
            Off = Rgb.WHITE_HALF

        class Stop:
            On = Rgb.RED
            Off = Rgb.WHITE_HALF

        class Mute:
            On = Rgb.YELLOW
            Off = Rgb.WHITE_HALF

        class Solo:
            On = Rgb.BLUE
            Off = Rgb.WHITE_HALF

        class Arm:
            On = Rgb.RED
            Off = Rgb.WHITE_HALF

        class Launch:
            On = Rgb.WHITE_HALF


skin = Skin(Colors)

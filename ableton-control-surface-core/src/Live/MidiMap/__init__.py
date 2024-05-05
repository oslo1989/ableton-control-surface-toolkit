from __future__ import annotations

from typing import Any, Callable, Optional

from Live import *
from Live.Application import *
from Live.Base import *
from Live.Browser import *
from Live.CcControlDevice import *
from Live.Chain import *
from Live.ChainMixerDevice import *
from Live.Clip import *
from Live.ClipSlot import *
from Live.CompressorDevice import *
from Live.Conversions import *
from Live.Device import *
from Live.DeviceIO import *
from Live.DeviceParameter import *
from Live.DriftDevice import *
from Live.DrumChain import *
from Live.DrumPad import *
from Live.Eq8Device import *
from Live.Groove import *
from Live.GroovePool import *
from Live.HybridReverbDevice import *
from Live.Listener import *
from Live.LomObject import *
from Live.MaxDevice import *
from Live.MeldDevice import *
from Live.MixerDevice import *
from Live.PluginDevice import *
from Live.RackDevice import *
from Live.RoarDevice import *
from Live.Sample import *
from Live.Scene import *
from Live.ShifterDevice import *
from Live.SimplerDevice import *
from Live.Song import *
from Live.SpectralResonatorDevice import *
from Live.Track import *
from Live.WavetableDevice import *


class CCFeedbackRule:
    """
    Structure to define feedback properties of MIDI mappings.
    """

    @property
    def cc_no(self) -> Any:
        pass

    @property
    def cc_value_map(self) -> Any:
        pass

    @property
    def channel(self) -> Any:
        pass

    @property
    def delay_in_ms(self) -> Any:
        pass

    @property
    def enabled(self) -> Any:
        pass


class MapMode:
    """
    Class that represent an enumeration of values for MapMode
    int([x]) -> integer
    int(x, base=10) -> integer

    Convert a number or string to an integer, or return 0 if no arguments
    are given.  If x is a number, return x.__int__().  For floating point
    numbers, this truncates towards zero.

    If x is not a number or if base is given, then x must be a string,
    bytes, or bytearray instance representing an integer literal in the
    given base.  The literal can be preceded by '+' or '-' and be surrounded
    by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
    Base 0 means to interpret the base from the string as an integer literal.
    >>> int('0b100', base=0)
    4
    """

    absolute = 0
    relative_signed_bit = 1
    relative_binary_offset = 2
    relative_two_compliment = 3
    relative_signed_bit2 = 4
    absolute_14_bit = 5
    relative_smooth_signed_bit = 6
    relative_smooth_binary_offset = 7
    relative_smooth_two_compliment = 8
    relative_smooth_signed_bit2 = 9


class NoteFeedbackRule:
    """
    Structure to define feedback properties of MIDI mappings.
    """

    @property
    def channel(self) -> Any:
        pass

    @property
    def delay_in_ms(self) -> Any:
        pass

    @property
    def enabled(self) -> Any:
        pass

    @property
    def note_no(self) -> Any:
        pass

    @property
    def vel_map(self) -> Any:
        pass


class PitchBendFeedbackRule:
    """
    Structure to define feedback properties of MIDI mappings.
    """

    @property
    def channel(self) -> Any:
        pass

    @property
    def delay_in_ms(self) -> Any:
        pass

    @property
    def enabled(self) -> Any:
        pass

    @property
    def value_pair_map(self) -> Any:
        pass


def forward_midi_cc(arg1: int, arg2: int, arg3: int, arg4: int, ShouldConsumeEvent: bool = True) -> bool:
    """
    forward_midi_cc( (int)arg1, (int)arg2, (int)arg3, (int)arg4 [, (bool)ShouldConsumeEvent=True]) -> bool :

        C++ signature :
            bool forward_midi_cc(unsigned int,unsigned int,int,int [,bool=True])
    """


def forward_midi_note(arg1: int, arg2: int, arg3: int, arg4: int, ShouldConsumeEvent: bool = True) -> bool:
    """
    forward_midi_note( (int)arg1, (int)arg2, (int)arg3, (int)arg4 [, (bool)ShouldConsumeEvent=True]) -> bool :

        C++ signature :
            bool forward_midi_note(unsigned int,unsigned int,int,int [,bool=True])
    """


def forward_midi_pitchbend(arg1: int, arg2: int, arg3: int) -> bool:
    """
    forward_midi_pitchbend( (int)arg1, (int)arg2, (int)arg3) -> bool :

        C++ signature :
            bool forward_midi_pitchbend(unsigned int,unsigned int,int)
    """


def map_midi_cc(
    midi_map_handle: int,
    parameter: object,
    midi_channel: int,
    controller_number: int,
    map_mode: object,
    avoid_takeover: bool,
    sensitivity: float | None = None,
) -> bool:
    """
    map_midi_cc( (int)midi_map_handle, (DeviceParameter)parameter, (int)midi_channel, (int)controller_number, (MapMode)map_mode, (bool)avoid_takeover [, (float)sensitivity=1.0]) -> bool :

        C++ signature :
            bool map_midi_cc(unsigned int,TPyHandle<ATimeableValue>,int,int,NRemoteMapperTypes::TControllerMapMode,bool [,float=1.0])
    """


def map_midi_cc_with_feedback_map(
    midi_map_handle: int,
    parameter: object,
    midi_channel: int,
    controller_number: int,
    map_mode: object,
    feedback_rule: object,
    avoid_takeover: bool,
    sensitivity: float | None = None,
) -> bool:
    """
    map_midi_cc_with_feedback_map( (int)midi_map_handle, (DeviceParameter)parameter, (int)midi_channel, (int)controller_number, (MapMode)map_mode, (CCFeedbackRule)feedback_rule, (bool)avoid_takeover [, (float)sensitivity=1.0]) -> bool :

        C++ signature :
            bool map_midi_cc_with_feedback_map(unsigned int,TPyHandle<ATimeableValue>,int,int,NRemoteMapperTypes::TControllerMapMode,NPythonMidiMap::TCCFeedbackRule,bool [,float=1.0])
    """


def map_midi_note(arg1: int, arg2: object, arg3: int, arg4: int) -> bool:
    """
    map_midi_note( (int)arg1, (DeviceParameter)arg2, (int)arg3, (int)arg4) -> bool :

        C++ signature :
            bool map_midi_note(unsigned int,TPyHandle<ATimeableValue>,int,int)
    """


def map_midi_note_with_feedback_map(arg1: int, arg2: object, arg3: int, arg4: int, arg5: object) -> bool:
    """
    map_midi_note_with_feedback_map( (int)arg1, (DeviceParameter)arg2, (int)arg3, (int)arg4, (NoteFeedbackRule)arg5) -> bool :

        C++ signature :
            bool map_midi_note_with_feedback_map(unsigned int,TPyHandle<ATimeableValue>,int,int,NPythonMidiMap::TNoteFeedbackRule)
    """


def map_midi_pitchbend(arg1: int, arg2: object, arg3: int, arg4: bool) -> bool:
    """
    map_midi_pitchbend( (int)arg1, (DeviceParameter)arg2, (int)arg3, (bool)arg4) -> bool :

        C++ signature :
            bool map_midi_pitchbend(unsigned int,TPyHandle<ATimeableValue>,int,bool)
    """


def map_midi_pitchbend_with_feedback_map(arg1: int, arg2: object, arg3: int, arg4: object, arg5: bool) -> bool:
    """
    map_midi_pitchbend_with_feedback_map( (int)arg1, (DeviceParameter)arg2, (int)arg3, (PitchBendFeedbackRule)arg4, (bool)arg5) -> bool :

        C++ signature :
            bool map_midi_pitchbend_with_feedback_map(unsigned int,TPyHandle<ATimeableValue>,int,NPythonMidiMap::TPitchBendFeedbackRule,bool)
    """


def send_feedback_for_parameter(arg1: int, arg2: object) -> None:
    """
    send_feedback_for_parameter( (int)arg1, (DeviceParameter)arg2) -> None :

        C++ signature :
            void send_feedback_for_parameter(unsigned int,TPyHandle<ATimeableValue>)
    """

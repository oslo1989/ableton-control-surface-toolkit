from __future__ import annotations

from typing import Any, Callable

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
from Live.MidiMap import *
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


class AudioToMidiType:
    """
    Class that represent an enumeration of values for AudioToMidiType
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

    harmony_to_midi = 0
    melody_to_midi = 1
    drums_to_midi = 2


def audio_to_midi_clip(audio_clip: object, audio_to_midi_type: int) -> None:
    """
    audio_to_midi_clip( (Song)song, (Clip)audio_clip, (int)audio_to_midi_type) -> None :
        Creates a MIDI clip in a new MIDI track with the notes extracted from the given
        audio_clip. The `audio_to_midi_type` decides which algorithm is used in
        the process. Raises error when called with an inconvertible clip or invalid
        `audio_to_midi_type`.

        C++ signature :
            void audio_to_midi_clip(TPyHandle<ASong>,TPyHandle<AClip>,int)
    """


def create_drum_rack_from_audio_clip(audio_clip: object) -> None:
    """
    create_drum_rack_from_audio_clip( (Song)song, (Clip)audio_clip) -> None :
        Creates a new track with a drum rack with a simpler on the first pad with
        the specified audio clip.

        C++ signature :
            void create_drum_rack_from_audio_clip(TPyHandle<ASong>,TPyHandle<AClip>)
    """


def create_midi_track_from_drum_pad(drum_pad: object) -> None:
    """
    create_midi_track_from_drum_pad( (Song)song, (DrumPad)drum_pad) -> None :
        Creates a new Midi track containing the specified Drum Pad's device chain.

        C++ signature :
            void create_midi_track_from_drum_pad(TPyHandle<ASong>,TPyHandle<ADrumGroupDevicePad>)
    """


def create_midi_track_with_simpler(audio_clip: object) -> None:
    """
    create_midi_track_with_simpler( (Song)song, (Clip)audio_clip) -> None :
        Creates a new Midi track with a simpler including the specified audio clip.

        C++ signature :
            void create_midi_track_with_simpler(TPyHandle<ASong>,TPyHandle<AClip>)
    """


def is_convertible_to_midi(audio_clip: object) -> bool:
    """
    is_convertible_to_midi( (Song)song, (Clip)audio_clip) -> bool :
        Returns whether `audio_clip` can be converted to MIDI.
        Raises error when called with a MIDI clip

        C++ signature :
            bool is_convertible_to_midi(TPyHandle<ASong>,TPyHandle<AClip>)
    """


def move_devices_on_track_to_new_drum_rack_pad(track_index: int) -> LomObject:
    """
    move_devices_on_track_to_new_drum_rack_pad( (Song)song, (int)track_index) -> LomObject :
        Moves the entire device chain of the track according to the track index
        onto the C1 (note 36) drum pad of a new drum rack in a new track.If the track associated with the track index does not contain any devices
        nothing changes (i.e. a new track and new drum rack are not created).

        C++ signature :
            TWeakPtr<TPyHandleBase> move_devices_on_track_to_new_drum_rack_pad(TPyHandle<ASong>,int)
    """


def sliced_simpler_to_drum_rack(simpler: object) -> None:
    """
    sliced_simpler_to_drum_rack( (Song)song, (SimplerDevice)simpler) -> None :
        Converts the Simpler into a Drum Rack, assigning each slice to a drum pad.
        Calling it on a non-sliced simpler raises an error.

        C++ signature :
            void sliced_simpler_to_drum_rack(TPyHandle<ASong>,TSimplerDevicePyHandle)
    """

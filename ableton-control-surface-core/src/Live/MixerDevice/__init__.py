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
from Live.Conversions import *
from Live.Device import *
from Live.DeviceIO import *
from Live.DeviceParameter import *
from Live.DriftDevice import *
from Live.DrumCellDevice import *
from Live.DrumChain import *
from Live.DrumPad import *
from Live.Envelope import *
from Live.Eq8Device import *
from Live.Groove import *
from Live.GroovePool import *
from Live.HybridReverbDevice import *
from Live.Licensing import *
from Live.Listener import *
from Live.LomObject import *
from Live.LooperDevice import *
from Live.MaxDevice import *
from Live.MeldDevice import *
from Live.MidiMap import *
from Live.PluginDevice import *
from Live.RackDevice import *
from Live.RoarDevice import *
from Live.Sample import *
from Live.Scene import *
from Live.ShifterDevice import *
from Live.SimplerDevice import *
from Live.Song import *
from Live.SpectralResonatorDevice import *
from Live.TakeLane import *
from Live.Track import *
from Live.TuningSystem import *
from Live.WavetableDevice import *


class MixerDevice:
    """
    This class represents a Mixer Device in Live, which gives you
    access to the Volume and Panning properties of a Track.
    """

    class crossfade_assignments:
        """
        Class that represent an enumeration of values for crossfade_assignments
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

        A = 0
        NONE = 1
        B = 2

    class panning_modes:
        """
        Class that represent an enumeration of values for panning_modes
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

        stereo = 0
        stereo_split = 1

    def add_crossfade_assign_listener(self, listener: Callable) -> None:
        """
        add_crossfade_assign_listener( (MixerDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "crossfade_assign" has changed.

            C++ signature :
                void add_crossfade_assign_listener(TPyHandle<ATrackDevice>,boost::python::api::object)
        """

    def add_panning_mode_listener(self, listener: Callable) -> None:
        """
        add_panning_mode_listener( (MixerDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "panning_mode" has changed.

            C++ signature :
                void add_panning_mode_listener(TPyHandle<ATrackDevice>,boost::python::api::object)
        """

    def add_sends_listener(self, listener: Callable) -> None:
        """
        add_sends_listener( (MixerDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "sends" has changed.

            C++ signature :
                void add_sends_listener(TPyHandle<ATrackDevice>,boost::python::api::object)
        """

    def crossfade_assign_has_listener(self, listener: Callable) -> bool:
        """
        crossfade_assign_has_listener( (MixerDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "crossfade_assign".

            C++ signature :
                bool crossfade_assign_has_listener(TPyHandle<ATrackDevice>,boost::python::api::object)
        """

    def panning_mode_has_listener(self, listener: Callable) -> bool:
        """
        panning_mode_has_listener( (MixerDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "panning_mode".

            C++ signature :
                bool panning_mode_has_listener(TPyHandle<ATrackDevice>,boost::python::api::object)
        """

    def remove_crossfade_assign_listener(self, listener: Callable) -> None:
        """
        remove_crossfade_assign_listener( (MixerDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "crossfade_assign".

            C++ signature :
                void remove_crossfade_assign_listener(TPyHandle<ATrackDevice>,boost::python::api::object)
        """

    def remove_panning_mode_listener(self, listener: Callable) -> None:
        """
        remove_panning_mode_listener( (MixerDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "panning_mode".

            C++ signature :
                void remove_panning_mode_listener(TPyHandle<ATrackDevice>,boost::python::api::object)
        """

    def remove_sends_listener(self, listener: Callable) -> None:
        """
        remove_sends_listener( (MixerDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "sends".

            C++ signature :
                void remove_sends_listener(TPyHandle<ATrackDevice>,boost::python::api::object)
        """

    def sends_has_listener(self, listener: Callable) -> bool:
        """
        sends_has_listener( (MixerDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "sends".

            C++ signature :
                bool sends_has_listener(TPyHandle<ATrackDevice>,boost::python::api::object)
        """

    @property
    def canonical_parent(self) -> Any:
        """
        Get the canonical parent of the mixer device.
        """

    @property
    def crossfade_assign(self) -> Any:
        """
        Player- and ReturnTracks only: Access to the Track's Crossfade Assign State.
        """

    @property
    def crossfader(self) -> Any:
        """
        MainTrack only: Const access to the Crossfader.
        """

    @property
    def cue_volume(self) -> Any:
        """
        MainTrack only: Const access to the Cue Volume Parameter.
        """

    @property
    def left_split_stereo(self) -> Any:
        """
        Const access to the Track's Left Split Stereo Panning Device Parameter.
        """

    @property
    def panning(self) -> Any:
        """
        Const access to the Tracks Panning Device Parameter.
        """

    @property
    def panning_mode(self) -> Any:
        """
        Access to the Track's Panning Mode.
        """

    @property
    def right_split_stereo(self) -> Any:
        """
        Const access to the Track's Right Split Stereo Panning Device Parameter.
        """

    @property
    def sends(self) -> Any:
        """
        Const access to the Tracks list of Send Amount Device Parameters.
        """

    @property
    def song_tempo(self) -> Any:
        """
        MainTrack only: Const access to the Song's Tempo.
        """

    @property
    def track_activator(self) -> Any:
        """
        Const access to the Tracks Activator Device Parameter.
        """

    @property
    def volume(self) -> Any:
        """
        Const access to the Tracks Volume Device Parameter.
        """

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
from Live.TuningSystem import *
from Live.WavetableDevice import *


class TakeLane:
    """
    This class represents a take lane in Live.
    """

    def add_arrangement_clips_listener(self, listener: Callable) -> None:
        """
        add_arrangement_clips_listener( (TakeLane)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "arrangement_clips" has changed.

            C++ signature :
                void add_arrangement_clips_listener(TPyHandle<ATakeLane>,boost::python::api::object)
        """

    def add_name_listener(self, listener: Callable) -> None:
        """
        add_name_listener( (TakeLane)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "name" has changed.

            C++ signature :
                void add_name_listener(TPyHandle<ATakeLane>,boost::python::api::object)
        """

    def arrangement_clips_has_listener(self, listener: Callable) -> bool:
        """
        arrangement_clips_has_listener( (TakeLane)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "arrangement_clips".

            C++ signature :
                bool arrangement_clips_has_listener(TPyHandle<ATakeLane>,boost::python::api::object)
        """

    def create_audio_clip(self, arg2: object, arg3: float) -> Clip:
        """
        create_audio_clip( (TakeLane)arg1, (object)arg2, (float)arg3) -> Clip :
            Creates an audio clip referencing the file at the given path and inserts it into the arrangement at the specified time.
            Throws an error when called on a non-audio or a frozen track, when the specified time is outside the [0., 1576800.] range, when the track is currently being recorded into, or when the path doesn't point to a valid audio file.

            C++ signature :
                TWeakPtr<TPyHandle<AClip>> create_audio_clip(TPyHandle<ATakeLane>,TString,double)
        """

    def create_midi_clip(self, arg2: float, arg3: float) -> Clip:
        """
        create_midi_clip( (TakeLane)arg1, (float)arg2, (float)arg3) -> Clip :
            Creates an empty MIDI clip and inserts it into the arrangement at the specified time.
            Throws an error when called on a non-MIDI track or a frozen track, when the specified time is outside the [0., 1576800.] range, or when the track is currently being recorded into.

            C++ signature :
                TWeakPtr<TPyHandle<AClip>> create_midi_clip(TPyHandle<ATakeLane>,double,double)
        """

    def name_has_listener(self, listener: Callable) -> bool:
        """
        name_has_listener( (TakeLane)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "name".

            C++ signature :
                bool name_has_listener(TPyHandle<ATakeLane>,boost::python::api::object)
        """

    def remove_arrangement_clips_listener(self, listener: Callable) -> None:
        """
        remove_arrangement_clips_listener( (TakeLane)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "arrangement_clips".

            C++ signature :
                void remove_arrangement_clips_listener(TPyHandle<ATakeLane>,boost::python::api::object)
        """

    def remove_name_listener(self, listener: Callable) -> None:
        """
        remove_name_listener( (TakeLane)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "name".

            C++ signature :
                void remove_name_listener(TPyHandle<ATakeLane>,boost::python::api::object)
        """

    @property
    def arrangement_clips(self) -> list[Clip]:
        """
        Read-only access to the arrangement clips in the take lane.
        """

    @property
    def canonical_parent(self) -> Any:
        """
        Get the canonical parent of the take lane.
        """

    @property
    def name(self) -> str:
        """
        Read/write access to the name of the TakeLane, as visible in the take lane header.
        """

    @name.setter
    def name(self, value: str) -> None:
        pass

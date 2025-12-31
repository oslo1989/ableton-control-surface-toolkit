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
from Live.TakeLane import *
from Live.Track import *
from Live.WavetableDevice import *


class PitchClassAndOctave:
    """
    This class represents a PitchClassAndOctave type.
    """

    @property
    def index_in_octave(self) -> Any:
        """
        A PitchClassAndOctave's index within the pseudo octave.
        """

    @property
    def octave(self) -> Any:
        """
        A PitchClassAndOctave's octave.
        """


class ReferencePitch:
    """
    This class represents a ReferencePitch type.
    """

    @property
    def frequency(self) -> Any:
        """
        A ReferencePitch's frequency in Hz.
        """

    @property
    def index_in_octave(self) -> Any:
        """
        A ReferencePitch's index within the pseudo octave.
        """

    @property
    def octave(self) -> Any:
        """
        A ReferencePitch's octave.
        """


class TuningSystem:
    """
    Represents a Tuning System and its properties.
    """

    def add_highest_note_listener(self, listener: Callable) -> None:
        """
        add_highest_note_listener( (TuningSystem)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "highest_note" has changed.

            C++ signature :
                void add_highest_note_listener(TPyHandle<ATuningSystem>,boost::python::api::object)
        """

    def add_lowest_note_listener(self, listener: Callable) -> None:
        """
        add_lowest_note_listener( (TuningSystem)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "lowest_note" has changed.

            C++ signature :
                void add_lowest_note_listener(TPyHandle<ATuningSystem>,boost::python::api::object)
        """

    def add_name_listener(self, listener: Callable) -> None:
        """
        add_name_listener( (TuningSystem)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "name" has changed.

            C++ signature :
                void add_name_listener(TPyHandle<ATuningSystem>,boost::python::api::object)
        """

    def add_note_tunings_listener(self, listener: Callable) -> None:
        """
        add_note_tunings_listener( (TuningSystem)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "note_tunings" has changed.

            C++ signature :
                void add_note_tunings_listener(TPyHandle<ATuningSystem>,boost::python::api::object)
        """

    def add_reference_pitch_listener(self, listener: Callable) -> None:
        """
        add_reference_pitch_listener( (TuningSystem)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "reference_pitch" has changed.

            C++ signature :
                void add_reference_pitch_listener(TPyHandle<ATuningSystem>,boost::python::api::object)
        """

    def highest_note_has_listener(self, listener: Callable) -> bool:
        """
        highest_note_has_listener( (TuningSystem)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "highest_note".

            C++ signature :
                bool highest_note_has_listener(TPyHandle<ATuningSystem>,boost::python::api::object)
        """

    def lowest_note_has_listener(self, listener: Callable) -> bool:
        """
        lowest_note_has_listener( (TuningSystem)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "lowest_note".

            C++ signature :
                bool lowest_note_has_listener(TPyHandle<ATuningSystem>,boost::python::api::object)
        """

    def name_has_listener(self, listener: Callable) -> bool:
        """
        name_has_listener( (TuningSystem)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "name".

            C++ signature :
                bool name_has_listener(TPyHandle<ATuningSystem>,boost::python::api::object)
        """

    def note_tunings_has_listener(self, listener: Callable) -> bool:
        """
        note_tunings_has_listener( (TuningSystem)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "note_tunings".

            C++ signature :
                bool note_tunings_has_listener(TPyHandle<ATuningSystem>,boost::python::api::object)
        """

    def reference_pitch_has_listener(self, listener: Callable) -> bool:
        """
        reference_pitch_has_listener( (TuningSystem)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "reference_pitch".

            C++ signature :
                bool reference_pitch_has_listener(TPyHandle<ATuningSystem>,boost::python::api::object)
        """

    def remove_highest_note_listener(self, listener: Callable) -> None:
        """
        remove_highest_note_listener( (TuningSystem)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "highest_note".

            C++ signature :
                void remove_highest_note_listener(TPyHandle<ATuningSystem>,boost::python::api::object)
        """

    def remove_lowest_note_listener(self, listener: Callable) -> None:
        """
        remove_lowest_note_listener( (TuningSystem)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "lowest_note".

            C++ signature :
                void remove_lowest_note_listener(TPyHandle<ATuningSystem>,boost::python::api::object)
        """

    def remove_name_listener(self, listener: Callable) -> None:
        """
        remove_name_listener( (TuningSystem)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "name".

            C++ signature :
                void remove_name_listener(TPyHandle<ATuningSystem>,boost::python::api::object)
        """

    def remove_note_tunings_listener(self, listener: Callable) -> None:
        """
        remove_note_tunings_listener( (TuningSystem)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "note_tunings".

            C++ signature :
                void remove_note_tunings_listener(TPyHandle<ATuningSystem>,boost::python::api::object)
        """

    def remove_reference_pitch_listener(self, listener: Callable) -> None:
        """
        remove_reference_pitch_listener( (TuningSystem)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "reference_pitch".

            C++ signature :
                void remove_reference_pitch_listener(TPyHandle<ATuningSystem>,boost::python::api::object)
        """

    @property
    def canonical_parent(self) -> Any:
        """
        Get the canonical parent of the TuningSystem.
        """

    @property
    def highest_note(self) -> Any:
        """
        Get/Set the highest note of the current tuning system, where the first entry is
        the index within the pseudo octave and the second entry is the octave.
        """

    @highest_note.setter
    def highest_note(self, value: Any) -> None:
        pass

    @property
    def lowest_note(self) -> Any:
        """
        Get/Set the lowest note of the current tuning system, where the first entry is
        the index within the pseudo octave and the second entry is the octave.
        """

    @lowest_note.setter
    def lowest_note(self, value: Any) -> None:
        pass

    @property
    def name(self) -> str:
        """
        Get/Set the name of the currently active tuning system.
        """

    @name.setter
    def name(self, value: str) -> None:
        pass

    @property
    def note_tunings(self) -> Any:
        """
        Get/Set the currently active tuning system's note tunings, specified in Cents, where 100 Cents is one semi-tone in equal temperament.
        """

    @note_tunings.setter
    def note_tunings(self, value: Any) -> None:
        pass

    @property
    def number_of_notes_in_pseudo_octave(self) -> Any:
        """
        Get the number of notes in the pseudo octave.
        """

    @property
    def pseudo_octave_in_cents(self) -> Any:
        """
        Get the pseudo octave in cents for the currently active tuning system.
        """

    @property
    def reference_pitch(self) -> Any:
        """
        Get/Set the reference pitch the currently active tuning system.
        """

    @reference_pitch.setter
    def reference_pitch(self, value: Any) -> None:
        pass

from __future__ import annotations

from typing import Any, Callable

from Live import *
from Live.Application import *
from Live.Base import *
from Live.Browser import *
from Live.CcControlDevice import *
from Live.Chain import *
from Live.ChainMixerDevice import *
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


class AutomationEnvelope:
    """
    Describes parameter automation per clip.
    """

    def insert_step(self, arg2: float, arg3: float, arg4: float) -> None:
        """
        insert_step( (AutomationEnvelope)arg1, (float)arg2, (float)arg3, (float)arg4) -> None :

            C++ signature :
                void insert_step(AAutomation {lvalue},double,double,double)
        """

    def value_at_time(self, arg2: float) -> float:
        """
        value_at_time( (AutomationEnvelope)arg1, (float)arg2) -> float :

            C++ signature :
                double value_at_time(AAutomation {lvalue},double)
        """


class Clip:
    """
    This class represents a Clip in Live. It can be either an Audio
    Clip or a MIDI Clip, in an Arrangement or the Session, depending
    on the Track (Slot) it lives in.
    """

    class View:
        """
        Representing the view aspects of a Clip.
        """

        def hide_envelope(self) -> None:
            """
            hide_envelope( (View)arg1) -> None :
                Hide the envelope view.

                C++ signature :
                    void hide_envelope(TPyViewData<AClip>)
            """

        def select_envelope_parameter(self, arg2: object) -> None:
            """
            select_envelope_parameter( (View)arg1, (DeviceParameter)arg2) -> None :
                Select the given device parameter in the envelope view.

                C++ signature :
                    void select_envelope_parameter(TPyViewData<AClip>,TPyHandle<ATimeableValue>)
            """

        def show_envelope(self) -> None:
            """
            show_envelope( (View)arg1) -> None :
                Show the envelope view.

                C++ signature :
                    void show_envelope(TPyViewData<AClip>)
            """

        def show_loop(self) -> None:
            """
            show_loop( (View)arg1) -> None :
                Show the entire loop in the detail view.

                C++ signature :
                    void show_loop(TPyViewData<AClip>)
            """

        @property
        def canonical_parent(self) -> Any:
            """
            Get the canonical parent of the clip view.
            """

        @property
        def grid_is_triplet(self) -> Any:
            """
            Get/set wether the grid is showing in triplet mode.
            """

        @grid_is_triplet.setter
        def grid_is_triplet(self, value: Any) -> None:
            pass

        @property
        def grid_quantization(self) -> Any:
            """
            Get/set clip grid quantization resolution.
            """

        @grid_quantization.setter
        def grid_quantization(self, value: Any) -> None:
            pass

    def add_color_index_listener(self, listener: Callable) -> None:
        """
        add_color_index_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "color_index" has changed.

            C++ signature :
                void add_color_index_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_color_listener(self, listener: Callable) -> None:
        """
        add_color_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "color" has changed.

            C++ signature :
                void add_color_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_end_marker_listener(self, listener: Callable) -> None:
        """
        add_end_marker_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "end_marker" has changed.

            C++ signature :
                void add_end_marker_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_end_time_listener(self, listener: Callable) -> None:
        """
        add_end_time_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "end_time" has changed.

            C++ signature :
                void add_end_time_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_file_path_listener(self, listener: Callable) -> None:
        """
        add_file_path_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "file_path" has changed.

            C++ signature :
                void add_file_path_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_gain_listener(self, listener: Callable) -> None:
        """
        add_gain_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "gain" has changed.

            C++ signature :
                void add_gain_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_groove_listener(self, listener: Callable) -> None:
        """
        add_groove_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "groove" has changed.

            C++ signature :
                void add_groove_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_has_envelopes_listener(self, listener: Callable) -> None:
        """
        add_has_envelopes_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "has_envelopes" has changed.

            C++ signature :
                void add_has_envelopes_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_is_overdubbing_listener(self, listener: Callable) -> None:
        """
        add_is_overdubbing_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "is_overdubbing" has changed.

            C++ signature :
                void add_is_overdubbing_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_is_recording_listener(self, listener: Callable) -> None:
        """
        add_is_recording_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "is_recording" has changed.

            C++ signature :
                void add_is_recording_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_launch_mode_listener(self, listener: Callable) -> None:
        """
        add_launch_mode_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "launch_mode" has changed.

            C++ signature :
                void add_launch_mode_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_launch_quantization_listener(self, listener: Callable) -> None:
        """
        add_launch_quantization_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "launch_quantization" has changed.

            C++ signature :
                void add_launch_quantization_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_legato_listener(self, listener: Callable) -> None:
        """
        add_legato_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "legato" has changed.

            C++ signature :
                void add_legato_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_loop_end_listener(self, listener: Callable) -> None:
        """
        add_loop_end_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "loop_end" has changed.

            C++ signature :
                void add_loop_end_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_loop_jump_listener(self, listener: Callable) -> None:
        """
        add_loop_jump_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "loop_jump" has changed.

            C++ signature :
                void add_loop_jump_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_loop_start_listener(self, listener: Callable) -> None:
        """
        add_loop_start_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "loop_start" has changed.

            C++ signature :
                void add_loop_start_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_looping_listener(self, listener: Callable) -> None:
        """
        add_looping_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "looping" has changed.

            C++ signature :
                void add_looping_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_muted_listener(self, listener: Callable) -> None:
        """
        add_muted_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "muted" has changed.

            C++ signature :
                void add_muted_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_name_listener(self, listener: Callable) -> None:
        """
        add_name_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "name" has changed.

            C++ signature :
                void add_name_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_new_notes(self, arg2: object) -> IntU64Vector:
        """
        add_new_notes( (Clip)arg1, (object)arg2) -> IntU64Vector :
            Expects a Python iterable holding a number of Live.Clip.MidiNoteSpecification
            objects. The objects will be used to construct new notes in the clip.

            C++ signature :
                std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long>> add_new_notes(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_notes_listener(self, listener: Callable) -> None:
        """
        add_notes_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "notes" has changed.

            C++ signature :
                void add_notes_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_pitch_coarse_listener(self, listener: Callable) -> None:
        """
        add_pitch_coarse_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "pitch_coarse" has changed.

            C++ signature :
                void add_pitch_coarse_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_pitch_fine_listener(self, listener: Callable) -> None:
        """
        add_pitch_fine_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "pitch_fine" has changed.

            C++ signature :
                void add_pitch_fine_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_playing_position_listener(self, listener: Callable) -> None:
        """
        add_playing_position_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "playing_position" has changed.

            C++ signature :
                void add_playing_position_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_playing_status_listener(self, listener: Callable) -> None:
        """
        add_playing_status_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "playing_status" has changed.

            C++ signature :
                void add_playing_status_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_position_listener(self, listener: Callable) -> None:
        """
        add_position_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "position" has changed.

            C++ signature :
                void add_position_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_ram_mode_listener(self, listener: Callable) -> None:
        """
        add_ram_mode_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "ram_mode" has changed.

            C++ signature :
                void add_ram_mode_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_signature_denominator_listener(self, listener: Callable) -> None:
        """
        add_signature_denominator_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "signature_denominator" has changed.

            C++ signature :
                void add_signature_denominator_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_signature_numerator_listener(self, listener: Callable) -> None:
        """
        add_signature_numerator_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "signature_numerator" has changed.

            C++ signature :
                void add_signature_numerator_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_start_marker_listener(self, listener: Callable) -> None:
        """
        add_start_marker_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "start_marker" has changed.

            C++ signature :
                void add_start_marker_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_velocity_amount_listener(self, listener: Callable) -> None:
        """
        add_velocity_amount_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "velocity_amount" has changed.

            C++ signature :
                void add_velocity_amount_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_warp_marker(self, warp_marker: object) -> None:
        """
        add_warp_marker( (Clip)self, (object)warp_marker) -> None :
            Available for AudioClips only.
            Adds the specified warp marker, if possible.

            C++ signature :
                void add_warp_marker(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_warp_markers_listener(self, listener: Callable) -> None:
        """
        add_warp_markers_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "warp_markers" has changed.

            C++ signature :
                void add_warp_markers_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_warp_mode_listener(self, listener: Callable) -> None:
        """
        add_warp_mode_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "warp_mode" has changed.

            C++ signature :
                void add_warp_mode_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def add_warping_listener(self, listener: Callable) -> None:
        """
        add_warping_listener( (Clip)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "warping" has changed.

            C++ signature :
                void add_warping_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def apply_note_modifications(self, arg2: object) -> None:
        """
        apply_note_modifications( (Clip)arg1, (MidiNoteVector)arg2) -> None :
            Expects a list of notes as returned from get_notes_extended. The content
            of the list will be used to modify existing notes in the clip, based on
            matching note IDs.
            This function should be used when modifying existing notes, e.g. changing the
            velocity or start time. The function ensures that per-note events attached to
            the modified notes are preserved. This is NOT the case when replacing notes
            via a combination of remove_notes_extended and add_new_notes.
            The given list can be a subset of the notes in the clip, but it must not
            contain any notes that are not present in the clip.


            C++ signature :
                void apply_note_modifications(TPyHandle<AClip>,std::__1::vector<NClipApi::TNoteInfo, std::__1::allocator<NClipApi::TNoteInfo>>)
        """

    def automation_envelope(self, arg2: object) -> AutomationEnvelope:
        """
        automation_envelope( (Clip)arg1, (DeviceParameter)arg2) -> AutomationEnvelope :
            Return the envelope for the given parameter.Returns None if the envelope doesn't exist.Returns None for Arrangement clips.Returns None for parameters from a different track.

            C++ signature :
                TWeakPtr<AAutomation> automation_envelope(TPyHandle<AClip>,TPyHandle<ATimeableValue>)
        """

    def beat_to_sample_time(self, beat_time: float) -> float:
        """
        beat_to_sample_time( (Clip)self, (float)beat_time) -> float :
            Available for AudioClips only.
            Converts the given beat time to sample time. Raises an error if the sample is not warped.

            C++ signature :
                double beat_to_sample_time(TPyHandle<AClip>,double)
        """

    def clear_all_envelopes(self) -> None:
        """
        clear_all_envelopes( (Clip)arg1) -> None :
            Clears all envelopes for this clip.

            C++ signature :
                void clear_all_envelopes(TPyHandle<AClip>)
        """

    def clear_envelope(self, arg2: object) -> None:
        """
        clear_envelope( (Clip)arg1, (DeviceParameter)arg2) -> None :
            Clears the envelope of this clips given parameter.

            C++ signature :
                void clear_envelope(TPyHandle<AClip>,TPyHandle<ATimeableValue>)
        """

    def color_has_listener(self, listener: Callable) -> bool:
        """
        color_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "color".

            C++ signature :
                bool color_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def color_index_has_listener(self, listener: Callable) -> bool:
        """
        color_index_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "color_index".

            C++ signature :
                bool color_index_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def create_automation_envelope(self, arg2: object) -> AutomationEnvelope:
        """
        create_automation_envelope( (Clip)arg1, (DeviceParameter)arg2) -> AutomationEnvelope :
            Creates an envelope for a given parameter and returns it.This should only be used if the envelope doesn't exist.Raises an error if the envelope can't be created.

            C++ signature :
                TWeakPtr<AAutomation> create_automation_envelope(TPyHandle<AClip>,TPyHandle<ATimeableValue>)
        """

    def crop(self) -> None:
        """
        crop( (Clip)arg1) -> None :
            Crops the clip. The region that is cropped depends on whether the clip is
            looped or not. If looped, the region outside of the loop is removed.
            If not looped, the region outside the start and end markers is removed.

            C++ signature :
                void crop(TPyHandle<AClip>)
        """

    def deselect_all_notes(self) -> None:
        """
        deselect_all_notes( (Clip)arg1) -> None :
            De-selects all notes present in the clip.

            C++ signature :
                void deselect_all_notes(TPyHandle<AClip>)
        """

    def duplicate_loop(self) -> None:
        """
        duplicate_loop( (Clip)arg1) -> None :
            Make the loop two times longer and duplicates notes and envelopes.
            Duplicates the clip start/end range if the clip is not looped.

            C++ signature :
                void duplicate_loop(TPyHandle<AClip>)
        """

    def duplicate_notes_by_id(
        self, note_ids: object, destination_time: object = None, transposition_amount: int = 0
    ) -> IntU64Vector:
        """
        duplicate_notes_by_id( (Clip)self, (object)note_ids [, (object)destination_time=None [, (int)transposition_amount=0]]) -> IntU64Vector :
            Duplicate all notes matching the given note IDs.
            If the optional destination_time is not provided, new notes will be inserted
            after the last selected note. This behavior can be observed when duplicating
            notes in the Live GUI.
            If the transposition_amount is specified, the notes in the region will be
            transposed by the number of semitones.
            Raises an error on audio clips.

            C++ signature :
                std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long>> duplicate_notes_by_id(TPyHandle<AClip>,boost::python::api::object [,boost::python::api::object=None [,int=0]])
        """

    def duplicate_region(
        self,
        region_start: float,
        region_length: float,
        destination_time: float,
        pitch: int = 0,
        transposition_amount: int = 0,
    ) -> None:
        """
        duplicate_region( (Clip)self, (float)region_start, (float)region_length, (float)destination_time [, (int)pitch=-1 [, (int)transposition_amount=0]]) -> None :
            Duplicate the notes in the specified region to the destination_time.
            Only notes of the specified pitch are duplicated or all if pitch is -1.
            If the transposition_amount is not 0, the notes in the region will
            be transposed by the transpose_amount of semitones.Raises an error on audio clips.

            C++ signature :
                void duplicate_region(TPyHandle<AClip>,double,double,double [,int=-1 [,int=0]])
        """

    def end_marker_has_listener(self, listener: Callable) -> bool:
        """
        end_marker_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "end_marker".

            C++ signature :
                bool end_marker_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def end_time_has_listener(self, listener: Callable) -> bool:
        """
        end_time_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "end_time".

            C++ signature :
                bool end_time_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def file_path_has_listener(self, listener: Callable) -> bool:
        """
        file_path_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "file_path".

            C++ signature :
                bool file_path_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def fire(self) -> None:
        """
        fire( (Clip)arg1) -> None :
            (Re)Start playing this Clip.

            C++ signature :
                void fire(TPyHandle<AClip>)
        """

    def gain_has_listener(self, listener: Callable) -> bool:
        """
        gain_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "gain".

            C++ signature :
                bool gain_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def get_all_notes_extended(self) -> MidiNoteVector:
        """
        get_all_notes_extended( (Clip)arg1) -> MidiNoteVector :
            Returns a list of all MIDI notes from the clip, regardless of their position
            relative to the start and end markers/loop start and loop end.
            Each note is represented by a Live.Clip.MidiNote object.
            The returned list can be modified freely, but modifications will not
            be reflected in the MIDI clip until apply_note_modifications is called.

            C++ signature :
                std::__1::vector<NClipApi::TNoteInfo, std::__1::allocator<NClipApi::TNoteInfo>> get_all_notes_extended(TPyHandle<AClip>)
        """

    def get_notes(self, from_time: float, from_pitch: int, time_span: float, pitch_span: int) -> tuple:
        """
        get_notes( (Clip)self, (float)from_time, (int)from_pitch, (float)time_span, (int)pitch_span) -> tuple :
            Returns a tuple of tuples where each inner tuple represents
            a note starting in the given pitch- and time range.
            The inner tuple contains pitch, time, duration, velocity, and mute state.

            C++ signature :
                boost::python::tuple get_notes(TPyHandle<AClip>,double,int,double,int)
        """

    def get_notes_by_id(self, note_ids: object) -> MidiNoteVector:
        """
        get_notes_by_id( (Clip)arg1, (object)note_ids) -> MidiNoteVector :
            Return a list of MIDI notes matching the given note IDs.


            C++ signature :
                std::__1::vector<NClipApi::TNoteInfo, std::__1::allocator<NClipApi::TNoteInfo>> get_notes_by_id(TPyHandle<AClip>,boost::python::api::object)
        """

    def get_notes_extended(
        self, from_pitch: int, pitch_span: int, from_time: float, time_span: float
    ) -> MidiNoteVector:
        """
        get_notes_extended( (Clip)arg1, (int)from_pitch, (int)pitch_span, (float)from_time, (float)time_span) -> MidiNoteVector :
            Returns a list of MIDI notes from the given pitch and time range.
            Each note is represented by a Live.Clip.MidiNote object.
            The returned list can be modified freely, but modifications will not
            be reflected in the MIDI clip until apply_note_modifications is called.

            C++ signature :
                std::__1::vector<NClipApi::TNoteInfo, std::__1::allocator<NClipApi::TNoteInfo>> get_notes_extended(TPyHandle<AClip>,int,int,double,double)
        """

    def get_selected_notes(self) -> tuple:
        """
        get_selected_notes( (Clip)arg1) -> tuple :
            Returns a tuple of tuples where each inner tuple
            represents a selected note. The inner tuple contains
            pitch, time, duration, velocity, and mute state.

            C++ signature :
                boost::python::tuple get_selected_notes(TPyHandle<AClip>)
        """

    def get_selected_notes_extended(self) -> MidiNoteVector:
        """
        get_selected_notes_extended( (Clip)arg1) -> MidiNoteVector :
            Returns a list of all MIDI notes from the clip that are currently selected.
            Each note is represented by a Live.Clip.MidiNote object.
            The returned list can be modified freely, but modifications will not
            be reflected in the MIDI clip until apply_note_modifications is called.

            C++ signature :
                std::__1::vector<NClipApi::TNoteInfo, std::__1::allocator<NClipApi::TNoteInfo>> get_selected_notes_extended(TPyHandle<AClip>)
        """

    def groove_has_listener(self, listener: Callable) -> bool:
        """
        groove_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "groove".

            C++ signature :
                bool groove_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def has_envelopes_has_listener(self, listener: Callable) -> bool:
        """
        has_envelopes_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "has_envelopes".

            C++ signature :
                bool has_envelopes_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def is_overdubbing_has_listener(self, listener: Callable) -> bool:
        """
        is_overdubbing_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "is_overdubbing".

            C++ signature :
                bool is_overdubbing_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def is_recording_has_listener(self, listener: Callable) -> bool:
        """
        is_recording_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "is_recording".

            C++ signature :
                bool is_recording_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def launch_mode_has_listener(self, listener: Callable) -> bool:
        """
        launch_mode_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "launch_mode".

            C++ signature :
                bool launch_mode_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def launch_quantization_has_listener(self, listener: Callable) -> bool:
        """
        launch_quantization_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "launch_quantization".

            C++ signature :
                bool launch_quantization_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def legato_has_listener(self, listener: Callable) -> bool:
        """
        legato_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "legato".

            C++ signature :
                bool legato_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def loop_end_has_listener(self, listener: Callable) -> bool:
        """
        loop_end_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "loop_end".

            C++ signature :
                bool loop_end_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def loop_jump_has_listener(self, listener: Callable) -> bool:
        """
        loop_jump_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "loop_jump".

            C++ signature :
                bool loop_jump_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def loop_start_has_listener(self, listener: Callable) -> bool:
        """
        loop_start_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "loop_start".

            C++ signature :
                bool loop_start_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def looping_has_listener(self, listener: Callable) -> bool:
        """
        looping_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "looping".

            C++ signature :
                bool looping_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def move_playing_pos(self, arg2: float) -> None:
        """
        move_playing_pos( (Clip)arg1, (float)arg2) -> None :
            Jump forward or backward by the specified relative amount in beats.
            Will do nothing, if the Clip is not playing.

            C++ signature :
                void move_playing_pos(TPyHandle<AClip>,double)
        """

    def move_warp_marker(self, marker_beat_time: float, beat_time_distance: float) -> None:
        """
        move_warp_marker( (Clip)self, (float)marker_beat_time, (float)beat_time_distance) -> None :
            Available for AudioClips only.
            Moves the specified warp marker by the specified beat time amount, if possible.

            C++ signature :
                void move_warp_marker(TPyHandle<AClip>,double,double)
        """

    def muted_has_listener(self, listener: Callable) -> bool:
        """
        muted_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "muted".

            C++ signature :
                bool muted_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def name_has_listener(self, listener: Callable) -> bool:
        """
        name_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "name".

            C++ signature :
                bool name_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def notes_has_listener(self, listener: Callable) -> bool:
        """
        notes_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "notes".

            C++ signature :
                bool notes_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def pitch_coarse_has_listener(self, listener: Callable) -> bool:
        """
        pitch_coarse_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "pitch_coarse".

            C++ signature :
                bool pitch_coarse_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def pitch_fine_has_listener(self, listener: Callable) -> bool:
        """
        pitch_fine_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "pitch_fine".

            C++ signature :
                bool pitch_fine_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def playing_position_has_listener(self, listener: Callable) -> bool:
        """
        playing_position_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "playing_position".

            C++ signature :
                bool playing_position_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def playing_status_has_listener(self, listener: Callable) -> bool:
        """
        playing_status_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "playing_status".

            C++ signature :
                bool playing_status_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def position_has_listener(self, listener: Callable) -> bool:
        """
        position_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "position".

            C++ signature :
                bool position_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def quantize(self, arg2: int, arg3: float) -> None:
        """
        quantize( (Clip)arg1, (int)arg2, (float)arg3) -> None :
            Quantize all notes in a clip or align warp markers.

            C++ signature :
                void quantize(TPyHandle<AClip>,int,float)
        """

    def quantize_pitch(self, arg2: int, arg3: int, arg4: float) -> None:
        """
        quantize_pitch( (Clip)arg1, (int)arg2, (int)arg3, (float)arg4) -> None :
            Quantize all the notes of a given pitch.  Raises an error on audio clips.

            C++ signature :
                void quantize_pitch(TPyHandle<AClip>,int,int,float)
        """

    def ram_mode_has_listener(self, listener: Callable) -> bool:
        """
        ram_mode_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "ram_mode".

            C++ signature :
                bool ram_mode_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_color_index_listener(self, listener: Callable) -> None:
        """
        remove_color_index_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "color_index".

            C++ signature :
                void remove_color_index_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_color_listener(self, listener: Callable) -> None:
        """
        remove_color_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "color".

            C++ signature :
                void remove_color_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_end_marker_listener(self, listener: Callable) -> None:
        """
        remove_end_marker_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "end_marker".

            C++ signature :
                void remove_end_marker_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_end_time_listener(self, listener: Callable) -> None:
        """
        remove_end_time_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "end_time".

            C++ signature :
                void remove_end_time_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_file_path_listener(self, listener: Callable) -> None:
        """
        remove_file_path_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "file_path".

            C++ signature :
                void remove_file_path_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_gain_listener(self, listener: Callable) -> None:
        """
        remove_gain_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "gain".

            C++ signature :
                void remove_gain_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_groove_listener(self, listener: Callable) -> None:
        """
        remove_groove_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "groove".

            C++ signature :
                void remove_groove_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_has_envelopes_listener(self, listener: Callable) -> None:
        """
        remove_has_envelopes_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "has_envelopes".

            C++ signature :
                void remove_has_envelopes_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_is_overdubbing_listener(self, listener: Callable) -> None:
        """
        remove_is_overdubbing_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "is_overdubbing".

            C++ signature :
                void remove_is_overdubbing_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_is_recording_listener(self, listener: Callable) -> None:
        """
        remove_is_recording_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "is_recording".

            C++ signature :
                void remove_is_recording_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_launch_mode_listener(self, listener: Callable) -> None:
        """
        remove_launch_mode_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "launch_mode".

            C++ signature :
                void remove_launch_mode_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_launch_quantization_listener(self, listener: Callable) -> None:
        """
        remove_launch_quantization_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "launch_quantization".

            C++ signature :
                void remove_launch_quantization_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_legato_listener(self, listener: Callable) -> None:
        """
        remove_legato_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "legato".

            C++ signature :
                void remove_legato_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_loop_end_listener(self, listener: Callable) -> None:
        """
        remove_loop_end_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "loop_end".

            C++ signature :
                void remove_loop_end_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_loop_jump_listener(self, listener: Callable) -> None:
        """
        remove_loop_jump_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "loop_jump".

            C++ signature :
                void remove_loop_jump_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_loop_start_listener(self, listener: Callable) -> None:
        """
        remove_loop_start_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "loop_start".

            C++ signature :
                void remove_loop_start_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_looping_listener(self, listener: Callable) -> None:
        """
        remove_looping_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "looping".

            C++ signature :
                void remove_looping_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_muted_listener(self, listener: Callable) -> None:
        """
        remove_muted_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "muted".

            C++ signature :
                void remove_muted_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_name_listener(self, listener: Callable) -> None:
        """
        remove_name_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "name".

            C++ signature :
                void remove_name_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_notes(self, arg2: float, arg3: int, arg4: float, arg5: int) -> None:
        """
        remove_notes( (Clip)arg1, (float)arg2, (int)arg3, (float)arg4, (int)arg5) -> None :
            Delete all notes starting in the given pitch- and time range.

            C++ signature :
                void remove_notes(TPyHandle<AClip>,double,int,double,int)
        """

    def remove_notes_by_id(self, arg2: object) -> None:
        """
        remove_notes_by_id( (Clip)arg1, (object)arg2) -> None :
            Delete all notes matching the given note IDs.
            This function should NOT be used to implement modification of existing notes
            (i.e. in combination with add_new_notes), as that leads to loss of per-note
            events. apply_note_modifications must be used instead for modifying existing
            notes.

            C++ signature :
                void remove_notes_by_id(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_notes_extended(self, from_pitch: int, pitch_span: int, from_time: float, time_span: float) -> None:
        """
        remove_notes_extended( (Clip)arg1, (int)from_pitch, (int)pitch_span, (float)from_time, (float)time_span) -> None :
            Delete all notes starting in the given pitch and time range.
            This function should NOT be used to implement modification of existing notes
            (i.e. in combination with add_new_notes), as that leads to loss of per-note
            events. apply_note_modifications must be used instead for modifying existing
            notes.

            C++ signature :
                void remove_notes_extended(TPyHandle<AClip>,int,int,double,double)
        """

    def remove_notes_listener(self, listener: Callable) -> None:
        """
        remove_notes_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "notes".

            C++ signature :
                void remove_notes_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_pitch_coarse_listener(self, listener: Callable) -> None:
        """
        remove_pitch_coarse_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "pitch_coarse".

            C++ signature :
                void remove_pitch_coarse_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_pitch_fine_listener(self, listener: Callable) -> None:
        """
        remove_pitch_fine_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "pitch_fine".

            C++ signature :
                void remove_pitch_fine_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_playing_position_listener(self, listener: Callable) -> None:
        """
        remove_playing_position_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "playing_position".

            C++ signature :
                void remove_playing_position_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_playing_status_listener(self, listener: Callable) -> None:
        """
        remove_playing_status_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "playing_status".

            C++ signature :
                void remove_playing_status_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_position_listener(self, listener: Callable) -> None:
        """
        remove_position_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "position".

            C++ signature :
                void remove_position_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_ram_mode_listener(self, listener: Callable) -> None:
        """
        remove_ram_mode_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "ram_mode".

            C++ signature :
                void remove_ram_mode_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_signature_denominator_listener(self, listener: Callable) -> None:
        """
        remove_signature_denominator_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "signature_denominator".

            C++ signature :
                void remove_signature_denominator_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_signature_numerator_listener(self, listener: Callable) -> None:
        """
        remove_signature_numerator_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "signature_numerator".

            C++ signature :
                void remove_signature_numerator_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_start_marker_listener(self, listener: Callable) -> None:
        """
        remove_start_marker_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "start_marker".

            C++ signature :
                void remove_start_marker_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_velocity_amount_listener(self, listener: Callable) -> None:
        """
        remove_velocity_amount_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "velocity_amount".

            C++ signature :
                void remove_velocity_amount_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_warp_marker(self, beat_time: float) -> None:
        """
        remove_warp_marker( (Clip)self, (float)beat_time) -> None :
            Available for AudioClips only.
            Removes the specified warp marker, if possible.

            C++ signature :
                void remove_warp_marker(TPyHandle<AClip>,double)
        """

    def remove_warp_markers_listener(self, listener: Callable) -> None:
        """
        remove_warp_markers_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "warp_markers".

            C++ signature :
                void remove_warp_markers_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_warp_mode_listener(self, listener: Callable) -> None:
        """
        remove_warp_mode_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "warp_mode".

            C++ signature :
                void remove_warp_mode_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def remove_warping_listener(self, listener: Callable) -> None:
        """
        remove_warping_listener( (Clip)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "warping".

            C++ signature :
                void remove_warping_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def replace_selected_notes(self, arg2: object) -> None:
        """
        replace_selected_notes( (Clip)arg1, (tuple)arg2) -> None :
            Called with a tuple of tuples where each inner tuple represents
            a note in the same format as returned by get_selected_notes. The
            notes described that way will then be used to replace the old selection.

            C++ signature :
                void replace_selected_notes(TPyHandle<AClip>,boost::python::tuple)
        """

    def sample_to_beat_time(self, sample_time: float) -> float:
        """
        sample_to_beat_time( (Clip)self, (float)sample_time) -> float :
            Available for AudioClips only.
            Converts the given sample time to beat time. Raises an error if the sample is not warped.

            C++ signature :
                double sample_to_beat_time(TPyHandle<AClip>,double)
        """

    def scrub(self, scrub_position: float) -> None:
        """
        scrub( (Clip)self, (float)scrub_position) -> None :
            Scrubs inside a clip.
            scrub_position defines the position in beats that the scrub will start from.
            The scrub will continue until stop_scrub is called.
            Global quantization applies to the scrub's position and length.

            C++ signature :
                void scrub(TPyHandle<AClip>,double)
        """

    def seconds_to_sample_time(self, seconds: float) -> float:
        """
        seconds_to_sample_time( (Clip)self, (float)seconds) -> float :
            Available for AudioClips only.
            Converts the given seconds to sample time. Raises an error if the sample is warped.

            C++ signature :
                double seconds_to_sample_time(TPyHandle<AClip>,double)
        """

    def select_all_notes(self) -> None:
        """
        select_all_notes( (Clip)arg1) -> None :
            Selects all notes present in the clip.

            C++ signature :
                void select_all_notes(TPyHandle<AClip>)
        """

    def select_notes_by_id(self, arg2: object) -> None:
        """
        select_notes_by_id( (Clip)arg1, (object)arg2) -> None :
            Selects all notes matching the given note IDs.

            C++ signature :
                void select_notes_by_id(TPyHandle<AClip>,boost::python::api::object)
        """

    def set_fire_button_state(self, arg2: bool) -> None:
        """
        set_fire_button_state( (Clip)arg1, (bool)arg2) -> None :
            Set the clip's fire button state directly. Supports all launch modes.

            C++ signature :
                void set_fire_button_state(TPyHandle<AClip>,bool)
        """

    def set_notes(self, arg2: object) -> None:
        """
        set_notes( (Clip)arg1, (tuple)arg2) -> None :
            Called with a tuple of tuples where each inner tuple represents
            a note in the same format as returned by get_notes. The
            notes described that way will then be added to the clip.

            C++ signature :
                void set_notes(TPyHandle<AClip>,boost::python::tuple)
        """

    def signature_denominator_has_listener(self, listener: Callable) -> bool:
        """
        signature_denominator_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "signature_denominator".

            C++ signature :
                bool signature_denominator_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def signature_numerator_has_listener(self, listener: Callable) -> bool:
        """
        signature_numerator_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "signature_numerator".

            C++ signature :
                bool signature_numerator_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def start_marker_has_listener(self, listener: Callable) -> bool:
        """
        start_marker_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "start_marker".

            C++ signature :
                bool start_marker_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def stop(self) -> None:
        """
        stop( (Clip)arg1) -> None :
            Stop playing this Clip.

            C++ signature :
                void stop(TPyHandle<AClip>)
        """

    def stop_scrub(self) -> None:
        """
        stop_scrub( (Clip)arg1) -> None :
            Stops the current scrub.

            C++ signature :
                void stop_scrub(TPyHandle<AClip>)
        """

    def velocity_amount_has_listener(self, listener: Callable) -> bool:
        """
        velocity_amount_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "velocity_amount".

            C++ signature :
                bool velocity_amount_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def warp_markers_has_listener(self, listener: Callable) -> bool:
        """
        warp_markers_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "warp_markers".

            C++ signature :
                bool warp_markers_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def warp_mode_has_listener(self, listener: Callable) -> bool:
        """
        warp_mode_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "warp_mode".

            C++ signature :
                bool warp_mode_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    def warping_has_listener(self, listener: Callable) -> bool:
        """
        warping_has_listener( (Clip)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "warping".

            C++ signature :
                bool warping_has_listener(TPyHandle<AClip>,boost::python::api::object)
        """

    @property
    def available_warp_modes(self) -> Any:
        """
        Available for AudioClips only.
        Get/Set the available warp modes, that can be used.
        """

    @available_warp_modes.setter
    def available_warp_modes(self, value: Any) -> None:
        pass

    @property
    def canonical_parent(self) -> Any:
        """
        Get the canonical parent of the Clip.
        """

    @property
    def color(self) -> Any:
        """
        Get/set access to the color of the Clip (RGB).
        """

    @color.setter
    def color(self, value: Any) -> None:
        pass

    @property
    def color_index(self) -> Any:
        """
        Get/set access to the color index of the Clip.
        """

    @color_index.setter
    def color_index(self, value: Any) -> None:
        pass

    @property
    def end_marker(self) -> Any:
        """
        Get/Set the Clips end marker pos in beats/seconds (unit depends on warping).
        """

    @end_marker.setter
    def end_marker(self, value: Any) -> None:
        pass

    @property
    def end_time(self) -> Any:
        """
        Get the clip's end time.
        """

    @property
    def file_path(self) -> Any:
        """
        Get the path of the file represented by the Audio Clip.
        """

    @property
    def gain(self) -> Any:
        """
        Available for AudioClips only.
        Read/write access to the gain setting of the
        Audio Clip
        """

    @gain.setter
    def gain(self, value: Any) -> None:
        pass

    @property
    def gain_display_string(self) -> Any:
        """
        Return a string with the gain as dB value
        """

    @property
    def groove(self) -> Any:
        """
        Get the groove associated with this clip.
        """

    @property
    def has_envelopes(self) -> bool:
        """
        Will notify if the clip gets his first envelope or the last envelope is removed.
        """

    @property
    def has_groove(self) -> bool:
        """
        Returns true if a groove is associated with this clip.
        """

    @property
    def is_arrangement_clip(self) -> bool:
        """
        return true if this Clip is an Arrangement Clip.
        A Clip can be either a Session or Arrangement Clip.
        """

    @property
    def is_audio_clip(self) -> bool:
        """
        Return true if this Clip is an Audio Clip.
        A Clip can be either an Audioclip or a MIDI Clip.
        """

    @property
    def is_midi_clip(self) -> bool:
        """
        return true if this Clip is a MIDI Clip.
        A Clip can be either an Audioclip or a MIDI Clip.
        """

    @property
    def is_overdubbing(self) -> bool:
        """
        returns true if the Clip is recording overdubs
        """

    @property
    def is_playing(self) -> bool:
        """
        Get/Set if this Clip is currently playing. If the Clips trigger mode
        is set to a quantization value, the Clip will not start playing immediately.
        If you need to know wether the Clip was triggered, use the is_triggered property.
        """

    @is_playing.setter
    def is_playing(self, value: bool) -> None:
        pass

    @property
    def is_recording(self) -> bool:
        """
        returns true if the Clip was triggered to record or is recording.
        """

    @property
    def is_triggered(self) -> bool:
        """
        returns true if the Clip was triggered or is playing.
        """

    @property
    def launch_mode(self) -> Any:
        """
        Get/Set access to the launch mode setting of the Clip.
        """

    @launch_mode.setter
    def launch_mode(self, value: Any) -> None:
        pass

    @property
    def launch_quantization(self) -> Any:
        """
        Get/Set access to the launch quantization setting of the Clip.
        """

    @launch_quantization.setter
    def launch_quantization(self, value: Any) -> None:
        pass

    @property
    def legato(self) -> Any:
        """
        Get/Set access to the legato setting of the Clip
        """

    @legato.setter
    def legato(self, value: Any) -> None:
        pass

    @property
    def length(self) -> Any:
        """
        Get to the Clips length in beats/seconds (unit depends on warping).
        """

    @property
    def loop_end(self) -> Any:
        """
        Get/Set the loop end pos of this Clip in beats/seconds (unit depends on warping).
        """

    @loop_end.setter
    def loop_end(self, value: Any) -> None:
        pass

    @property
    def loop_start(self) -> Any:
        """
        Get/Set the Clips loopstart pos in beats/seconds (unit depends on warping).
        """

    @loop_start.setter
    def loop_start(self, value: Any) -> None:
        pass

    @property
    def looping(self) -> Any:
        """
        Get/Set the Clips 'loop is enabled' flag
        .Only Warped Audio Clips or MIDI Clip can be looped.
        """

    @looping.setter
    def looping(self, value: Any) -> None:
        pass

    @property
    def muted(self) -> Any:
        """
        Read/write access to the mute state of the Clip.
        """

    @muted.setter
    def muted(self, value: Any) -> None:
        pass

    @property
    def name(self) -> str:
        """
        Read/write access to the name of the Clip.
        """

    @name.setter
    def name(self, value: str) -> None:
        pass

    @property
    def pitch_coarse(self) -> Any:
        """
        Available for AudioClips only.
        Read/write access to the pitch (in halftones) setting of the
        Audio Clip, ranging from -48 to 48
        """

    @pitch_coarse.setter
    def pitch_coarse(self, value: Any) -> None:
        pass

    @property
    def pitch_fine(self) -> Any:
        """
        Available for AudioClips only.
        Read/write access to the pitch fine setting of the
        Audio Clip, ranging from -500 to 500
        """

    @pitch_fine.setter
    def pitch_fine(self, value: Any) -> None:
        pass

    @property
    def playing_position(self) -> Any:
        """
        Constant access to the current playing position of the clip.
        The returned value is the position in beats for midi and warped audio clips,
        or in seconds for unwarped audio clips. Stopped clips will return 0.
        """

    @property
    def position(self) -> Any:
        """
        Get/Set the loop position of this Clip in beats/seconds (unit depends on warping).
        """

    @position.setter
    def position(self, value: Any) -> None:
        pass

    @property
    def ram_mode(self) -> Any:
        """
        Available for AudioClips only.
        Read/write access to the Ram mode setting of the Audio Clip
        """

    @ram_mode.setter
    def ram_mode(self, value: Any) -> None:
        pass

    @property
    def sample_length(self) -> Any:
        """
        Available for AudioClips only.
        Get the sample length in sample time or -1 if there is no sample available.
        """

    @property
    def sample_rate(self) -> Any:
        """
        Available for AudioClips only.
        Read-only access to the Clip's sampling rate.
        """

    @property
    def signature_denominator(self) -> Any:
        """
        Get/Set access to the global signature denominator of the Clip.
        """

    @signature_denominator.setter
    def signature_denominator(self, value: Any) -> None:
        pass

    @property
    def signature_numerator(self) -> Any:
        """
        Get/Set access to the global signature numerator of the Clip.
        """

    @signature_numerator.setter
    def signature_numerator(self, value: Any) -> None:
        pass

    @property
    def start_marker(self) -> Any:
        """
        Get/Set the Clips start marker pos in beats/seconds (unit depends on warping).
        """

    @start_marker.setter
    def start_marker(self, value: Any) -> None:
        pass

    @property
    def start_time(self) -> Any:
        """
        Get the clip's start time offset. For Session View clips, this is the time the clip was started. For Arrangement View clips, this is the offset within the arrangement.
        """

    @property
    def velocity_amount(self) -> Any:
        """
        Get/Set access to the velocity to volume amount of the Clip.
        """

    @velocity_amount.setter
    def velocity_amount(self, value: Any) -> None:
        pass

    @property
    def view(self) -> View:
        """
        Get the view of the Clip.
        """

    @property
    def warp_markers(self) -> Any:
        """
        Available for AudioClips only.
        Get the warp markers for this audio clip.
        """

    @property
    def warp_mode(self) -> Any:
        """
        Available for AudioClips only.
        Get/Set the warp mode for this audio clip.
        """

    @warp_mode.setter
    def warp_mode(self, value: Any) -> None:
        pass

    @property
    def warping(self) -> Any:
        """
        Available for AudioClips only.
        Get/Set if this Clip is timestreched.
        """

    @warping.setter
    def warping(self, value: Any) -> None:
        pass

    @property
    def will_record_on_start(self) -> Any:
        """
        returns true if the Clip will record on being started.
        """


class ClipLaunchQuantization:
    """
    Class that represent an enumeration of values for ClipLaunchQuantization
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

    q_global = 0
    q_none = 1
    q_8_bars = 2
    q_4_bars = 3
    q_2_bars = 4
    q_bar = 5
    q_half = 6
    q_half_triplet = 7
    q_quarter = 8
    q_quarter_triplet = 9
    q_eighth = 10
    q_eighth_triplet = 11
    q_sixteenth = 12
    q_sixteenth_triplet = 13
    q_thirtysecond = 14


class GridQuantization:
    """
    Class that represent an enumeration of values for GridQuantization
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

    no_grid = 0
    g_8_bars = 1
    g_4_bars = 2
    g_2_bars = 3
    g_bar = 4
    g_half = 5
    g_quarter = 6
    g_eighth = 7
    g_sixteenth = 8
    g_thirtysecond = 9
    count = 10


class LaunchMode:
    """
    Class that represent an enumeration of values for LaunchMode
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

    trigger = 0
    gate = 1
    toggle = 2
    repeat = 3


class MidiNote:
    """
    An object representing a MIDI Note
    """

    @property
    def duration(self) -> Any:
        pass

    @property
    def mute(self) -> Any:
        pass

    @property
    def note_id(self) -> Any:
        """
        A numerical ID that's unique within the originating clip of the note. Not to be
        used directly, but important for other API calls, namely apply_note_modifications.
        """

    @property
    def pitch(self) -> Any:
        pass

    @property
    def probability(self) -> Any:
        pass

    @property
    def release_velocity(self) -> Any:
        pass

    @property
    def start_time(self) -> Any:
        pass

    @property
    def velocity(self) -> Any:
        pass

    @property
    def velocity_deviation(self) -> Any:
        pass


class MidiNoteSpecification:
    """
    An object specifying the data for creating a MIDI note. To be used with the
    add_new_notes function.
    """


class MidiNoteVector:
    """
    A container for holding MIDI notes from Live.
    """

    def append(self, arg2: object) -> None:
        """
        append( (MidiNoteVector)arg1, (object)arg2) -> None :

            C++ signature :
                void append(std::__1::vector<NClipApi::TNoteInfo, std::__1::allocator<NClipApi::TNoteInfo>> {lvalue},boost::python::api::object)
        """

    def extend(self, arg2: object) -> None:
        """
        extend( (MidiNoteVector)arg1, (object)arg2) -> None :

            C++ signature :
                void extend(std::__1::vector<NClipApi::TNoteInfo, std::__1::allocator<NClipApi::TNoteInfo>> {lvalue},boost::python::api::object)
        """


class WarpMarker:
    """
    This class represents a WarpMarker type.
    """

    @property
    def beat_time(self) -> Any:
        """
        A WarpMarker's beat time.
        """

    @property
    def sample_time(self) -> Any:
        """
        A WarpMarker's sample time.
        """


class WarpMarkerVector:
    """
    A container for returning warp markers from Live.
    """

    def append(self, arg2: object) -> None:
        """
        append( (WarpMarkerVector)arg1, (object)arg2) -> None :

            C++ signature :
                void append(std::__1::vector<NApiHelpers::TWarpMarker, std::__1::allocator<NApiHelpers::TWarpMarker>> {lvalue},boost::python::api::object)
        """

    def extend(self, arg2: object) -> None:
        """
        extend( (WarpMarkerVector)arg1, (object)arg2) -> None :

            C++ signature :
                void extend(std::__1::vector<NApiHelpers::TWarpMarker, std::__1::allocator<NApiHelpers::TWarpMarker>> {lvalue},boost::python::api::object)
        """


class WarpMode:
    """
    Class that represent an enumeration of values for WarpMode
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

    beats = 0
    complex = 1
    complex_pro = 2
    repitch = 3
    rex = 4
    texture = 5
    tones = 6
    count = 7

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
from Live.MidiMap import *
from Live.MixerDevice import *
from Live.PluginDevice import *
from Live.RackDevice import *
from Live.RoarDevice import *
from Live.Sample import *
from Live.Scene import *
from Live.ShifterDevice import *
from Live.SimplerDevice import *
from Live.SpectralResonatorDevice import *
from Live.Track import *
from Live.WavetableDevice import *


class BeatTime:
    """
    Represents a Time, splitted into Bars, Beats, SubDivision and Ticks.
    """

    @property
    def bars(self) -> Any:
        pass

    @property
    def beats(self) -> Any:
        pass

    @property
    def sub_division(self) -> Any:
        pass

    @property
    def ticks(self) -> Any:
        pass


class CaptureDestination:
    """
    Class that represent an enumeration of values for CaptureDestination
    The destination for MIDI capture.
    """

    auto = 0
    session = 1
    arrangement = 2


class CaptureMode:
    """
    Class that represent an enumeration of values for CaptureMode
    The capture mode that is used for capture and insert scene.
    """

    all = 0
    all_except_selected = 1


class CuePoint:
    """
    Represents a 'Marker' in the arrangement.
    """

    def add_name_listener(self, listener: Callable) -> None:
        """
        add_name_listener( (CuePoint)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "name" has changed.

            C++ signature :
                void add_name_listener(TPyHandle<ACuePoint>,boost::python::api::object)
        """

    def add_time_listener(self, listener: Callable) -> None:
        """
        add_time_listener( (CuePoint)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "time" has changed.

            C++ signature :
                void add_time_listener(TPyHandle<ACuePoint>,boost::python::api::object)
        """

    def jump(self) -> None:
        """
        jump( (CuePoint)arg1) -> None :
            When the Song is playing, set the playing-position quantized to
            this Cuepoint's time. When not playing, simply move the start
            playing position.

            C++ signature :
                void jump(TPyHandle<ACuePoint>)
        """

    def name_has_listener(self, listener: Callable) -> bool:
        """
        name_has_listener( (CuePoint)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "name".

            C++ signature :
                bool name_has_listener(TPyHandle<ACuePoint>,boost::python::api::object)
        """

    def remove_name_listener(self, listener: Callable) -> None:
        """
        remove_name_listener( (CuePoint)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "name".

            C++ signature :
                void remove_name_listener(TPyHandle<ACuePoint>,boost::python::api::object)
        """

    def remove_time_listener(self, listener: Callable) -> None:
        """
        remove_time_listener( (CuePoint)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "time".

            C++ signature :
                void remove_time_listener(TPyHandle<ACuePoint>,boost::python::api::object)
        """

    def time_has_listener(self, listener: Callable) -> bool:
        """
        time_has_listener( (CuePoint)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "time".

            C++ signature :
                bool time_has_listener(TPyHandle<ACuePoint>,boost::python::api::object)
        """

    @property
    def canonical_parent(self) -> Any:
        """
        Get the canonical parent of the cue point.
        """

    @property
    def name(self) -> str:
        """
        Get/Listen to the name of this CuePoint, as visible in the arranger.
        """

    @property
    def time(self) -> Any:
        """
        Get/Listen to the CuePoint's time in beats.
        """


class Quantization:
    """
    Class that represent an enumeration of values for Quantization
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

    q_no_q = 0
    q_8_bars = 1
    q_4_bars = 2
    q_2_bars = 3
    q_bar = 4
    q_half = 5
    q_half_triplet = 6
    q_quarter = 7
    q_quarter_triplet = 8
    q_eight = 9
    q_eight_triplet = 10
    q_sixtenth = 11
    q_sixtenth_triplet = 12
    q_thirtytwoth = 13


class RecordingQuantization:
    """
    Class that represent an enumeration of values for RecordingQuantization
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

    rec_q_no_q = 0
    rec_q_quarter = 1
    rec_q_eight = 2
    rec_q_eight_triplet = 3
    rec_q_eight_eight_triplet = 4
    rec_q_sixtenth = 5
    rec_q_sixtenth_triplet = 6
    rec_q_sixtenth_sixtenth_triplet = 7
    rec_q_thirtysecond = 8


class SessionRecordStatus:
    """
    Class that represent an enumeration of values for SessionRecordStatus
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

    off = 0
    transition = 1
    on = 2


class SmptTime:
    """
    Represents a Time, split into Hours, Minutes, Seconds and Frames.
    The frame type must be specified when calling a function that returns
    a SmptTime.
    """

    @property
    def frames(self) -> Any:
        pass

    @property
    def hours(self) -> Any:
        pass

    @property
    def minutes(self) -> Any:
        pass

    @property
    def seconds(self) -> Any:
        pass


class Song:
    """
    This class represents a Live set.
    """

    class View:
        """
        Representing the view aspects of a Live document: The Session and Arrangerview.
        """

        def add_detail_clip_listener(self, listener: Callable) -> None:
            """
            add_detail_clip_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "detail_clip" has changed.

                C++ signature :
                    void add_detail_clip_listener(TPyViewData<ASong>,boost::python::api::object)
            """

        def add_draw_mode_listener(self, listener: Callable) -> None:
            """
            add_draw_mode_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "draw_mode" has changed.

                C++ signature :
                    void add_draw_mode_listener(TPyViewData<ASong>,boost::python::api::object)
            """

        def add_follow_song_listener(self, listener: Callable) -> None:
            """
            add_follow_song_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "follow_song" has changed.

                C++ signature :
                    void add_follow_song_listener(TPyViewData<ASong>,boost::python::api::object)
            """

        def add_selected_chain_listener(self, listener: Callable) -> None:
            """
            add_selected_chain_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "selected_chain" has changed.

                C++ signature :
                    void add_selected_chain_listener(TPyViewData<ASong>,boost::python::api::object)
            """

        def add_selected_parameter_listener(self, listener: Callable) -> None:
            """
            add_selected_parameter_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "selected_parameter" has changed.

                C++ signature :
                    void add_selected_parameter_listener(TPyViewData<ASong>,boost::python::api::object)
            """

        def add_selected_scene_listener(self, listener: Callable) -> None:
            """
            add_selected_scene_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "selected_scene" has changed.

                C++ signature :
                    void add_selected_scene_listener(TPyViewData<ASong>,boost::python::api::object)
            """

        def add_selected_track_listener(self, listener: Callable) -> None:
            """
            add_selected_track_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "selected_track" has changed.

                C++ signature :
                    void add_selected_track_listener(TPyViewData<ASong>,boost::python::api::object)
            """

        def detail_clip_has_listener(self, listener: Callable) -> bool:
            """
            detail_clip_has_listener( (View)arg1, (object)arg2) -> bool :
                Returns true, if the given listener function or method is connected
                to the property "detail_clip".

                C++ signature :
                    bool detail_clip_has_listener(TPyViewData<ASong>,boost::python::api::object)
            """

        def draw_mode_has_listener(self, listener: Callable) -> bool:
            """
            draw_mode_has_listener( (View)arg1, (object)arg2) -> bool :
                Returns true, if the given listener function or method is connected
                to the property "draw_mode".

                C++ signature :
                    bool draw_mode_has_listener(TPyViewData<ASong>,boost::python::api::object)
            """

        def follow_song_has_listener(self, listener: Callable) -> bool:
            """
            follow_song_has_listener( (View)arg1, (object)arg2) -> bool :
                Returns true, if the given listener function or method is connected
                to the property "follow_song".

                C++ signature :
                    bool follow_song_has_listener(TPyViewData<ASong>,boost::python::api::object)
            """

        def remove_detail_clip_listener(self, listener: Callable) -> None:
            """
            remove_detail_clip_listener( (View)arg1, (object)arg2) -> None :
                Remove a previously set listener function or method from
                property "detail_clip".

                C++ signature :
                    void remove_detail_clip_listener(TPyViewData<ASong>,boost::python::api::object)
            """

        def remove_draw_mode_listener(self, listener: Callable) -> None:
            """
            remove_draw_mode_listener( (View)arg1, (object)arg2) -> None :
                Remove a previously set listener function or method from
                property "draw_mode".

                C++ signature :
                    void remove_draw_mode_listener(TPyViewData<ASong>,boost::python::api::object)
            """

        def remove_follow_song_listener(self, listener: Callable) -> None:
            """
            remove_follow_song_listener( (View)arg1, (object)arg2) -> None :
                Remove a previously set listener function or method from
                property "follow_song".

                C++ signature :
                    void remove_follow_song_listener(TPyViewData<ASong>,boost::python::api::object)
            """

        def remove_selected_chain_listener(self, listener: Callable) -> None:
            """
            remove_selected_chain_listener( (View)arg1, (object)arg2) -> None :
                Remove a previously set listener function or method from
                property "selected_chain".

                C++ signature :
                    void remove_selected_chain_listener(TPyViewData<ASong>,boost::python::api::object)
            """

        def remove_selected_parameter_listener(self, listener: Callable) -> None:
            """
            remove_selected_parameter_listener( (View)arg1, (object)arg2) -> None :
                Remove a previously set listener function or method from
                property "selected_parameter".

                C++ signature :
                    void remove_selected_parameter_listener(TPyViewData<ASong>,boost::python::api::object)
            """

        def remove_selected_scene_listener(self, listener: Callable) -> None:
            """
            remove_selected_scene_listener( (View)arg1, (object)arg2) -> None :
                Remove a previously set listener function or method from
                property "selected_scene".

                C++ signature :
                    void remove_selected_scene_listener(TPyViewData<ASong>,boost::python::api::object)
            """

        def remove_selected_track_listener(self, listener: Callable) -> None:
            """
            remove_selected_track_listener( (View)arg1, (object)arg2) -> None :
                Remove a previously set listener function or method from
                property "selected_track".

                C++ signature :
                    void remove_selected_track_listener(TPyViewData<ASong>,boost::python::api::object)
            """

        def select_device(self, arg2: object, ShouldAppointDevice: bool = True) -> None:
            """
            select_device( (View)arg1, (Device)arg2 [, (bool)ShouldAppointDevice=True]) -> None :
                Select the given device.

                C++ signature :
                    void select_device(TPyViewData<ASong>,TPyHandle<ADevice> [,bool=True])
            """

        def selected_chain_has_listener(self, listener: Callable) -> bool:
            """
            selected_chain_has_listener( (View)arg1, (object)arg2) -> bool :
                Returns true, if the given listener function or method is connected
                to the property "selected_chain".

                C++ signature :
                    bool selected_chain_has_listener(TPyViewData<ASong>,boost::python::api::object)
            """

        def selected_parameter_has_listener(self, listener: Callable) -> bool:
            """
            selected_parameter_has_listener( (View)arg1, (object)arg2) -> bool :
                Returns true, if the given listener function or method is connected
                to the property "selected_parameter".

                C++ signature :
                    bool selected_parameter_has_listener(TPyViewData<ASong>,boost::python::api::object)
            """

        def selected_scene_has_listener(self, listener: Callable) -> bool:
            """
            selected_scene_has_listener( (View)arg1, (object)arg2) -> bool :
                Returns true, if the given listener function or method is connected
                to the property "selected_scene".

                C++ signature :
                    bool selected_scene_has_listener(TPyViewData<ASong>,boost::python::api::object)
            """

        def selected_track_has_listener(self, listener: Callable) -> bool:
            """
            selected_track_has_listener( (View)arg1, (object)arg2) -> bool :
                Returns true, if the given listener function or method is connected
                to the property "selected_track".

                C++ signature :
                    bool selected_track_has_listener(TPyViewData<ASong>,boost::python::api::object)
            """

        @property
        def canonical_parent(self) -> Any:
            """
            Get the canonical parent of the song view.
            """

        @property
        def detail_clip(self) -> Clip:
            """
            Get/Set the Clip that is currently visible in Lives Detailview.
            """

        @detail_clip.setter
        def detail_clip(self, value: Clip) -> None:
            pass

        @property
        def draw_mode(self) -> Any:
            """
            Get/Set if the Envelope/Note draw mode is enabled.
            """

        @draw_mode.setter
        def draw_mode(self, value: Any) -> None:
            pass

        @property
        def follow_song(self) -> Any:
            """
            Get/Set if the Arrangerview should scroll to show the playmarker.
            """

        @follow_song.setter
        def follow_song(self, value: Any) -> None:
            pass

        @property
        def highlighted_clip_slot(self) -> ClipSlot:
            """
            Get/Set the clip slot, defined via the selected track and scene in the Session.Will be None for Main- and Sendtracks.
            """

        @highlighted_clip_slot.setter
        def highlighted_clip_slot(self, value: ClipSlot) -> None:
            pass

        @property
        def selected_chain(self) -> Any:
            """
            Get the highlighted chain if available.
            """

        @property
        def selected_parameter(self) -> DeviceParameter:
            """
            Get the currently selected device parameter.
            """

        @property
        def selected_scene(self) -> Scene:
            """
            Get/Set the current selected scene in Lives Sessionview.
            """

        @selected_scene.setter
        def selected_scene(self, value: Scene) -> None:
            pass

        @property
        def selected_track(self) -> Track:
            """
            Get/Set the current selected Track in Lives Session or Arrangerview.
            """

        @selected_track.setter
        def selected_track(self, value: Track) -> None:
            pass

    def add_appointed_device_listener(self, listener: Callable) -> None:
        """
        add_appointed_device_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "appointed_device" has changed.

            C++ signature :
                void add_appointed_device_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_arrangement_overdub_listener(self, listener: Callable) -> None:
        """
        add_arrangement_overdub_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "arrangement_overdub" has changed.

            C++ signature :
                void add_arrangement_overdub_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_back_to_arranger_listener(self, listener: Callable) -> None:
        """
        add_back_to_arranger_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "back_to_arranger" has changed.

            C++ signature :
                void add_back_to_arranger_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_can_capture_midi_listener(self, listener: Callable) -> None:
        """
        add_can_capture_midi_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "can_capture_midi" has changed.

            C++ signature :
                void add_can_capture_midi_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_can_jump_to_next_cue_listener(self, listener: Callable) -> None:
        """
        add_can_jump_to_next_cue_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "can_jump_to_next_cue" has changed.

            C++ signature :
                void add_can_jump_to_next_cue_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_can_jump_to_prev_cue_listener(self, listener: Callable) -> None:
        """
        add_can_jump_to_prev_cue_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "can_jump_to_prev_cue" has changed.

            C++ signature :
                void add_can_jump_to_prev_cue_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_clip_trigger_quantization_listener(self, listener: Callable) -> None:
        """
        add_clip_trigger_quantization_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "clip_trigger_quantization" has changed.

            C++ signature :
                void add_clip_trigger_quantization_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_count_in_duration_listener(self, listener: Callable) -> None:
        """
        add_count_in_duration_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "count_in_duration" has changed.

            C++ signature :
                void add_count_in_duration_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_cue_points_listener(self, listener: Callable) -> None:
        """
        add_cue_points_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "cue_points" has changed.

            C++ signature :
                void add_cue_points_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_current_song_time_listener(self, listener: Callable) -> None:
        """
        add_current_song_time_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "current_song_time" has changed.

            C++ signature :
                void add_current_song_time_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_data_listener(self, listener: Callable) -> None:
        """
        add_data_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "data" has changed.

            C++ signature :
                void add_data_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_exclusive_arm_listener(self, listener: Callable) -> None:
        """
        add_exclusive_arm_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "exclusive_arm" has changed.

            C++ signature :
                void add_exclusive_arm_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_groove_amount_listener(self, listener: Callable) -> None:
        """
        add_groove_amount_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "groove_amount" has changed.

            C++ signature :
                void add_groove_amount_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_is_ableton_link_enabled_listener(self, listener: Callable) -> None:
        """
        add_is_ableton_link_enabled_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "is_ableton_link_enabled" has changed.

            C++ signature :
                void add_is_ableton_link_enabled_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_is_ableton_link_start_stop_sync_enabled_listener(self, listener: Callable) -> None:
        """
        add_is_ableton_link_start_stop_sync_enabled_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "is_ableton_link_start_stop_sync_enabled" has changed.

            C++ signature :
                void add_is_ableton_link_start_stop_sync_enabled_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_is_counting_in_listener(self, listener: Callable) -> None:
        """
        add_is_counting_in_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "is_counting_in" has changed.

            C++ signature :
                void add_is_counting_in_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_is_playing_listener(self, listener: Callable) -> None:
        """
        add_is_playing_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "is_playing" has changed.

            C++ signature :
                void add_is_playing_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_loop_length_listener(self, listener: Callable) -> None:
        """
        add_loop_length_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "loop_length" has changed.

            C++ signature :
                void add_loop_length_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_loop_listener(self, listener: Callable) -> None:
        """
        add_loop_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "loop" has changed.

            C++ signature :
                void add_loop_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_loop_start_listener(self, listener: Callable) -> None:
        """
        add_loop_start_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "loop_start" has changed.

            C++ signature :
                void add_loop_start_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_metronome_listener(self, listener: Callable) -> None:
        """
        add_metronome_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "metronome" has changed.

            C++ signature :
                void add_metronome_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_midi_recording_quantization_listener(self, listener: Callable) -> None:
        """
        add_midi_recording_quantization_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "midi_recording_quantization" has changed.

            C++ signature :
                void add_midi_recording_quantization_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_nudge_down_listener(self, listener: Callable) -> None:
        """
        add_nudge_down_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "nudge_down" has changed.

            C++ signature :
                void add_nudge_down_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_nudge_up_listener(self, listener: Callable) -> None:
        """
        add_nudge_up_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "nudge_up" has changed.

            C++ signature :
                void add_nudge_up_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_overdub_listener(self, listener: Callable) -> None:
        """
        add_overdub_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "overdub" has changed.

            C++ signature :
                void add_overdub_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_punch_in_listener(self, listener: Callable) -> None:
        """
        add_punch_in_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "punch_in" has changed.

            C++ signature :
                void add_punch_in_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_punch_out_listener(self, listener: Callable) -> None:
        """
        add_punch_out_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "punch_out" has changed.

            C++ signature :
                void add_punch_out_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_re_enable_automation_enabled_listener(self, listener: Callable) -> None:
        """
        add_re_enable_automation_enabled_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "re_enable_automation_enabled" has changed.

            C++ signature :
                void add_re_enable_automation_enabled_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_record_mode_listener(self, listener: Callable) -> None:
        """
        add_record_mode_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "record_mode" has changed.

            C++ signature :
                void add_record_mode_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_return_tracks_listener(self, listener: Callable) -> None:
        """
        add_return_tracks_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "return_tracks" has changed.

            C++ signature :
                void add_return_tracks_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_root_note_listener(self, listener: Callable) -> None:
        """
        add_root_note_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "root_note" has changed.

            C++ signature :
                void add_root_note_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_scale_intervals_listener(self, listener: Callable) -> None:
        """
        add_scale_intervals_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "scale_intervals" has changed.

            C++ signature :
                void add_scale_intervals_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_scale_name_listener(self, listener: Callable) -> None:
        """
        add_scale_name_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "scale_name" has changed.

            C++ signature :
                void add_scale_name_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_scenes_listener(self, listener: Callable) -> None:
        """
        add_scenes_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "scenes" has changed.

            C++ signature :
                void add_scenes_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_session_automation_record_listener(self, listener: Callable) -> None:
        """
        add_session_automation_record_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "session_automation_record" has changed.

            C++ signature :
                void add_session_automation_record_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_session_record_listener(self, listener: Callable) -> None:
        """
        add_session_record_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "session_record" has changed.

            C++ signature :
                void add_session_record_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_session_record_status_listener(self, listener: Callable) -> None:
        """
        add_session_record_status_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "session_record_status" has changed.

            C++ signature :
                void add_session_record_status_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_signature_denominator_listener(self, listener: Callable) -> None:
        """
        add_signature_denominator_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "signature_denominator" has changed.

            C++ signature :
                void add_signature_denominator_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_signature_numerator_listener(self, listener: Callable) -> None:
        """
        add_signature_numerator_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "signature_numerator" has changed.

            C++ signature :
                void add_signature_numerator_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_song_length_listener(self, listener: Callable) -> None:
        """
        add_song_length_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "song_length" has changed.

            C++ signature :
                void add_song_length_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_start_time_listener(self, listener: Callable) -> None:
        """
        add_start_time_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "start_time" has changed.

            C++ signature :
                void add_start_time_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_swing_amount_listener(self, listener: Callable) -> None:
        """
        add_swing_amount_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "swing_amount" has changed.

            C++ signature :
                void add_swing_amount_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_tempo_follower_enabled_listener(self, listener: Callable) -> None:
        """
        add_tempo_follower_enabled_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "tempo_follower_enabled" has changed.

            C++ signature :
                void add_tempo_follower_enabled_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_tempo_listener(self, listener: Callable) -> None:
        """
        add_tempo_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "tempo" has changed.

            C++ signature :
                void add_tempo_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_tracks_listener(self, listener: Callable) -> None:
        """
        add_tracks_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "tracks" has changed.

            C++ signature :
                void add_tracks_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_tuning_system_listener(self, listener: Callable) -> None:
        """
        add_tuning_system_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "tuning_system" has changed.

            C++ signature :
                void add_tuning_system_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def add_visible_tracks_listener(self, listener: Callable) -> None:
        """
        add_visible_tracks_listener( (Song)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "visible_tracks" has changed.

            C++ signature :
                void add_visible_tracks_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def appointed_device_has_listener(self, listener: Callable) -> bool:
        """
        appointed_device_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "appointed_device".

            C++ signature :
                bool appointed_device_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def arrangement_overdub_has_listener(self, listener: Callable) -> bool:
        """
        arrangement_overdub_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "arrangement_overdub".

            C++ signature :
                bool arrangement_overdub_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def back_to_arranger_has_listener(self, listener: Callable) -> bool:
        """
        back_to_arranger_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "back_to_arranger".

            C++ signature :
                bool back_to_arranger_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def begin_undo_step(self) -> None:
        """
        begin_undo_step( (Song)arg1) -> None :

            C++ signature :
                void begin_undo_step(TPyHandle<ASong>)
        """

    def can_capture_midi_has_listener(self, listener: Callable) -> bool:
        """
        can_capture_midi_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "can_capture_midi".

            C++ signature :
                bool can_capture_midi_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def can_jump_to_next_cue_has_listener(self, listener: Callable) -> bool:
        """
        can_jump_to_next_cue_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "can_jump_to_next_cue".

            C++ signature :
                bool can_jump_to_next_cue_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def can_jump_to_prev_cue_has_listener(self, listener: Callable) -> bool:
        """
        can_jump_to_prev_cue_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "can_jump_to_prev_cue".

            C++ signature :
                bool can_jump_to_prev_cue_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def capture_and_insert_scene(self, CaptureMode: int = 0) -> None:
        """
        capture_and_insert_scene( (Song)arg1 [, (int)CaptureMode=Song.CaptureMode.all]) -> None :
            Capture currently playing clips and insert them as a new scene after
            the selected scene. Raises a runtime error if creating a new scene would exceed the limitations.

            C++ signature :
                void capture_and_insert_scene(TPyHandle<ASong> [,int=Song.CaptureMode.all])
        """

    def capture_midi(self, Destination: int = 0) -> None:
        """
        capture_midi( (Song)arg1 [, (int)Destination=Song.CaptureDestination.auto]) -> None :
            Capture recently played MIDI material from audible tracks.
            If no Destination is given or Destination is set to CaptureDestination.auto, the captured material is inserted into the Session or Arrangement depending on which is visible.
            If Destination is set to CaptureDestination.session or CaptureDestination.arrangement, inserts the material into Session or Arrangement, respectively.
            Raises a limitation error when capturing into the Session and a new scene would have to be created but can't because it would exceed the limitations.

            C++ signature :
                void capture_midi(TPyHandle<ASong> [,int=Song.CaptureDestination.auto])
        """

    def clip_trigger_quantization_has_listener(self, listener: Callable) -> bool:
        """
        clip_trigger_quantization_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "clip_trigger_quantization".

            C++ signature :
                bool clip_trigger_quantization_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def continue_playing(self) -> None:
        """
        continue_playing( (Song)arg1) -> None :
            Continue playing the song from the current position

            C++ signature :
                void continue_playing(TPyHandle<ASong>)
        """

    def count_in_duration_has_listener(self, listener: Callable) -> bool:
        """
        count_in_duration_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "count_in_duration".

            C++ signature :
                bool count_in_duration_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def create_audio_track(self, Index: object = None) -> Track:
        """
        create_audio_track( (Song)arg1 [, (object)Index=None]) -> Track :
            Create a new audio track at the optional given index and return it.If the index is -1,
            the new track is added at the end. It will create a default audio track if possible.
            If the index is invalid or the new track would exceed the limitations, a limitation error is raised.If the index is missing, the track is created after the last selected item

            C++ signature :
                TWeakPtr<TTrackPyHandle> create_audio_track(TPyHandle<ASong> [,boost::python::api::object=None])
        """

    def create_midi_track(self, Index: object = None) -> Track:
        """
        create_midi_track( (Song)arg1 [, (object)Index=None]) -> Track :
            Create a new midi track at the optional given index and return it.If the index is -1,
             the new track is added at the end.It will create a default midi track if possible.
            If the index is invalid or the new track would exceed the limitations, a limitation error is raised.If the index is missing, the track is created after the last selected item

            C++ signature :
                TWeakPtr<TTrackPyHandle> create_midi_track(TPyHandle<ASong> [,boost::python::api::object=None])
        """

    def create_return_track(self) -> Track:
        """
        create_return_track( (Song)arg1) -> Track :
            Create a new return track at the end and return it. If the new track would exceed
            the limitations, a limitation error is raised.
            If the maximum number of return tracks is exceeded, a RuntimeError is raised.

            C++ signature :
                TWeakPtr<TTrackPyHandle> create_return_track(TPyHandle<ASong>)
        """

    def create_scene(self, arg2: int) -> Scene:
        """
        create_scene( (Song)arg1, (int)arg2) -> Scene :
            Create a new scene at the given index. If the index is -1,
            the new scene is added at the end. If the index is invalid or
            the new scene would exceed the limitations, a limitation error is raised.

            C++ signature :
                TWeakPtr<TPyHandle<AScene>> create_scene(TPyHandle<ASong>,int)
        """

    def cue_points_has_listener(self, listener: Callable) -> bool:
        """
        cue_points_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "cue_points".

            C++ signature :
                bool cue_points_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def current_song_time_has_listener(self, listener: Callable) -> bool:
        """
        current_song_time_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "current_song_time".

            C++ signature :
                bool current_song_time_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def data_has_listener(self, listener: Callable) -> bool:
        """
        data_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "data".

            C++ signature :
                bool data_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def delete_return_track(self, arg2: int) -> None:
        """
        delete_return_track( (Song)arg1, (int)arg2) -> None :
            Delete the return track with the given index. If no track with this index
            exists, an exception will be raised.

            C++ signature :
                void delete_return_track(TPyHandle<ASong>,int)
        """

    def delete_scene(self, arg2: int) -> None:
        """
        delete_scene( (Song)arg1, (int)arg2) -> None :
            Delete the scene with the given index. If no scene with this index
            exists, an exception will be raised.

            C++ signature :
                void delete_scene(TPyHandle<ASong>,int)
        """

    def delete_track(self, arg2: int) -> None:
        """
        delete_track( (Song)arg1, (int)arg2) -> None :
            Delete the track with the given index. If no track with this index
            exists, an exception will be raised.

            C++ signature :
                void delete_track(TPyHandle<ASong>,int)
        """

    def duplicate_scene(self, arg2: int) -> None:
        """
        duplicate_scene( (Song)arg1, (int)arg2) -> None :
            Duplicates a scene and selects the new one.
            Raises a limitation error if creating a new scene would exceed the limitations.

            C++ signature :
                void duplicate_scene(TPyHandle<ASong>,int)
        """

    def duplicate_track(self, arg2: int) -> None:
        """
        duplicate_track( (Song)arg1, (int)arg2) -> None :
            Duplicates a track and selects the new one.
            If the track is inside a folded group track, the group track is unfolded.
            Raises a limitation error if creating a new track would exceed the limitations.

            C++ signature :
                void duplicate_track(TPyHandle<ASong>,int)
        """

    def end_undo_step(self) -> None:
        """
        end_undo_step( (Song)arg1) -> None :

            C++ signature :
                void end_undo_step(TPyHandle<ASong>)
        """

    def exclusive_arm_has_listener(self, listener: Callable) -> bool:
        """
        exclusive_arm_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "exclusive_arm".

            C++ signature :
                bool exclusive_arm_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def find_device_position(self, device: object, target: object, target_position: int) -> int:
        """
        find_device_position( (Song)arg1, (Device)device, (LomObject)target, (int)target_position) -> int :
            Returns the closest possible position to the given target, where the
            device can be inserted. If inserting is not possible at all (i.e. if
            the device type is wrong), -1 is returned.

            C++ signature :
                int find_device_position(TPyHandle<ASong>,TPyHandle<ADevice>,TPyHandleBase,int)
        """

    def force_link_beat_time(self) -> None:
        """
        force_link_beat_time( (Song)arg1) -> None :
            Force the Link timeline to jump to Lives current beat time.
            Danger: This can cause beat time discontinuities in other connected apps.

            C++ signature :
                void force_link_beat_time(TPyHandle<ASong>)
        """

    def get_beats_loop_length(self) -> BeatTime:
        """
        get_beats_loop_length( (Song)arg1) -> BeatTime :
            Get const access to the songs loop length, using a
            BeatTime class with the current global set signature.

            C++ signature :
                NSongApi::TBeatTime get_beats_loop_length(TPyHandle<ASong>)
        """

    def get_beats_loop_start(self) -> BeatTime:
        """
        get_beats_loop_start( (Song)arg1) -> BeatTime :
            Get const access to the songs loop start, using a
            BeatTime class with the current global set signature.

            C++ signature :
                NSongApi::TBeatTime get_beats_loop_start(TPyHandle<ASong>)
        """

    def get_current_beats_song_time(self) -> BeatTime:
        """
        get_current_beats_song_time( (Song)arg1) -> BeatTime :
            Get const access to the songs current playing position, using a
            BeatTime class with the current global set signature.

            C++ signature :
                NSongApi::TBeatTime get_current_beats_song_time(TPyHandle<ASong>)
        """

    def get_current_smpte_song_time(self, arg2: int) -> SmptTime:
        """
        get_current_smpte_song_time( (Song)arg1, (int)arg2) -> SmptTime :
            Get const access to the songs current playing position, by specifying
            the SMPTE format in which you would like to receive the time.

            C++ signature :
                NSongApi::TSmptTime get_current_smpte_song_time(TPyHandle<ASong>,int)
        """

    def get_data(self, key: object, default_value: object) -> object:
        """
        get_data( (Song)arg1, (object)key, (object)default_value) -> object :
            Get data for the given key, that was previously stored using set_data.

            C++ signature :
                boost::python::api::object get_data(TPyHandle<ASong>,TString,boost::python::api::object)
        """

    def groove_amount_has_listener(self, listener: Callable) -> bool:
        """
        groove_amount_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "groove_amount".

            C++ signature :
                bool groove_amount_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def is_ableton_link_enabled_has_listener(self, listener: Callable) -> bool:
        """
        is_ableton_link_enabled_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "is_ableton_link_enabled".

            C++ signature :
                bool is_ableton_link_enabled_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def is_ableton_link_start_stop_sync_enabled_has_listener(self, listener: Callable) -> bool:
        """
        is_ableton_link_start_stop_sync_enabled_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "is_ableton_link_start_stop_sync_enabled".

            C++ signature :
                bool is_ableton_link_start_stop_sync_enabled_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def is_counting_in_has_listener(self, listener: Callable) -> bool:
        """
        is_counting_in_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "is_counting_in".

            C++ signature :
                bool is_counting_in_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def is_cue_point_selected(self) -> bool:
        """
        is_cue_point_selected( (Song)arg1) -> bool :
            Return true if the global playing pos is currently on a cue point.

            C++ signature :
                bool is_cue_point_selected(TPyHandle<ASong>)
        """

    def is_playing_has_listener(self, listener: Callable) -> bool:
        """
        is_playing_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "is_playing".

            C++ signature :
                bool is_playing_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def jump_by(self, arg2: float) -> None:
        """
        jump_by( (Song)arg1, (float)arg2) -> None :
            Set a new playing pos, relative to the current one.

            C++ signature :
                void jump_by(TPyHandle<ASong>,double)
        """

    def jump_to_next_cue(self) -> None:
        """
        jump_to_next_cue( (Song)arg1) -> None :
            Jump to the next cue (marker) if possible.

            C++ signature :
                void jump_to_next_cue(TPyHandle<ASong>)
        """

    def jump_to_prev_cue(self) -> None:
        """
        jump_to_prev_cue( (Song)arg1) -> None :
            Jump to the prior cue (marker) if possible.

            C++ signature :
                void jump_to_prev_cue(TPyHandle<ASong>)
        """

    def loop_has_listener(self, listener: Callable) -> bool:
        """
        loop_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "loop".

            C++ signature :
                bool loop_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def loop_length_has_listener(self, listener: Callable) -> bool:
        """
        loop_length_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "loop_length".

            C++ signature :
                bool loop_length_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def loop_start_has_listener(self, listener: Callable) -> bool:
        """
        loop_start_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "loop_start".

            C++ signature :
                bool loop_start_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def metronome_has_listener(self, listener: Callable) -> bool:
        """
        metronome_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "metronome".

            C++ signature :
                bool metronome_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def midi_recording_quantization_has_listener(self, listener: Callable) -> bool:
        """
        midi_recording_quantization_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "midi_recording_quantization".

            C++ signature :
                bool midi_recording_quantization_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def move_device(self, device: object, target: object, target_position: int) -> int:
        """
        move_device( (Song)arg1, (Device)device, (LomObject)target, (int)target_position) -> int :
            Move a device into the target at the given position, where 0 moves it before the first device and len(devices) moves it to the end of the device chain.If the device cannot be moved to this position, the nearest possible position is chosen. If the device type is not valid, a runtime error is raised.Returns the index, where the device was moved to.

            C++ signature :
                int move_device(TPyHandle<ASong>,TPyHandle<ADevice>,TPyHandleBase,int)
        """

    def nudge_down_has_listener(self, listener: Callable) -> bool:
        """
        nudge_down_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "nudge_down".

            C++ signature :
                bool nudge_down_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def nudge_up_has_listener(self, listener: Callable) -> bool:
        """
        nudge_up_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "nudge_up".

            C++ signature :
                bool nudge_up_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def overdub_has_listener(self, listener: Callable) -> bool:
        """
        overdub_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "overdub".

            C++ signature :
                bool overdub_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def play_selection(self) -> None:
        """
        play_selection( (Song)arg1) -> None :
            Start playing the current set selection, or do nothing if
            no selection is set.

            C++ signature :
                void play_selection(TPyHandle<ASong>)
        """

    def punch_in_has_listener(self, listener: Callable) -> bool:
        """
        punch_in_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "punch_in".

            C++ signature :
                bool punch_in_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def punch_out_has_listener(self, listener: Callable) -> bool:
        """
        punch_out_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "punch_out".

            C++ signature :
                bool punch_out_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def re_enable_automation(self) -> None:
        """
        re_enable_automation( (Song)arg1) -> None :
            Discards overrides of automated parameters.

            C++ signature :
                void re_enable_automation(TPyHandle<ASong>)
        """

    def re_enable_automation_enabled_has_listener(self, listener: Callable) -> bool:
        """
        re_enable_automation_enabled_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "re_enable_automation_enabled".

            C++ signature :
                bool re_enable_automation_enabled_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def record_mode_has_listener(self, listener: Callable) -> bool:
        """
        record_mode_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "record_mode".

            C++ signature :
                bool record_mode_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def redo(self) -> str:
        """
        redo( (Song)arg1) -> str :
            Redo the last action that was undone.

            C++ signature :
                TString redo(TPyHandle<ASong>)
        """

    def remove_appointed_device_listener(self, listener: Callable) -> None:
        """
        remove_appointed_device_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "appointed_device".

            C++ signature :
                void remove_appointed_device_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_arrangement_overdub_listener(self, listener: Callable) -> None:
        """
        remove_arrangement_overdub_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "arrangement_overdub".

            C++ signature :
                void remove_arrangement_overdub_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_back_to_arranger_listener(self, listener: Callable) -> None:
        """
        remove_back_to_arranger_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "back_to_arranger".

            C++ signature :
                void remove_back_to_arranger_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_can_capture_midi_listener(self, listener: Callable) -> None:
        """
        remove_can_capture_midi_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "can_capture_midi".

            C++ signature :
                void remove_can_capture_midi_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_can_jump_to_next_cue_listener(self, listener: Callable) -> None:
        """
        remove_can_jump_to_next_cue_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "can_jump_to_next_cue".

            C++ signature :
                void remove_can_jump_to_next_cue_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_can_jump_to_prev_cue_listener(self, listener: Callable) -> None:
        """
        remove_can_jump_to_prev_cue_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "can_jump_to_prev_cue".

            C++ signature :
                void remove_can_jump_to_prev_cue_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_clip_trigger_quantization_listener(self, listener: Callable) -> None:
        """
        remove_clip_trigger_quantization_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "clip_trigger_quantization".

            C++ signature :
                void remove_clip_trigger_quantization_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_count_in_duration_listener(self, listener: Callable) -> None:
        """
        remove_count_in_duration_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "count_in_duration".

            C++ signature :
                void remove_count_in_duration_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_cue_points_listener(self, listener: Callable) -> None:
        """
        remove_cue_points_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "cue_points".

            C++ signature :
                void remove_cue_points_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_current_song_time_listener(self, listener: Callable) -> None:
        """
        remove_current_song_time_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "current_song_time".

            C++ signature :
                void remove_current_song_time_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_data_listener(self, listener: Callable) -> None:
        """
        remove_data_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "data".

            C++ signature :
                void remove_data_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_exclusive_arm_listener(self, listener: Callable) -> None:
        """
        remove_exclusive_arm_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "exclusive_arm".

            C++ signature :
                void remove_exclusive_arm_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_groove_amount_listener(self, listener: Callable) -> None:
        """
        remove_groove_amount_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "groove_amount".

            C++ signature :
                void remove_groove_amount_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_is_ableton_link_enabled_listener(self, listener: Callable) -> None:
        """
        remove_is_ableton_link_enabled_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "is_ableton_link_enabled".

            C++ signature :
                void remove_is_ableton_link_enabled_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_is_ableton_link_start_stop_sync_enabled_listener(self, listener: Callable) -> None:
        """
        remove_is_ableton_link_start_stop_sync_enabled_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "is_ableton_link_start_stop_sync_enabled".

            C++ signature :
                void remove_is_ableton_link_start_stop_sync_enabled_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_is_counting_in_listener(self, listener: Callable) -> None:
        """
        remove_is_counting_in_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "is_counting_in".

            C++ signature :
                void remove_is_counting_in_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_is_playing_listener(self, listener: Callable) -> None:
        """
        remove_is_playing_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "is_playing".

            C++ signature :
                void remove_is_playing_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_loop_length_listener(self, listener: Callable) -> None:
        """
        remove_loop_length_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "loop_length".

            C++ signature :
                void remove_loop_length_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_loop_listener(self, listener: Callable) -> None:
        """
        remove_loop_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "loop".

            C++ signature :
                void remove_loop_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_loop_start_listener(self, listener: Callable) -> None:
        """
        remove_loop_start_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "loop_start".

            C++ signature :
                void remove_loop_start_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_metronome_listener(self, listener: Callable) -> None:
        """
        remove_metronome_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "metronome".

            C++ signature :
                void remove_metronome_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_midi_recording_quantization_listener(self, listener: Callable) -> None:
        """
        remove_midi_recording_quantization_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "midi_recording_quantization".

            C++ signature :
                void remove_midi_recording_quantization_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_nudge_down_listener(self, listener: Callable) -> None:
        """
        remove_nudge_down_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "nudge_down".

            C++ signature :
                void remove_nudge_down_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_nudge_up_listener(self, listener: Callable) -> None:
        """
        remove_nudge_up_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "nudge_up".

            C++ signature :
                void remove_nudge_up_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_overdub_listener(self, listener: Callable) -> None:
        """
        remove_overdub_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "overdub".

            C++ signature :
                void remove_overdub_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_punch_in_listener(self, listener: Callable) -> None:
        """
        remove_punch_in_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "punch_in".

            C++ signature :
                void remove_punch_in_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_punch_out_listener(self, listener: Callable) -> None:
        """
        remove_punch_out_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "punch_out".

            C++ signature :
                void remove_punch_out_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_re_enable_automation_enabled_listener(self, listener: Callable) -> None:
        """
        remove_re_enable_automation_enabled_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "re_enable_automation_enabled".

            C++ signature :
                void remove_re_enable_automation_enabled_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_record_mode_listener(self, listener: Callable) -> None:
        """
        remove_record_mode_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "record_mode".

            C++ signature :
                void remove_record_mode_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_return_tracks_listener(self, listener: Callable) -> None:
        """
        remove_return_tracks_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "return_tracks".

            C++ signature :
                void remove_return_tracks_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_root_note_listener(self, listener: Callable) -> None:
        """
        remove_root_note_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "root_note".

            C++ signature :
                void remove_root_note_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_scale_intervals_listener(self, listener: Callable) -> None:
        """
        remove_scale_intervals_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "scale_intervals".

            C++ signature :
                void remove_scale_intervals_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_scale_name_listener(self, listener: Callable) -> None:
        """
        remove_scale_name_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "scale_name".

            C++ signature :
                void remove_scale_name_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_scenes_listener(self, listener: Callable) -> None:
        """
        remove_scenes_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "scenes".

            C++ signature :
                void remove_scenes_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_session_automation_record_listener(self, listener: Callable) -> None:
        """
        remove_session_automation_record_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "session_automation_record".

            C++ signature :
                void remove_session_automation_record_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_session_record_listener(self, listener: Callable) -> None:
        """
        remove_session_record_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "session_record".

            C++ signature :
                void remove_session_record_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_session_record_status_listener(self, listener: Callable) -> None:
        """
        remove_session_record_status_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "session_record_status".

            C++ signature :
                void remove_session_record_status_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_signature_denominator_listener(self, listener: Callable) -> None:
        """
        remove_signature_denominator_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "signature_denominator".

            C++ signature :
                void remove_signature_denominator_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_signature_numerator_listener(self, listener: Callable) -> None:
        """
        remove_signature_numerator_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "signature_numerator".

            C++ signature :
                void remove_signature_numerator_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_song_length_listener(self, listener: Callable) -> None:
        """
        remove_song_length_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "song_length".

            C++ signature :
                void remove_song_length_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_start_time_listener(self, listener: Callable) -> None:
        """
        remove_start_time_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "start_time".

            C++ signature :
                void remove_start_time_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_swing_amount_listener(self, listener: Callable) -> None:
        """
        remove_swing_amount_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "swing_amount".

            C++ signature :
                void remove_swing_amount_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_tempo_follower_enabled_listener(self, listener: Callable) -> None:
        """
        remove_tempo_follower_enabled_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "tempo_follower_enabled".

            C++ signature :
                void remove_tempo_follower_enabled_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_tempo_listener(self, listener: Callable) -> None:
        """
        remove_tempo_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "tempo".

            C++ signature :
                void remove_tempo_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_tracks_listener(self, listener: Callable) -> None:
        """
        remove_tracks_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "tracks".

            C++ signature :
                void remove_tracks_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_tuning_system_listener(self, listener: Callable) -> None:
        """
        remove_tuning_system_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "tuning_system".

            C++ signature :
                void remove_tuning_system_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def remove_visible_tracks_listener(self, listener: Callable) -> None:
        """
        remove_visible_tracks_listener( (Song)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "visible_tracks".

            C++ signature :
                void remove_visible_tracks_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def return_tracks_has_listener(self, listener: Callable) -> bool:
        """
        return_tracks_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "return_tracks".

            C++ signature :
                bool return_tracks_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def root_note_has_listener(self, listener: Callable) -> bool:
        """
        root_note_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "root_note".

            C++ signature :
                bool root_note_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def scale_intervals_has_listener(self, listener: Callable) -> bool:
        """
        scale_intervals_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "scale_intervals".

            C++ signature :
                bool scale_intervals_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def scale_name_has_listener(self, listener: Callable) -> bool:
        """
        scale_name_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "scale_name".

            C++ signature :
                bool scale_name_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def scenes_has_listener(self, listener: Callable) -> bool:
        """
        scenes_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "scenes".

            C++ signature :
                bool scenes_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def scrub_by(self, arg2: float) -> None:
        """
        scrub_by( (Song)arg1, (float)arg2) -> None :
            Same as jump_by, but does not stop playback.

            C++ signature :
                void scrub_by(TPyHandle<ASong>,double)
        """

    def session_automation_record_has_listener(self, listener: Callable) -> bool:
        """
        session_automation_record_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "session_automation_record".

            C++ signature :
                bool session_automation_record_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def session_record_has_listener(self, listener: Callable) -> bool:
        """
        session_record_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "session_record".

            C++ signature :
                bool session_record_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def session_record_status_has_listener(self, listener: Callable) -> bool:
        """
        session_record_status_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "session_record_status".

            C++ signature :
                bool session_record_status_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def set_data(self, key: object, value: object) -> None:
        """
        set_data( (Song)arg1, (object)key, (object)value) -> None :
            Store data for the given key in this object. The data is persistent and will be restored when loading the Live Set.

            C++ signature :
                void set_data(TPyHandle<ASong>,TString,boost::python::api::object)
        """

    def set_or_delete_cue(self) -> None:
        """
        set_or_delete_cue( (Song)arg1) -> None :
            When a cue is selected, it gets deleted. If no cue is selected,
            a new cue is created at the current global songtime.

            C++ signature :
                void set_or_delete_cue(TPyHandle<ASong>)
        """

    def signature_denominator_has_listener(self, listener: Callable) -> bool:
        """
        signature_denominator_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "signature_denominator".

            C++ signature :
                bool signature_denominator_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def signature_numerator_has_listener(self, listener: Callable) -> bool:
        """
        signature_numerator_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "signature_numerator".

            C++ signature :
                bool signature_numerator_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def song_length_has_listener(self, listener: Callable) -> bool:
        """
        song_length_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "song_length".

            C++ signature :
                bool song_length_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def start_playing(self) -> None:
        """
        start_playing( (Song)arg1) -> None :
            Start playing from the startmarker

            C++ signature :
                void start_playing(TPyHandle<ASong>)
        """

    def start_time_has_listener(self, listener: Callable) -> bool:
        """
        start_time_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "start_time".

            C++ signature :
                bool start_time_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def stop_all_clips(self, Quantized: bool = True) -> None:
        """
        stop_all_clips( (Song)arg1 [, (bool)Quantized=True]) -> None :
            Stop all playing Clips (if any) but continue playing the Song.

            C++ signature :
                void stop_all_clips(TPyHandle<ASong> [,bool=True])
        """

    def stop_playing(self) -> None:
        """
        stop_playing( (Song)arg1) -> None :
            Stop playing the Song.

            C++ signature :
                void stop_playing(TPyHandle<ASong>)
        """

    def swing_amount_has_listener(self, listener: Callable) -> bool:
        """
        swing_amount_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "swing_amount".

            C++ signature :
                bool swing_amount_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def tap_tempo(self) -> None:
        """
        tap_tempo( (Song)arg1) -> None :
            Trigger the tap tempo function.

            C++ signature :
                void tap_tempo(TPyHandle<ASong>)
        """

    def tempo_follower_enabled_has_listener(self, listener: Callable) -> bool:
        """
        tempo_follower_enabled_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "tempo_follower_enabled".

            C++ signature :
                bool tempo_follower_enabled_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def tempo_has_listener(self, listener: Callable) -> bool:
        """
        tempo_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "tempo".

            C++ signature :
                bool tempo_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def tracks_has_listener(self, listener: Callable) -> bool:
        """
        tracks_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "tracks".

            C++ signature :
                bool tracks_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def trigger_session_record(self, record_length: float | None = None) -> None:
        """
        trigger_session_record( (Song)self [, (float)record_length=1.7976931348623157e+308]) -> None :
            Triggers a new session recording.

            C++ signature :
                void trigger_session_record(TPyHandle<ASong> [,double=1.7976931348623157e+308])
        """

    def tuning_system_has_listener(self, listener: Callable) -> bool:
        """
        tuning_system_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "tuning_system".

            C++ signature :
                bool tuning_system_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    def undo(self) -> str:
        """
        undo( (Song)arg1) -> str :
            Undo the last action that was made.

            C++ signature :
                TString undo(TPyHandle<ASong>)
        """

    def visible_tracks_has_listener(self, listener: Callable) -> bool:
        """
        visible_tracks_has_listener( (Song)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "visible_tracks".

            C++ signature :
                bool visible_tracks_has_listener(TPyHandle<ASong>,boost::python::api::object)
        """

    @property
    def appointed_device(self) -> Device:
        """
        Read, write, and listen access to the appointed Device
        """

    @appointed_device.setter
    def appointed_device(self, value: Device) -> None:
        pass

    @property
    def arrangement_overdub(self) -> Any:
        """
        Get/Set the global arrangement overdub state.
        """

    @arrangement_overdub.setter
    def arrangement_overdub(self, value: Any) -> None:
        pass

    @property
    def back_to_arranger(self) -> Any:
        """
        Get/Set if triggering a Clip in the Session, disabled the playback of
        Clips in the Arranger.
        """

    @back_to_arranger.setter
    def back_to_arranger(self, value: Any) -> None:
        pass

    @property
    def can_capture_midi(self) -> bool:
        """
        Get whether there currently is material to be captured on any tracks.
        """

    @property
    def can_jump_to_next_cue(self) -> bool:
        """
        Returns true when there is a cue marker right to the playing pos that
        we could jump to.
        """

    @property
    def can_jump_to_prev_cue(self) -> bool:
        """
        Returns true when there is a cue marker left to the playing pos that
        we could jump to.
        """

    @property
    def can_redo(self) -> bool:
        """
        Returns true if there is an undone action that we can redo.
        """

    @property
    def can_undo(self) -> bool:
        """
        Returns true if there is an action that we can restore.
        """

    @property
    def canonical_parent(self) -> Any:
        """
        Get the canonical parent of the song.
        """

    @property
    def clip_trigger_quantization(self) -> Any:
        """
        Get/Set access to the quantization settings that are used to fire
        Clips in the Session.
        """

    @clip_trigger_quantization.setter
    def clip_trigger_quantization(self, value: Any) -> None:
        pass

    @property
    def count_in_duration(self) -> Any:
        """
        Get the count in duration. Returns an index, mapped as follows:
        0 - None, 1 - 1 Bar, 2 - 2 Bars, 3 - 4 Bars.
        """

    @property
    def cue_points(self) -> Any:
        """
        Const access to a list of all cue points of the Live Song.
        """

    @property
    def current_song_time(self) -> Any:
        """
        Get/Set access to the songs current playing position in beats.
        """

    @current_song_time.setter
    def current_song_time(self, value: Any) -> None:
        pass

    @property
    def exclusive_arm(self) -> Any:
        """
        Get if Tracks should be armed exclusively by default.
        """

    @property
    def exclusive_solo(self) -> Any:
        """
        Get if Tracks should be soloed exclusively by default.
        """

    @property
    def groove_amount(self) -> Any:
        """
        Get/Set the global groove amount, that adjust all setup grooves
        in all clips.
        """

    @groove_amount.setter
    def groove_amount(self, value: Any) -> None:
        pass

    @property
    def groove_pool(self) -> Any:
        """
        Get the groove pool.
        """

    @property
    def is_ableton_link_enabled(self) -> bool:
        """
        Enable/disable Ableton Link.
        """

    @property
    def is_ableton_link_start_stop_sync_enabled(self) -> bool:
        """
        Enable/disable Ableton Link Start Stop Sync.
        """

    @property
    def is_counting_in(self) -> bool:
        """
        Get whether currently counting in.
        """

    @property
    def is_playing(self) -> bool:
        """
        Returns true if the Song is currently playing.
        """

    @property
    def last_event_time(self) -> Any:
        """
        Return the time of the last set event in the song. In contrary to
        song_length, this will not add some extra beats that are mostly needed
        for Display purposes in the Arrangerview.
        """

    @property
    def loop(self) -> Any:
        """
        Get/Set the looping flag that en/disables the usage of the global
        loop markers in the song.
        """

    @loop.setter
    def loop(self, value: Any) -> None:
        pass

    @property
    def loop_length(self) -> Any:
        """
        Get/Set the length of the global loop marker position in beats.
        """

    @loop_length.setter
    def loop_length(self, value: Any) -> None:
        pass

    @property
    def loop_start(self) -> Any:
        """
        Get/Set the start of the global loop marker position in beats.
        """

    @loop_start.setter
    def loop_start(self, value: Any) -> None:
        pass

    @property
    def master_track(self) -> Track:
        """
        Access to the Main Track (always available)
        """

    @property
    def metronome(self) -> Any:
        """
        Get/Set if the metronom is audible.
        """

    @metronome.setter
    def metronome(self, value: Any) -> None:
        pass

    @property
    def midi_recording_quantization(self) -> Any:
        """
        Get/Set access to the settings that are used to quantize
        MIDI recordings.
        """

    @midi_recording_quantization.setter
    def midi_recording_quantization(self, value: Any) -> None:
        pass

    @property
    def nudge_down(self) -> Any:
        """
        Get/Set the status of the nudge down button.
        """

    @nudge_down.setter
    def nudge_down(self, value: Any) -> None:
        pass

    @property
    def nudge_up(self) -> Any:
        """
        Get/Set the status of the nudge up button.
        """

    @nudge_up.setter
    def nudge_up(self, value: Any) -> None:
        pass

    @property
    def overdub(self) -> Any:
        """
        Legacy hook for Live 8 overdub state. Now hooks to
        session record, but never starts playback.
        """

    @property
    def punch_in(self) -> Any:
        """
        Get/Set the flag that will enable recording as soon as the Song plays
        and hits the global loop start region.
        """

    @punch_in.setter
    def punch_in(self, value: Any) -> None:
        pass

    @property
    def punch_out(self) -> Any:
        """
        Get/Set the flag that will disable recording as soon as the Song plays
        and hits the global loop end region.
        """

    @punch_out.setter
    def punch_out(self, value: Any) -> None:
        pass

    @property
    def re_enable_automation_enabled(self) -> Any:
        """
        Returns true if some automated parameter has been overriden
        """

    @property
    def record_mode(self) -> Any:
        """
        Get/Set the state of the global recording flag.
        """

    @record_mode.setter
    def record_mode(self, value: Any) -> None:
        pass

    @property
    def return_tracks(self) -> list[Track]:
        """
        Const access to the list of available Return Tracks.
        """

    @property
    def root_note(self) -> Any:
        """
        Set and access the root note (i.e. key) of the song used for control surfaces. The root note can be a number between 0 and 11, with 0 corresponding to C and 11 corresponding to B.
        """

    @property
    def scale_intervals(self) -> Any:
        """
        Reports the current scale's intervals as a list of integers, starting with the root note and representing the number of halfsteps (e.g. Major -> 0, 2, 4, 5, 7, 9, 11)
        """

    @property
    def scale_name(self) -> str:
        """
        Set and access the last used scale name for control surfaces. The default scale names that can be saved with a set and recalled are
        'Major', 'Minor', 'Dorian', 'Mixolydian' ,'Lydian' ,'Phrygian' ,'Locrian',
        'Whole Tone', 'Half-whole Dim.', 'Whole-half Dim.', 'Minor Blues',
        'Minor Pentatonic', 'Major Pentatonic', 'Harmonic Minor', 'Harmonic Major',
        'Dorian #4', 'Phrygian Dominant', 'Melodic Minor', 'Lydian Augmented',
        'Lydian Dominant', 'Super Locrian', 'Bhairav', 'Hungarian Minor',
        '8-Tone Spanish', 'Hirajoshi', 'In-Sen', 'Iwato', 'Kumoi', 'Pelog Selisir',
        'Pelog Tembung', 'Messaien 3', 'Messaien 4', 'Messaien 5', 'Messaien 6',
        'Messaien 7'
        """

    @property
    def scenes(self) -> list[Scene]:
        """
        Const access to a list of all Scenes in the Live Song.
        """

    @property
    def select_on_launch(self) -> Any:
        """
        Get if Scenes and Clips should be selected when fired.
        """

    @property
    def session_automation_record(self) -> Any:
        """
        Returns true if automation recording is enabled.
        """

    @property
    def session_record(self) -> Any:
        """
        Get/Set the session record state.
        """

    @session_record.setter
    def session_record(self, value: Any) -> None:
        pass

    @property
    def session_record_status(self) -> Any:
        """
        Get the session slot-recording state.
        """

    @property
    def signature_denominator(self) -> Any:
        """
        Get/Set access to the global signature denominator of the Song.
        """

    @signature_denominator.setter
    def signature_denominator(self, value: Any) -> None:
        pass

    @property
    def signature_numerator(self) -> Any:
        """
        Get/Set access to the global signature numerator of the Song.
        """

    @signature_numerator.setter
    def signature_numerator(self, value: Any) -> None:
        pass

    @property
    def song_length(self) -> Any:
        """
        Return the time of the last set event in the song, plus som extra beats
        that are usually added for better navigation in the arrangerview.
        """

    @property
    def start_time(self) -> Any:
        """
        Get/Set access to the songs current start time in beats. The set time
        may be overridden by the current loop/locator start time.
        """

    @start_time.setter
    def start_time(self, value: Any) -> None:
        pass

    @property
    def swing_amount(self) -> Any:
        """
        Get/Set access to the amount of swing that is applied when adding or quantizing notes to MIDI clips
        """

    @swing_amount.setter
    def swing_amount(self, value: Any) -> None:
        pass

    @property
    def tempo(self) -> float:
        """
        Get/Set the global project tempo.
        """

    @tempo.setter
    def tempo(self, value: float) -> None:
        pass

    @property
    def tempo_follower_enabled(self) -> Any:
        """
        Get/Set whether the Tempo Follower is controlling the tempo. The Tempo Follower Toggle must be made visible in the preferences for this property to be effective.
        """

    @tempo_follower_enabled.setter
    def tempo_follower_enabled(self, value: Any) -> None:
        pass

    @property
    def tracks(self) -> list[Track]:
        """
        Const access to a list of all Player Tracks in the Live Song, excluding
        the return and Main Track (see also Song.send_tracks and Song.master_track).
        At least one MIDI or Audio Track is always available.
        """

    @property
    def tuning_system(self) -> Any:
        """
        Access the currently active tuning system.
        """

    @property
    def view(self) -> View:
        """
        Representing the view aspects of a Live document:
        The Session and Arrangerview.
        """

    @property
    def visible_tracks(self) -> list[Track]:
        """
        Const access to a list of all visible Player Tracks in the Live Song, excluding
        the return and Main Track (see also Song.send_tracks and Song.master_track).
        At least one MIDI or Audio Track is always available.
        """


class TimeFormat:
    """
    Class that represent an enumeration of values for TimeFormat
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

    ms_time = 0
    smpte_24 = 1
    smpte_25 = 2
    smpte_30 = 3
    smpte_30_drop = 4
    smpte_29 = 5


class TuningSystem:
    """
    Represents a Tuning System and its properties.
    """

    @property
    def maximum_note(self) -> Any:
        """
        Returns a tuple where the first entry is the index within the pseudo octave and
        the second entry is the octave or the maximum note in the tuning system.
        """

    @property
    def minimum_note(self) -> Any:
        """
        Returns a tuple where the first entry is the index within the pseudo octave and
        the second entry is the octave or the minimum note in the tuning system.
        """

    @property
    def number_of_notes_in_pseudo_octave(self) -> Any:
        """
        Get the number of notes in the pseudo octave.
        """


def get_all_scales_ordered() -> tuple:
    """
    get_all_scales_ordered() -> tuple :
        Get an ordered tuple of tuples of all available scale names to intervals.

        C++ signature :
            boost::python::tuple get_all_scales_ordered()
    """

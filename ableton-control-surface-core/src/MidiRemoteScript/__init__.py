from __future__ import annotations

from typing import Any, Callable


class FullVelocity:
    @property
    def enabled(self) -> Any:
        pass


class MidiRemoteScript:
    def handle(self) -> int:
        """
        handle( (MidiRemoteScript)arg1) -> int :

            C++ signature :
                int handle(TMidiRemoteScript*)
        """

    def instance_identifier(self) -> int:
        """
        instance_identifier( (MidiRemoteScript)arg1) -> int :

            C++ signature :
                int instance_identifier(TMidiRemoteScript*)
        """

    def log_message(self, arg2: object) -> None:
        """
        log_message( (MidiRemoteScript)arg1, (object)arg2) -> None :

            C++ signature :
                void log_message(TMidiRemoteScript*,TString)
        """

    def preferences(self, arg2: object) -> Preferences:
        """
        preferences( (MidiRemoteScript)arg1, (object)arg2) -> Preferences :

            C++ signature :
                TWeakPtr<APythonPreferenceEntry> preferences(TMidiRemoteScript*,TString)
        """

    def release_controlled_track(self) -> None:
        """
        release_controlled_track( (MidiRemoteScript)arg1) -> None :
            Disclaimer: The API functions/properties used for Push will be changed or removed and may not be available in the future.

            C++ signature :
                void release_controlled_track(TMidiRemoteScript*)
        """

    def request_rebuild_midi_map(self) -> None:
        """
        request_rebuild_midi_map( (MidiRemoteScript)arg1) -> None :

            C++ signature :
                void request_rebuild_midi_map(TMidiRemoteScript*)
        """

    def reset_input_history(self) -> None:
        """
        reset_input_history( (MidiRemoteScript)arg1) -> None :

            C++ signature :
                void reset_input_history(TMidiRemoteScript*)
        """

    def send_midi(self, arg2: object) -> None:
        """
        send_midi( (MidiRemoteScript)arg1, (tuple)arg2) -> None :

            C++ signature :
                void send_midi(TMidiRemoteScript*,boost::python::tuple)
        """

    def set_cc_translation(self, arg2: int, arg3: int, arg4: int, arg5: int) -> None:
        """
        set_cc_translation( (MidiRemoteScript)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5) -> None :

            C++ signature :
                void set_cc_translation(TMidiRemoteScript*,int,int,int,int)
        """

    def set_controlled_track(self, arg2: object) -> None:
        """
        set_controlled_track( (MidiRemoteScript)arg1, (Track)arg2) -> None :
            Disclaimer: The API functions/properties used for Push will be changed or removed and may not be available in the future.

            C++ signature :
                void set_controlled_track(TMidiRemoteScript*,TTrackPyHandle)
        """

    def set_feedback_channels(self, arg2: object) -> None:
        """
        set_feedback_channels( (MidiRemoteScript)arg1, (list)arg2) -> None :
            Disclaimer: The API functions/properties used for Push will be changed or removed and may not be available in the future.

            C++ signature :
                void set_feedback_channels(TMidiRemoteScript*,boost::python::list)
        """

    def set_feedback_velocity(self, arg2: int) -> None:
        """
        set_feedback_velocity( (MidiRemoteScript)arg1, (int)arg2) -> None :
            Disclaimer: The API functions/properties used for Push will be changed or removed and may not be available in the future.

            C++ signature :
                void set_feedback_velocity(TMidiRemoteScript {lvalue},int)
        """

    def set_note_translation(self, arg2: int, arg3: int, arg4: int, arg5: int) -> None:
        """
        set_note_translation( (MidiRemoteScript)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5) -> None :

            C++ signature :
                void set_note_translation(TMidiRemoteScript*,int,int,int,int)
        """

    def set_pad_translation(self, arg2: object) -> None:
        """
        set_pad_translation( (MidiRemoteScript)arg1, (tuple)arg2) -> None :

            C++ signature :
                void set_pad_translation(TMidiRemoteScript*,boost::python::tuple)
        """

    def set_session_highlight(
        self,
        track_offset: int,
        scene_offset: int,
        width: int,
        height: int,
        include_return_tracks: bool = False,
        include_rack_chains: bool = False,
    ) -> None:
        """
        set_session_highlight( (MidiRemoteScript)arg1, (int)track_offset, (int)scene_offset, (int)width, (int)height [, (bool)include_return_tracks=False [, (bool)include_rack_chains=False]]) -> None :

            C++ signature :
                void set_session_highlight(TMidiRemoteScript*,int,int,int,int [,bool=False [,bool=False]])
        """

    def set_sync_sysex_macos(self, arg2: bool) -> None:
        """
        set_sync_sysex_macos( (MidiRemoteScript)arg1, (bool)arg2) -> None :

            C++ signature :
                void set_sync_sysex_macos(TMidiRemoteScript*,bool)
        """

    def show_message(self, arg2: object) -> None:
        """
        show_message( (MidiRemoteScript)arg1, (object)arg2) -> None :

            C++ signature :
                void show_message(TMidiRemoteScript*,TString)
        """

    def song(self) -> Song:
        """
        song( (MidiRemoteScript)arg1) -> Song :

            C++ signature :
                TWeakPtr<TPyHandle<ASong>> song(TMidiRemoteScript*)
        """

    def toggle_lock(self) -> None:
        """
        toggle_lock( (MidiRemoteScript)arg1) -> None :

            C++ signature :
                void toggle_lock(TMidiRemoteScript*)
        """

    def update_locks(self) -> None:
        """
        update_locks( (MidiRemoteScript)arg1) -> None :

            C++ signature :
                void update_locks(TMidiRemoteScript*)
        """

    @property
    def full_velocity(self) -> Any:
        """
        Disclaimer: The API functions/properties used for Push will be changed or removed and may not be available in the future.
        """

    @property
    def note_repeat(self) -> Any:
        """
        Disclaimer: The API functions/properties used for Push will be changed or removed and may not be available in the future.
        """

    @property
    def playhead(self) -> Any:
        """
        Disclaimer: The API functions/properties used for Push will be changed or removed and may not be available in the future.
        """

    @property
    def velocity_levels(self) -> Any:
        """
        Disclaimer: The API functions/properties used for Push will be changed or removed and may not be available in the future.
        """


class MutableVector:
    """
    A vector of things that is mutable and creatable from Python
    """

    def append(self, arg2: object) -> None:
        """
        append( (MutableVector)arg1, (object)arg2) -> None :

            C++ signature :
                void append(std::__1::vector<std::__1::variant<int, float, TPush2Visualisation::TVisualisationColor, std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>>, std::__1::allocator<std::__1::variant<int, float, TPush2Visualisation::TVisualisationColor, std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>>>> {lvalue},boost::python::api::object)
        """

    def extend(self, arg2: object) -> None:
        """
        extend( (MutableVector)arg1, (object)arg2) -> None :

            C++ signature :
                void extend(std::__1::vector<std::__1::variant<int, float, TPush2Visualisation::TVisualisationColor, std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>>, std::__1::allocator<std::__1::variant<int, float, TPush2Visualisation::TVisualisationColor, std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>>>> {lvalue},boost::python::api::object)
        """


class NoteRepeat:
    @property
    def aftertouch_ramp_length(self) -> Any:
        pass

    @property
    def aftertouch_ramp_start(self) -> Any:
        pass

    @property
    def enabled(self) -> Any:
        pass

    @property
    def repeat_rate(self) -> Any:
        pass


class Playhead:
    def set_feedback_channels(self, arg2: object) -> None:
        """
        set_feedback_channels( (Playhead)arg1, (list)arg2) -> None :
            Set the list of channels the notes representing playhead steps will be sent on.

            C++ signature :
                void set_feedback_channels(ATimeToMidiModule {lvalue},boost::python::list)
        """

    @property
    def clip(self) -> Clip:
        """
        The associated clip
        """

    @property
    def notes(self) -> Any:
        """
        Sequence of midi notes that represent the steps of the playhead
        """

    @property
    def start_time(self) -> Any:
        """
        The time at which the first midi note will be sent. It is relative to the clip.
        """

    @property
    def step_length(self) -> Any:
        """
        Time between each sent midi note.
        """

    @property
    def track(self) -> Track:
        """
        The track of the associated clip
        """

    @property
    def velocity(self) -> Any:
        """
        The velocity that is used for every sent note
        """

    @property
    def wrap_around(self) -> Any:
        """
        Enables/Disables wrapping of the playhead.
        """


class Preferences:
    def set_serializer(self, arg2: object) -> None:
        """
        set_serializer( (Preferences)arg1, (object)arg2) -> None :

            C++ signature :
                void set_serializer(APythonPreferenceEntry {lvalue},boost::python::api::object)
        """


class Push2MidiRemoteScript:
    def handle(self) -> int:
        """
        handle( (MidiRemoteScript)arg1) -> int :

            C++ signature :
                int handle(TMidiRemoteScript*)
        """

    def instance_identifier(self) -> int:
        """
        instance_identifier( (MidiRemoteScript)arg1) -> int :

            C++ signature :
                int instance_identifier(TMidiRemoteScript*)
        """

    def launch_external_process(self) -> None:
        """
        launch_external_process( (Push2MidiRemoteScript)arg1) -> None :
            Disclaimer: The API functions/properties used for Push and Push 2 will be changed or removed and may not be available in the future.

            C++ signature :
                void launch_external_process(TPush2MidiRemoteScript {lvalue})
        """

    def log_message(self, arg2: object) -> None:
        """
        log_message( (MidiRemoteScript)arg1, (object)arg2) -> None :

            C++ signature :
                void log_message(TMidiRemoteScript*,TString)
        """

    def preferences(self, arg2: object) -> Preferences:
        """
        preferences( (MidiRemoteScript)arg1, (object)arg2) -> Preferences :

            C++ signature :
                TWeakPtr<APythonPreferenceEntry> preferences(TMidiRemoteScript*,TString)
        """

    def process_connected(self) -> bool:
        """
        process_connected( (Push2MidiRemoteScript)arg1) -> bool :
            Disclaimer: The API functions/properties used for Push and Push 2 will be changed or removed and may not be available in the future.

            C++ signature :
                bool process_connected(TPush2MidiRemoteScript {lvalue})
        """

    def release_controlled_track(self) -> None:
        """
        release_controlled_track( (MidiRemoteScript)arg1) -> None :
            Disclaimer: The API functions/properties used for Push will be changed or removed and may not be available in the future.

            C++ signature :
                void release_controlled_track(TMidiRemoteScript*)
        """

    def request_rebuild_midi_map(self) -> None:
        """
        request_rebuild_midi_map( (MidiRemoteScript)arg1) -> None :

            C++ signature :
                void request_rebuild_midi_map(TMidiRemoteScript*)
        """

    def reset_input_history(self) -> None:
        """
        reset_input_history( (MidiRemoteScript)arg1) -> None :

            C++ signature :
                void reset_input_history(TMidiRemoteScript*)
        """

    def send_midi(self, arg2: object) -> None:
        """
        send_midi( (MidiRemoteScript)arg1, (tuple)arg2) -> None :

            C++ signature :
                void send_midi(TMidiRemoteScript*,boost::python::tuple)
        """

    def send_model_update(self, arg2: object) -> None:
        """
        send_model_update( (Push2MidiRemoteScript)arg1, (object)arg2) -> None :
            Disclaimer: The API functions/properties used for Push and Push 2 will be changed or removed and may not be available in the future.

            C++ signature :
                void send_model_update(TPush2MidiRemoteScript {lvalue},TArray<unsigned char>)
        """

    def set_cc_translation(self, arg2: int, arg3: int, arg4: int, arg5: int) -> None:
        """
        set_cc_translation( (MidiRemoteScript)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5) -> None :

            C++ signature :
                void set_cc_translation(TMidiRemoteScript*,int,int,int,int)
        """

    def set_controlled_track(self, arg2: object) -> None:
        """
        set_controlled_track( (MidiRemoteScript)arg1, (Track)arg2) -> None :
            Disclaimer: The API functions/properties used for Push will be changed or removed and may not be available in the future.

            C++ signature :
                void set_controlled_track(TMidiRemoteScript*,TTrackPyHandle)
        """

    def set_feedback_channels(self, arg2: object) -> None:
        """
        set_feedback_channels( (MidiRemoteScript)arg1, (list)arg2) -> None :
            Disclaimer: The API functions/properties used for Push will be changed or removed and may not be available in the future.

            C++ signature :
                void set_feedback_channels(TMidiRemoteScript*,boost::python::list)
        """

    def set_feedback_velocity(self, arg2: int) -> None:
        """
        set_feedback_velocity( (MidiRemoteScript)arg1, (int)arg2) -> None :
            Disclaimer: The API functions/properties used for Push will be changed or removed and may not be available in the future.

            C++ signature :
                void set_feedback_velocity(TMidiRemoteScript {lvalue},int)
        """

    def set_firmware_version(self, arg2: float) -> None:
        """
        set_firmware_version( (PushMidiRemoteScript)arg1, (float)arg2) -> None :

            C++ signature :
                void set_firmware_version(TPushMidiRemoteScript {lvalue},float)
        """

    def set_note_translation(self, arg2: int, arg3: int, arg4: int, arg5: int) -> None:
        """
        set_note_translation( (MidiRemoteScript)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5) -> None :

            C++ signature :
                void set_note_translation(TMidiRemoteScript*,int,int,int,int)
        """

    def set_pad_translation(self, arg2: object) -> None:
        """
        set_pad_translation( (MidiRemoteScript)arg1, (tuple)arg2) -> None :

            C++ signature :
                void set_pad_translation(TMidiRemoteScript*,boost::python::tuple)
        """

    def set_session_highlight(
        self,
        track_offset: int,
        scene_offset: int,
        width: int,
        height: int,
        include_return_tracks: bool = False,
        include_rack_chains: bool = False,
    ) -> None:
        """
        set_session_highlight( (MidiRemoteScript)arg1, (int)track_offset, (int)scene_offset, (int)width, (int)height [, (bool)include_return_tracks=False [, (bool)include_rack_chains=False]]) -> None :

            C++ signature :
                void set_session_highlight(TMidiRemoteScript*,int,int,int,int [,bool=False [,bool=False]])
        """

    def set_sync_sysex_macos(self, arg2: bool) -> None:
        """
        set_sync_sysex_macos( (MidiRemoteScript)arg1, (bool)arg2) -> None :

            C++ signature :
                void set_sync_sysex_macos(TMidiRemoteScript*,bool)
        """

    def show_message(self, arg2: object) -> None:
        """
        show_message( (MidiRemoteScript)arg1, (object)arg2) -> None :

            C++ signature :
                void show_message(TMidiRemoteScript*,TString)
        """

    def song(self) -> Song:
        """
        song( (MidiRemoteScript)arg1) -> Song :

            C++ signature :
                TWeakPtr<TPyHandle<ASong>> song(TMidiRemoteScript*)
        """

    def toggle_lock(self) -> None:
        """
        toggle_lock( (MidiRemoteScript)arg1) -> None :

            C++ signature :
                void toggle_lock(TMidiRemoteScript*)
        """

    def update_locks(self) -> None:
        """
        update_locks( (MidiRemoteScript)arg1) -> None :

            C++ signature :
                void update_locks(TMidiRemoteScript*)
        """

    @property
    def full_velocity(self) -> Any:
        """
        Disclaimer: The API functions/properties used for Push will be changed or removed and may not be available in the future.
        """

    @property
    def note_repeat(self) -> Any:
        """
        Disclaimer: The API functions/properties used for Push will be changed or removed and may not be available in the future.
        """

    @property
    def playhead(self) -> Any:
        """
        Disclaimer: The API functions/properties used for Push will be changed or removed and may not be available in the future.
        """

    @property
    def real_time_mapper(self) -> Any:
        """
        Disclaimer: The API functions/properties used for Push and Push 2 will be changed or removed and may not be available in the future.
        """

    @property
    def velocity_levels(self) -> Any:
        """
        Disclaimer: The API functions/properties used for Push will be changed or removed and may not be available in the future.
        """


class Push2ProcessState:
    """
    Class that represent an enumeration of values for Push2ProcessState
    The state the external process is in.
    """

    initialized = 0
    launching = 1
    running = 2
    connected = 3
    died = 4
    terminated = 5
    killed = 6
    wait_for_termination = 7
    defunct_process_wait_for_termination = 8
    defunct_process_terminated = 9
    defunct_process_killed = 10


class PushMidiRemoteScript:
    def handle(self) -> int:
        """
        handle( (MidiRemoteScript)arg1) -> int :

            C++ signature :
                int handle(TMidiRemoteScript*)
        """

    def instance_identifier(self) -> int:
        """
        instance_identifier( (MidiRemoteScript)arg1) -> int :

            C++ signature :
                int instance_identifier(TMidiRemoteScript*)
        """

    def log_message(self, arg2: object) -> None:
        """
        log_message( (MidiRemoteScript)arg1, (object)arg2) -> None :

            C++ signature :
                void log_message(TMidiRemoteScript*,TString)
        """

    def preferences(self, arg2: object) -> Preferences:
        """
        preferences( (MidiRemoteScript)arg1, (object)arg2) -> Preferences :

            C++ signature :
                TWeakPtr<APythonPreferenceEntry> preferences(TMidiRemoteScript*,TString)
        """

    def release_controlled_track(self) -> None:
        """
        release_controlled_track( (MidiRemoteScript)arg1) -> None :
            Disclaimer: The API functions/properties used for Push will be changed or removed and may not be available in the future.

            C++ signature :
                void release_controlled_track(TMidiRemoteScript*)
        """

    def request_rebuild_midi_map(self) -> None:
        """
        request_rebuild_midi_map( (MidiRemoteScript)arg1) -> None :

            C++ signature :
                void request_rebuild_midi_map(TMidiRemoteScript*)
        """

    def reset_input_history(self) -> None:
        """
        reset_input_history( (MidiRemoteScript)arg1) -> None :

            C++ signature :
                void reset_input_history(TMidiRemoteScript*)
        """

    def send_midi(self, arg2: object) -> None:
        """
        send_midi( (MidiRemoteScript)arg1, (tuple)arg2) -> None :

            C++ signature :
                void send_midi(TMidiRemoteScript*,boost::python::tuple)
        """

    def set_cc_translation(self, arg2: int, arg3: int, arg4: int, arg5: int) -> None:
        """
        set_cc_translation( (MidiRemoteScript)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5) -> None :

            C++ signature :
                void set_cc_translation(TMidiRemoteScript*,int,int,int,int)
        """

    def set_controlled_track(self, arg2: object) -> None:
        """
        set_controlled_track( (MidiRemoteScript)arg1, (Track)arg2) -> None :
            Disclaimer: The API functions/properties used for Push will be changed or removed and may not be available in the future.

            C++ signature :
                void set_controlled_track(TMidiRemoteScript*,TTrackPyHandle)
        """

    def set_feedback_channels(self, arg2: object) -> None:
        """
        set_feedback_channels( (MidiRemoteScript)arg1, (list)arg2) -> None :
            Disclaimer: The API functions/properties used for Push will be changed or removed and may not be available in the future.

            C++ signature :
                void set_feedback_channels(TMidiRemoteScript*,boost::python::list)
        """

    def set_feedback_velocity(self, arg2: int) -> None:
        """
        set_feedback_velocity( (MidiRemoteScript)arg1, (int)arg2) -> None :
            Disclaimer: The API functions/properties used for Push will be changed or removed and may not be available in the future.

            C++ signature :
                void set_feedback_velocity(TMidiRemoteScript {lvalue},int)
        """

    def set_firmware_version(self, arg2: float) -> None:
        """
        set_firmware_version( (PushMidiRemoteScript)arg1, (float)arg2) -> None :

            C++ signature :
                void set_firmware_version(TPushMidiRemoteScript {lvalue},float)
        """

    def set_note_translation(self, arg2: int, arg3: int, arg4: int, arg5: int) -> None:
        """
        set_note_translation( (MidiRemoteScript)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5) -> None :

            C++ signature :
                void set_note_translation(TMidiRemoteScript*,int,int,int,int)
        """

    def set_pad_translation(self, arg2: object) -> None:
        """
        set_pad_translation( (MidiRemoteScript)arg1, (tuple)arg2) -> None :

            C++ signature :
                void set_pad_translation(TMidiRemoteScript*,boost::python::tuple)
        """

    def set_session_highlight(
        self,
        track_offset: int,
        scene_offset: int,
        width: int,
        height: int,
        include_return_tracks: bool = False,
        include_rack_chains: bool = False,
    ) -> None:
        """
        set_session_highlight( (MidiRemoteScript)arg1, (int)track_offset, (int)scene_offset, (int)width, (int)height [, (bool)include_return_tracks=False [, (bool)include_rack_chains=False]]) -> None :

            C++ signature :
                void set_session_highlight(TMidiRemoteScript*,int,int,int,int [,bool=False [,bool=False]])
        """

    def set_sync_sysex_macos(self, arg2: bool) -> None:
        """
        set_sync_sysex_macos( (MidiRemoteScript)arg1, (bool)arg2) -> None :

            C++ signature :
                void set_sync_sysex_macos(TMidiRemoteScript*,bool)
        """

    def show_message(self, arg2: object) -> None:
        """
        show_message( (MidiRemoteScript)arg1, (object)arg2) -> None :

            C++ signature :
                void show_message(TMidiRemoteScript*,TString)
        """

    def song(self) -> Song:
        """
        song( (MidiRemoteScript)arg1) -> Song :

            C++ signature :
                TWeakPtr<TPyHandle<ASong>> song(TMidiRemoteScript*)
        """

    def toggle_lock(self) -> None:
        """
        toggle_lock( (MidiRemoteScript)arg1) -> None :

            C++ signature :
                void toggle_lock(TMidiRemoteScript*)
        """

    def update_locks(self) -> None:
        """
        update_locks( (MidiRemoteScript)arg1) -> None :

            C++ signature :
                void update_locks(TMidiRemoteScript*)
        """

    @property
    def full_velocity(self) -> Any:
        """
        Disclaimer: The API functions/properties used for Push will be changed or removed and may not be available in the future.
        """

    @property
    def note_repeat(self) -> Any:
        """
        Disclaimer: The API functions/properties used for Push will be changed or removed and may not be available in the future.
        """

    @property
    def playhead(self) -> Any:
        """
        Disclaimer: The API functions/properties used for Push will be changed or removed and may not be available in the future.
        """

    @property
    def velocity_levels(self) -> Any:
        """
        Disclaimer: The API functions/properties used for Push will be changed or removed and may not be available in the future.
        """


class RealTimeMapper:
    def attach_object(self, lom_object: object, channel_type: object) -> tuple:
        """
        attach_object( (RealTimeMapper)self, (object)lom_object, (object)channel_type) -> tuple :
            Attaches the provided LOM object to a suitable channel and returns that channel's id and LOM object id, each as a string. Returns an empty channel id string if no suitable channel is found.Calling this multiple times for the same object and channel type will attach anew channel each time! Each of these channels needs to be detached separately.

            C++ signature :
                boost::python::tuple attach_object(IPythonRealTimeMapper {lvalue},boost::python::api::object,TString)
        """

    def detach_channel(self, channel_id: object) -> None:
        """
        detach_channel( (RealTimeMapper)self, (object)channel_id) -> None :
            Detaches the channel with the provided id if it is attached to a lom_object.

            C++ signature :
                void detach_channel(IPythonRealTimeMapper {lvalue},TString)
        """

    METER_POOLSIZE = 9

    @property
    def client_id(self) -> Any:
        """
        The id used to identify the inter-process connection.
        """

    @property
    def device_visualisation(self) -> Any:
        """
        Visualisation object for device, or None if there isn't one
        """


class RgbaColor:
    @property
    def alpha(self) -> Any:
        pass

    @property
    def blue(self) -> Any:
        pass

    @property
    def green(self) -> Any:
        pass

    @property
    def red(self) -> Any:
        pass


class VelocityLevels:
    def add_last_played_level_listener(self, listener: Callable) -> None:
        """
        add_last_played_level_listener( (VelocityLevels)arg1, (object)arg2) -> None :

            C++ signature :
                void add_last_played_level_listener(AVelocityLevelsModule {lvalue},boost::python::api::object)
        """

    def last_played_level_has_listener(self, listener: Callable) -> bool:
        """
        last_played_level_has_listener( (VelocityLevels)arg1, (object)arg2) -> bool :

            C++ signature :
                bool last_played_level_has_listener(AVelocityLevelsModule {lvalue},boost::python::api::object)
        """

    def remove_last_played_level_listener(self, listener: Callable) -> None:
        """
        remove_last_played_level_listener( (VelocityLevels)arg1, (object)arg2) -> None :

            C++ signature :
                void remove_last_played_level_listener(AVelocityLevelsModule {lvalue},boost::python::api::object)
        """

    @property
    def enabled(self) -> Any:
        pass

    @property
    def last_played_level(self) -> Any:
        pass

    @property
    def levels(self) -> Any:
        pass

    @property
    def notes(self) -> Any:
        pass

    @property
    def source_channel(self) -> Any:
        pass

    @property
    def target_channel(self) -> Any:
        pass

    @property
    def target_note(self) -> Any:
        pass


class Visualisation:
    def get_view_data(self) -> VisualisationViewData:
        """
        get_view_data( (Visualisation)self) -> VisualisationViewData :
            Returns a copy of the view data of the visualisation

            C++ signature :
                std::__1::unordered_map<std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>, std::__1::variant<std::__1::variant<int, float, TPush2Visualisation::TVisualisationColor, std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>>, std::__1::vector<std::__1::variant<int, float, TPush2Visualisation::TVisualisationColor, std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>>, std::__1::allocator<std::__1::variant<int, float, TPush2Visualisation::TVisualisationColor, std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>>>>>, std::__1::hash<std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>>, std::__1::equal_to<std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>>, std::__1::allocator<std::__1::pair<std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>> const, std::__1::variant<std::__1::variant<int, float, TPush2Visualisation::TVisualisationColor, std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>>, std::__1::vector<std::__1::variant<int, float, TPush2Visualisation::TVisualisationColor, std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>>, std::__1::allocator<std::__1::variant<int, float, TPush2Visualisation::TVisualisationColor, std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>>>>>>>> get_view_data(TPush2Visualisation {lvalue})
        """

    def set_view_data(self, view_data: object) -> None:
        """
        set_view_data( (Visualisation)self, (VisualisationViewData)view_data) -> None :
            Copies given view data to the visualisation

            C++ signature :
                void set_view_data(TPush2Visualisation {lvalue},std::__1::unordered_map<std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>, std::__1::variant<std::__1::variant<int, float, TPush2Visualisation::TVisualisationColor, std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>>, std::__1::vector<std::__1::variant<int, float, TPush2Visualisation::TVisualisationColor, std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>>, std::__1::allocator<std::__1::variant<int, float, TPush2Visualisation::TVisualisationColor, std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>>>>>, std::__1::hash<std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>>, std::__1::equal_to<std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>>, std::__1::allocator<std::__1::pair<std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>> const, std::__1::variant<std::__1::variant<int, float, TPush2Visualisation::TVisualisationColor, std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>>, std::__1::vector<std::__1::variant<int, float, TPush2Visualisation::TVisualisationColor, std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>>, std::__1::allocator<std::__1::variant<int, float, TPush2Visualisation::TVisualisationColor, std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>>>>>>>>)
        """


class VisualisationViewData:
    def clear(self) -> None:
        """
        clear( (VisualisationViewData)arg1) -> None :

            C++ signature :
                void clear(std::__1::unordered_map<std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>, std::__1::variant<std::__1::variant<int, float, TPush2Visualisation::TVisualisationColor, std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>>, std::__1::vector<std::__1::variant<int, float, TPush2Visualisation::TVisualisationColor, std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>>, std::__1::allocator<std::__1::variant<int, float, TPush2Visualisation::TVisualisationColor, std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>>>>>, std::__1::hash<std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>>, std::__1::equal_to<std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>>, std::__1::allocator<std::__1::pair<std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>> const, std::__1::variant<std::__1::variant<int, float, TPush2Visualisation::TVisualisationColor, std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>>, std::__1::vector<std::__1::variant<int, float, TPush2Visualisation::TVisualisationColor, std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>>, std::__1::allocator<std::__1::variant<int, float, TPush2Visualisation::TVisualisationColor, std::__1::basic_string<wchar_t, std::__1::char_traits<wchar_t>, std::__1::allocator<wchar_t>>>>>>>>> {lvalue})
        """

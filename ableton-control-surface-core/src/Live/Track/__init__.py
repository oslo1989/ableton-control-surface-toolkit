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
from Live.TuningSystem import *
from Live.WavetableDevice import *


class DeviceContainer:
    """
    This class is a common super class of Track and Chain
    """


class DeviceInsertMode:
    """
    Class that represent an enumeration of values for DeviceInsertMode
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

    default = 0
    selected_left = 1
    selected_right = 2
    count = 3


class RoutingChannel:
    """
    This class represents a routing channel.
    """

    @property
    def display_name(self) -> str:
        """
        Display name of routing channel.
        """

    @property
    def layout(self) -> Any:
        """
        The routing channel's Layout, e.g., mono or stereo.
        """


class RoutingChannelLayout:
    """
    Class that represent an enumeration of values for RoutingChannelLayout
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

    mono = 0
    stereo = 1
    midi = 2


class RoutingChannelVector:
    """
    A container for returning routing channels from Live.
    """

    def append(self, arg2: object) -> None:
        """
        append( (RoutingChannelVector)arg1, (object)arg2) -> None :

            C++ signature :
                void append(std::__1::vector<NRoutingApi::TRoutingChannel, std::__1::allocator<NRoutingApi::TRoutingChannel>> {lvalue},boost::python::api::object)
        """

    def extend(self, arg2: object) -> None:
        """
        extend( (RoutingChannelVector)arg1, (object)arg2) -> None :

            C++ signature :
                void extend(std::__1::vector<NRoutingApi::TRoutingChannel, std::__1::allocator<NRoutingApi::TRoutingChannel>> {lvalue},boost::python::api::object)
        """


class RoutingType:
    """
    This class represents a routing type.
    """

    @property
    def attached_object(self) -> Any:
        """
        Live object associated with the routing type.
        """

    @property
    def category(self) -> Any:
        """
        Category of the routing type.
        """

    @property
    def display_name(self) -> str:
        """
        Display name of routing type.
        """


class RoutingTypeCategory:
    """
    Class that represent an enumeration of values for RoutingTypeCategory
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

    external = 0
    rewire = 1
    resampling = 2
    master = 3
    track = 4
    parent_group_track = 5
    none = 6
    invalid = 7


class RoutingTypeVector:
    """
    A container for returning routing types from Live.
    """

    def append(self, arg2: object) -> None:
        """
        append( (RoutingTypeVector)arg1, (object)arg2) -> None :

            C++ signature :
                void append(std::__1::vector<NRoutingApi::TRoutingType, std::__1::allocator<NRoutingApi::TRoutingType>> {lvalue},boost::python::api::object)
        """

    def extend(self, arg2: object) -> None:
        """
        extend( (RoutingTypeVector)arg1, (object)arg2) -> None :

            C++ signature :
                void extend(std::__1::vector<NRoutingApi::TRoutingType, std::__1::allocator<NRoutingApi::TRoutingType>> {lvalue},boost::python::api::object)
        """


class Track:
    """
    This class represents a track in Live. It can be either an Audio
    track, a MIDI Track, a Return Track or the Main track. The Main
    Track and at least one Audio or MIDI track will be always present.
    Return Tracks are optional.
    """

    class View:
        """
        Representing the view aspects of a Track.
        """

        def add_device_insert_mode_listener(self, listener: Callable) -> None:
            """
            add_device_insert_mode_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "device_insert_mode" has changed.

                C++ signature :
                    void add_device_insert_mode_listener(TPyViewData<ATrack>,boost::python::api::object)
            """

        def add_is_collapsed_listener(self, listener: Callable) -> None:
            """
            add_is_collapsed_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "is_collapsed" has changed.

                C++ signature :
                    void add_is_collapsed_listener(TPyViewData<ATrack>,boost::python::api::object)
            """

        def add_selected_device_listener(self, listener: Callable) -> None:
            """
            add_selected_device_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "selected_device" has changed.

                C++ signature :
                    void add_selected_device_listener(TPyViewData<ATrack>,boost::python::api::object)
            """

        def device_insert_mode_has_listener(self, listener: Callable) -> bool:
            """
            device_insert_mode_has_listener( (View)arg1, (object)arg2) -> bool :
                Returns true, if the given listener function or method is connected
                to the property "device_insert_mode".

                C++ signature :
                    bool device_insert_mode_has_listener(TPyViewData<ATrack>,boost::python::api::object)
            """

        def is_collapsed_has_listener(self, listener: Callable) -> bool:
            """
            is_collapsed_has_listener( (View)arg1, (object)arg2) -> bool :
                Returns true, if the given listener function or method is connected
                to the property "is_collapsed".

                C++ signature :
                    bool is_collapsed_has_listener(TPyViewData<ATrack>,boost::python::api::object)
            """

        def remove_device_insert_mode_listener(self, listener: Callable) -> None:
            """
            remove_device_insert_mode_listener( (View)arg1, (object)arg2) -> None :
                Remove a previously set listener function or method from
                property "device_insert_mode".

                C++ signature :
                    void remove_device_insert_mode_listener(TPyViewData<ATrack>,boost::python::api::object)
            """

        def remove_is_collapsed_listener(self, listener: Callable) -> None:
            """
            remove_is_collapsed_listener( (View)arg1, (object)arg2) -> None :
                Remove a previously set listener function or method from
                property "is_collapsed".

                C++ signature :
                    void remove_is_collapsed_listener(TPyViewData<ATrack>,boost::python::api::object)
            """

        def remove_selected_device_listener(self, listener: Callable) -> None:
            """
            remove_selected_device_listener( (View)arg1, (object)arg2) -> None :
                Remove a previously set listener function or method from
                property "selected_device".

                C++ signature :
                    void remove_selected_device_listener(TPyViewData<ATrack>,boost::python::api::object)
            """

        def select_instrument(self) -> bool:
            """
            select_instrument( (View)arg1) -> bool :
                Selects the track's instrument if it has one.

                C++ signature :
                    bool select_instrument(TPyViewData<ATrack>)
            """

        def selected_device_has_listener(self, listener: Callable) -> bool:
            """
            selected_device_has_listener( (View)arg1, (object)arg2) -> bool :
                Returns true, if the given listener function or method is connected
                to the property "selected_device".

                C++ signature :
                    bool selected_device_has_listener(TPyViewData<ATrack>,boost::python::api::object)
            """

        @property
        def canonical_parent(self) -> Any:
            """
            Get the canonical parent of the track view.
            """

        @property
        def device_insert_mode(self) -> Any:
            """
            Get/Listen the device insertion mode of the track.  By default, it will insert devices at the end, but it can be changed to make it relative to current selection.
            """

        @property
        def is_collapsed(self) -> bool:
            """
            Get/Set/Listen if the track is shown collapsed in the arranger view.
            """

        @is_collapsed.setter
        def is_collapsed(self, value: bool) -> None:
            pass

        @property
        def selected_device(self) -> Device:
            """
            Get/Set/Listen the insertion mode of the device.  While in insertion mode, loading new devices from the browser will place devices at the selected position.
            """

        @selected_device.setter
        def selected_device(self, value: Device) -> None:
            pass

    class monitoring_states:
        """
        Class that represent an enumeration of values for monitoring_states
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

        IN = 0
        AUTO = 1
        OFF = 2

    def add_arm_listener(self, listener: Callable) -> None:
        """
        add_arm_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "arm" has changed.

            C++ signature :
                void add_arm_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_arrangement_clips_listener(self, listener: Callable) -> None:
        """
        add_arrangement_clips_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "arrangement_clips" has changed.

            C++ signature :
                void add_arrangement_clips_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_available_input_routing_channels_listener(self, listener: Callable) -> None:
        """
        add_available_input_routing_channels_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "available_input_routing_channels" has changed.

            C++ signature :
                void add_available_input_routing_channels_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_available_input_routing_types_listener(self, listener: Callable) -> None:
        """
        add_available_input_routing_types_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "available_input_routing_types" has changed.

            C++ signature :
                void add_available_input_routing_types_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_available_output_routing_channels_listener(self, listener: Callable) -> None:
        """
        add_available_output_routing_channels_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "available_output_routing_channels" has changed.

            C++ signature :
                void add_available_output_routing_channels_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_available_output_routing_types_listener(self, listener: Callable) -> None:
        """
        add_available_output_routing_types_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "available_output_routing_types" has changed.

            C++ signature :
                void add_available_output_routing_types_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_back_to_arranger_listener(self, listener: Callable) -> None:
        """
        add_back_to_arranger_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "back_to_arranger" has changed.

            C++ signature :
                void add_back_to_arranger_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_clip_slots_listener(self, listener: Callable) -> None:
        """
        add_clip_slots_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "clip_slots" has changed.

            C++ signature :
                void add_clip_slots_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_color_index_listener(self, listener: Callable) -> None:
        """
        add_color_index_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "color_index" has changed.

            C++ signature :
                void add_color_index_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_color_listener(self, listener: Callable) -> None:
        """
        add_color_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "color" has changed.

            C++ signature :
                void add_color_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_current_input_routing_listener(self, listener: Callable) -> None:
        """
        add_current_input_routing_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "current_input_routing" has changed.

            C++ signature :
                void add_current_input_routing_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_current_input_sub_routing_listener(self, listener: Callable) -> None:
        """
        add_current_input_sub_routing_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "current_input_sub_routing" has changed.

            C++ signature :
                void add_current_input_sub_routing_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_current_monitoring_state_listener(self, listener: Callable) -> None:
        """
        add_current_monitoring_state_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "current_monitoring_state" has changed.

            C++ signature :
                void add_current_monitoring_state_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_current_output_routing_listener(self, listener: Callable) -> None:
        """
        add_current_output_routing_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "current_output_routing" has changed.

            C++ signature :
                void add_current_output_routing_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_current_output_sub_routing_listener(self, listener: Callable) -> None:
        """
        add_current_output_sub_routing_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "current_output_sub_routing" has changed.

            C++ signature :
                void add_current_output_sub_routing_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_data_listener(self, listener: Callable) -> None:
        """
        add_data_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "data" has changed.

            C++ signature :
                void add_data_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_devices_listener(self, listener: Callable) -> None:
        """
        add_devices_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "devices" has changed.

            C++ signature :
                void add_devices_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_fired_slot_index_listener(self, listener: Callable) -> None:
        """
        add_fired_slot_index_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "fired_slot_index" has changed.

            C++ signature :
                void add_fired_slot_index_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_has_audio_input_listener(self, listener: Callable) -> None:
        """
        add_has_audio_input_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "has_audio_input" has changed.

            C++ signature :
                void add_has_audio_input_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_has_audio_output_listener(self, listener: Callable) -> None:
        """
        add_has_audio_output_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "has_audio_output" has changed.

            C++ signature :
                void add_has_audio_output_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_has_midi_input_listener(self, listener: Callable) -> None:
        """
        add_has_midi_input_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "has_midi_input" has changed.

            C++ signature :
                void add_has_midi_input_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_has_midi_output_listener(self, listener: Callable) -> None:
        """
        add_has_midi_output_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "has_midi_output" has changed.

            C++ signature :
                void add_has_midi_output_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_implicit_arm_listener(self, listener: Callable) -> None:
        """
        add_implicit_arm_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "implicit_arm" has changed.

            C++ signature :
                void add_implicit_arm_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_input_meter_left_listener(self, listener: Callable) -> None:
        """
        add_input_meter_left_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "input_meter_left" has changed.

            C++ signature :
                void add_input_meter_left_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_input_meter_level_listener(self, listener: Callable) -> None:
        """
        add_input_meter_level_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "input_meter_level" has changed.

            C++ signature :
                void add_input_meter_level_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_input_meter_right_listener(self, listener: Callable) -> None:
        """
        add_input_meter_right_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "input_meter_right" has changed.

            C++ signature :
                void add_input_meter_right_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_input_routing_channel_listener(self, listener: Callable) -> None:
        """
        add_input_routing_channel_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "input_routing_channel" has changed.

            C++ signature :
                void add_input_routing_channel_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_input_routing_type_listener(self, listener: Callable) -> None:
        """
        add_input_routing_type_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "input_routing_type" has changed.

            C++ signature :
                void add_input_routing_type_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_input_routings_listener(self, listener: Callable) -> None:
        """
        add_input_routings_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "input_routings" has changed.

            C++ signature :
                void add_input_routings_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_input_sub_routings_listener(self, listener: Callable) -> None:
        """
        add_input_sub_routings_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "input_sub_routings" has changed.

            C++ signature :
                void add_input_sub_routings_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_is_frozen_listener(self, listener: Callable) -> None:
        """
        add_is_frozen_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "is_frozen" has changed.

            C++ signature :
                void add_is_frozen_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_is_showing_chains_listener(self, listener: Callable) -> None:
        """
        add_is_showing_chains_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "is_showing_chains" has changed.

            C++ signature :
                void add_is_showing_chains_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_mute_listener(self, listener: Callable) -> None:
        """
        add_mute_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "mute" has changed.

            C++ signature :
                void add_mute_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_muted_via_solo_listener(self, listener: Callable) -> None:
        """
        add_muted_via_solo_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "muted_via_solo" has changed.

            C++ signature :
                void add_muted_via_solo_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_name_listener(self, listener: Callable) -> None:
        """
        add_name_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "name" has changed.

            C++ signature :
                void add_name_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_output_meter_left_listener(self, listener: Callable) -> None:
        """
        add_output_meter_left_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "output_meter_left" has changed.

            C++ signature :
                void add_output_meter_left_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_output_meter_level_listener(self, listener: Callable) -> None:
        """
        add_output_meter_level_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "output_meter_level" has changed.

            C++ signature :
                void add_output_meter_level_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_output_meter_right_listener(self, listener: Callable) -> None:
        """
        add_output_meter_right_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "output_meter_right" has changed.

            C++ signature :
                void add_output_meter_right_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_output_routing_channel_listener(self, listener: Callable) -> None:
        """
        add_output_routing_channel_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "output_routing_channel" has changed.

            C++ signature :
                void add_output_routing_channel_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_output_routing_type_listener(self, listener: Callable) -> None:
        """
        add_output_routing_type_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "output_routing_type" has changed.

            C++ signature :
                void add_output_routing_type_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_output_routings_listener(self, listener: Callable) -> None:
        """
        add_output_routings_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "output_routings" has changed.

            C++ signature :
                void add_output_routings_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_output_sub_routings_listener(self, listener: Callable) -> None:
        """
        add_output_sub_routings_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "output_sub_routings" has changed.

            C++ signature :
                void add_output_sub_routings_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_performance_impact_listener(self, listener: Callable) -> None:
        """
        add_performance_impact_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "performance_impact" has changed.

            C++ signature :
                void add_performance_impact_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_playing_slot_index_listener(self, listener: Callable) -> None:
        """
        add_playing_slot_index_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "playing_slot_index" has changed.

            C++ signature :
                void add_playing_slot_index_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_solo_listener(self, listener: Callable) -> None:
        """
        add_solo_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "solo" has changed.

            C++ signature :
                void add_solo_listener(TTrackPyHandle,boost::python::api::object)
        """

    def add_take_lanes_listener(self, listener: Callable) -> None:
        """
        add_take_lanes_listener( (Track)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "take_lanes" has changed.

            C++ signature :
                void add_take_lanes_listener(TTrackPyHandle,boost::python::api::object)
        """

    def arm_has_listener(self, listener: Callable) -> bool:
        """
        arm_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "arm".

            C++ signature :
                bool arm_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def arrangement_clips_has_listener(self, listener: Callable) -> bool:
        """
        arrangement_clips_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "arrangement_clips".

            C++ signature :
                bool arrangement_clips_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def available_input_routing_channels_has_listener(self, listener: Callable) -> bool:
        """
        available_input_routing_channels_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "available_input_routing_channels".

            C++ signature :
                bool available_input_routing_channels_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def available_input_routing_types_has_listener(self, listener: Callable) -> bool:
        """
        available_input_routing_types_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "available_input_routing_types".

            C++ signature :
                bool available_input_routing_types_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def available_output_routing_channels_has_listener(self, listener: Callable) -> bool:
        """
        available_output_routing_channels_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "available_output_routing_channels".

            C++ signature :
                bool available_output_routing_channels_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def available_output_routing_types_has_listener(self, listener: Callable) -> bool:
        """
        available_output_routing_types_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "available_output_routing_types".

            C++ signature :
                bool available_output_routing_types_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def back_to_arranger_has_listener(self, listener: Callable) -> bool:
        """
        back_to_arranger_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "back_to_arranger".

            C++ signature :
                bool back_to_arranger_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def clip_slots_has_listener(self, listener: Callable) -> bool:
        """
        clip_slots_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "clip_slots".

            C++ signature :
                bool clip_slots_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def color_has_listener(self, listener: Callable) -> bool:
        """
        color_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "color".

            C++ signature :
                bool color_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def color_index_has_listener(self, listener: Callable) -> bool:
        """
        color_index_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "color_index".

            C++ signature :
                bool color_index_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def create_audio_clip(self, arg2: object, arg3: float) -> Clip:
        """
        create_audio_clip( (Track)arg1, (object)arg2, (float)arg3) -> Clip :
            Creates an audio clip referencing the file at the given path and inserts it into the arrangement at the specified time.
            Throws an error when called on a non-audio or a frozen track, when the specified time is outside the [0., 1576800.] range, when the track is currently being recorded into, or when the path doesn't point to a valid audio file.

            C++ signature :
                TWeakPtr<TPyHandle<AClip>> create_audio_clip(TTrackPyHandle,TString,double)
        """

    def create_midi_clip(self, arg2: float, arg3: float) -> Clip:
        """
        create_midi_clip( (Track)arg1, (float)arg2, (float)arg3) -> Clip :
            Creates an empty MIDI clip and inserts it into the arrangement at the specified time.
            Throws an error when called on a non-MIDI track or a frozen track, when the specified time is outside the [0., 1576800.] range, or when the track is currently being recorded into.

            C++ signature :
                TWeakPtr<TPyHandle<AClip>> create_midi_clip(TTrackPyHandle,double,double)
        """

    def create_take_lane(self) -> LomObject:
        """
        create_take_lane( (Track)arg1) -> LomObject :
            Create a new TakeLane for this track.

            C++ signature :
                TWeakPtr<TPyHandleBase> create_take_lane(TTrackPyHandle)
        """

    def current_input_routing_has_listener(self, listener: Callable) -> bool:
        """
        current_input_routing_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "current_input_routing".

            C++ signature :
                bool current_input_routing_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def current_input_sub_routing_has_listener(self, listener: Callable) -> bool:
        """
        current_input_sub_routing_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "current_input_sub_routing".

            C++ signature :
                bool current_input_sub_routing_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def current_monitoring_state_has_listener(self, listener: Callable) -> bool:
        """
        current_monitoring_state_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "current_monitoring_state".

            C++ signature :
                bool current_monitoring_state_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def current_output_routing_has_listener(self, listener: Callable) -> bool:
        """
        current_output_routing_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "current_output_routing".

            C++ signature :
                bool current_output_routing_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def current_output_sub_routing_has_listener(self, listener: Callable) -> bool:
        """
        current_output_sub_routing_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "current_output_sub_routing".

            C++ signature :
                bool current_output_sub_routing_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def data_has_listener(self, listener: Callable) -> bool:
        """
        data_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "data".

            C++ signature :
                bool data_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def delete_clip(self, arg2: object) -> None:
        """
        delete_clip( (Track)arg1, (Clip)arg2) -> None :
            Delete the given clip. Raises a runtime error when the clip belongs to another track.

            C++ signature :
                void delete_clip(TTrackPyHandle,TPyHandle<AClip>)
        """

    def delete_device(self, arg2: int) -> None:
        """
        delete_device( (Track)arg1, (int)arg2) -> None :
            Delete a device identified by the index in the 'devices' list.

            C++ signature :
                void delete_device(TTrackPyHandle,int)
        """

    def devices_has_listener(self, listener: Callable) -> bool:
        """
        devices_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "devices".

            C++ signature :
                bool devices_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def duplicate_clip_slot(self, arg2: int) -> int:
        """
        duplicate_clip_slot( (Track)arg1, (int)arg2) -> int :
            Duplicate a clip and put it into the next free slot and return the index
            of the destination slot. A new scene is created if no free slot is
            available. If creating the new scene would exceed the limitations,
            a runtime error is raised.

            C++ signature :
                int duplicate_clip_slot(TTrackPyHandle,int)
        """

    def duplicate_clip_to_arrangement(self, clip: object, destination_time: float) -> Clip:
        """
        duplicate_clip_to_arrangement( (Track)self, (Clip)clip, (float)destination_time) -> Clip :
            Duplicate the given clip into the arrangement of this track at the provided
            destination time and return it. When the type of the clip and the type of the
            track are incompatible, a runtime error is raised.

            C++ signature :
                TWeakPtr<TPyHandle<AClip>> duplicate_clip_to_arrangement(TTrackPyHandle,TPyHandle<AClip>,double)
        """

    def duplicate_device(self, arg2: int) -> None:
        """
        duplicate_device( (Track)arg1, (int)arg2) -> None :
            Duplicate a device at a given index in the 'devices' list.

            C++ signature :
                void duplicate_device(TTrackPyHandle,int)
        """

    def fired_slot_index_has_listener(self, listener: Callable) -> bool:
        """
        fired_slot_index_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "fired_slot_index".

            C++ signature :
                bool fired_slot_index_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def get_data(self, key: object, default_value: object) -> object:
        """
        get_data( (Track)arg1, (object)key, (object)default_value) -> object :
            Get data for the given key, that was previously stored using set_data.

            C++ signature :
                boost::python::api::object get_data(TTrackPyHandle,TString,boost::python::api::object)
        """

    def has_audio_input_has_listener(self, listener: Callable) -> bool:
        """
        has_audio_input_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "has_audio_input".

            C++ signature :
                bool has_audio_input_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def has_audio_output_has_listener(self, listener: Callable) -> bool:
        """
        has_audio_output_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "has_audio_output".

            C++ signature :
                bool has_audio_output_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def has_midi_input_has_listener(self, listener: Callable) -> bool:
        """
        has_midi_input_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "has_midi_input".

            C++ signature :
                bool has_midi_input_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def has_midi_output_has_listener(self, listener: Callable) -> bool:
        """
        has_midi_output_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "has_midi_output".

            C++ signature :
                bool has_midi_output_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def implicit_arm_has_listener(self, listener: Callable) -> bool:
        """
        implicit_arm_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "implicit_arm".

            C++ signature :
                bool implicit_arm_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def input_meter_left_has_listener(self, listener: Callable) -> bool:
        """
        input_meter_left_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "input_meter_left".

            C++ signature :
                bool input_meter_left_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def input_meter_level_has_listener(self, listener: Callable) -> bool:
        """
        input_meter_level_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "input_meter_level".

            C++ signature :
                bool input_meter_level_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def input_meter_right_has_listener(self, listener: Callable) -> bool:
        """
        input_meter_right_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "input_meter_right".

            C++ signature :
                bool input_meter_right_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def input_routing_channel_has_listener(self, listener: Callable) -> bool:
        """
        input_routing_channel_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "input_routing_channel".

            C++ signature :
                bool input_routing_channel_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def input_routing_type_has_listener(self, listener: Callable) -> bool:
        """
        input_routing_type_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "input_routing_type".

            C++ signature :
                bool input_routing_type_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def input_routings_has_listener(self, listener: Callable) -> bool:
        """
        input_routings_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "input_routings".

            C++ signature :
                bool input_routings_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def input_sub_routings_has_listener(self, listener: Callable) -> bool:
        """
        input_sub_routings_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "input_sub_routings".

            C++ signature :
                bool input_sub_routings_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def insert_device(self, DeviceName: str, DeviceIndex: int = 0) -> LomObject:
        """
        insert_device( (Track)arg1, (str)DeviceName [, (int)DeviceIndex=-1]) -> LomObject :
            Add a device at a given index in the 'devices' list. At end if -1.

            C++ signature :
                TWeakPtr<TPyHandleBase> insert_device(TTrackPyHandle,std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>> [,int=-1])
        """

    def is_frozen_has_listener(self, listener: Callable) -> bool:
        """
        is_frozen_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "is_frozen".

            C++ signature :
                bool is_frozen_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def is_showing_chains_has_listener(self, listener: Callable) -> bool:
        """
        is_showing_chains_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "is_showing_chains".

            C++ signature :
                bool is_showing_chains_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def jump_in_running_session_clip(self, arg2: float) -> None:
        """
        jump_in_running_session_clip( (Track)arg1, (float)arg2) -> None :
            Jump forward or backward in the currently running Sessionclip (if any)
            by the specified relative amount in beats. Does nothing if no Session Clip
            is currently running.

            C++ signature :
                void jump_in_running_session_clip(TTrackPyHandle,double)
        """

    def mute_has_listener(self, listener: Callable) -> bool:
        """
        mute_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "mute".

            C++ signature :
                bool mute_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def muted_via_solo_has_listener(self, listener: Callable) -> bool:
        """
        muted_via_solo_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "muted_via_solo".

            C++ signature :
                bool muted_via_solo_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def name_has_listener(self, listener: Callable) -> bool:
        """
        name_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "name".

            C++ signature :
                bool name_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def output_meter_left_has_listener(self, listener: Callable) -> bool:
        """
        output_meter_left_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "output_meter_left".

            C++ signature :
                bool output_meter_left_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def output_meter_level_has_listener(self, listener: Callable) -> bool:
        """
        output_meter_level_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "output_meter_level".

            C++ signature :
                bool output_meter_level_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def output_meter_right_has_listener(self, listener: Callable) -> bool:
        """
        output_meter_right_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "output_meter_right".

            C++ signature :
                bool output_meter_right_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def output_routing_channel_has_listener(self, listener: Callable) -> bool:
        """
        output_routing_channel_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "output_routing_channel".

            C++ signature :
                bool output_routing_channel_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def output_routing_type_has_listener(self, listener: Callable) -> bool:
        """
        output_routing_type_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "output_routing_type".

            C++ signature :
                bool output_routing_type_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def output_routings_has_listener(self, listener: Callable) -> bool:
        """
        output_routings_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "output_routings".

            C++ signature :
                bool output_routings_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def output_sub_routings_has_listener(self, listener: Callable) -> bool:
        """
        output_sub_routings_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "output_sub_routings".

            C++ signature :
                bool output_sub_routings_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def performance_impact_has_listener(self, listener: Callable) -> bool:
        """
        performance_impact_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "performance_impact".

            C++ signature :
                bool performance_impact_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def playing_slot_index_has_listener(self, listener: Callable) -> bool:
        """
        playing_slot_index_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "playing_slot_index".

            C++ signature :
                bool playing_slot_index_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_arm_listener(self, listener: Callable) -> None:
        """
        remove_arm_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "arm".

            C++ signature :
                void remove_arm_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_arrangement_clips_listener(self, listener: Callable) -> None:
        """
        remove_arrangement_clips_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "arrangement_clips".

            C++ signature :
                void remove_arrangement_clips_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_available_input_routing_channels_listener(self, listener: Callable) -> None:
        """
        remove_available_input_routing_channels_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "available_input_routing_channels".

            C++ signature :
                void remove_available_input_routing_channels_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_available_input_routing_types_listener(self, listener: Callable) -> None:
        """
        remove_available_input_routing_types_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "available_input_routing_types".

            C++ signature :
                void remove_available_input_routing_types_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_available_output_routing_channels_listener(self, listener: Callable) -> None:
        """
        remove_available_output_routing_channels_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "available_output_routing_channels".

            C++ signature :
                void remove_available_output_routing_channels_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_available_output_routing_types_listener(self, listener: Callable) -> None:
        """
        remove_available_output_routing_types_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "available_output_routing_types".

            C++ signature :
                void remove_available_output_routing_types_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_back_to_arranger_listener(self, listener: Callable) -> None:
        """
        remove_back_to_arranger_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "back_to_arranger".

            C++ signature :
                void remove_back_to_arranger_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_clip_slots_listener(self, listener: Callable) -> None:
        """
        remove_clip_slots_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "clip_slots".

            C++ signature :
                void remove_clip_slots_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_color_index_listener(self, listener: Callable) -> None:
        """
        remove_color_index_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "color_index".

            C++ signature :
                void remove_color_index_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_color_listener(self, listener: Callable) -> None:
        """
        remove_color_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "color".

            C++ signature :
                void remove_color_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_current_input_routing_listener(self, listener: Callable) -> None:
        """
        remove_current_input_routing_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "current_input_routing".

            C++ signature :
                void remove_current_input_routing_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_current_input_sub_routing_listener(self, listener: Callable) -> None:
        """
        remove_current_input_sub_routing_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "current_input_sub_routing".

            C++ signature :
                void remove_current_input_sub_routing_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_current_monitoring_state_listener(self, listener: Callable) -> None:
        """
        remove_current_monitoring_state_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "current_monitoring_state".

            C++ signature :
                void remove_current_monitoring_state_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_current_output_routing_listener(self, listener: Callable) -> None:
        """
        remove_current_output_routing_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "current_output_routing".

            C++ signature :
                void remove_current_output_routing_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_current_output_sub_routing_listener(self, listener: Callable) -> None:
        """
        remove_current_output_sub_routing_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "current_output_sub_routing".

            C++ signature :
                void remove_current_output_sub_routing_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_data_listener(self, listener: Callable) -> None:
        """
        remove_data_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "data".

            C++ signature :
                void remove_data_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_devices_listener(self, listener: Callable) -> None:
        """
        remove_devices_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "devices".

            C++ signature :
                void remove_devices_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_fired_slot_index_listener(self, listener: Callable) -> None:
        """
        remove_fired_slot_index_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "fired_slot_index".

            C++ signature :
                void remove_fired_slot_index_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_has_audio_input_listener(self, listener: Callable) -> None:
        """
        remove_has_audio_input_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "has_audio_input".

            C++ signature :
                void remove_has_audio_input_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_has_audio_output_listener(self, listener: Callable) -> None:
        """
        remove_has_audio_output_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "has_audio_output".

            C++ signature :
                void remove_has_audio_output_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_has_midi_input_listener(self, listener: Callable) -> None:
        """
        remove_has_midi_input_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "has_midi_input".

            C++ signature :
                void remove_has_midi_input_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_has_midi_output_listener(self, listener: Callable) -> None:
        """
        remove_has_midi_output_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "has_midi_output".

            C++ signature :
                void remove_has_midi_output_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_implicit_arm_listener(self, listener: Callable) -> None:
        """
        remove_implicit_arm_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "implicit_arm".

            C++ signature :
                void remove_implicit_arm_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_input_meter_left_listener(self, listener: Callable) -> None:
        """
        remove_input_meter_left_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "input_meter_left".

            C++ signature :
                void remove_input_meter_left_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_input_meter_level_listener(self, listener: Callable) -> None:
        """
        remove_input_meter_level_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "input_meter_level".

            C++ signature :
                void remove_input_meter_level_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_input_meter_right_listener(self, listener: Callable) -> None:
        """
        remove_input_meter_right_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "input_meter_right".

            C++ signature :
                void remove_input_meter_right_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_input_routing_channel_listener(self, listener: Callable) -> None:
        """
        remove_input_routing_channel_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "input_routing_channel".

            C++ signature :
                void remove_input_routing_channel_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_input_routing_type_listener(self, listener: Callable) -> None:
        """
        remove_input_routing_type_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "input_routing_type".

            C++ signature :
                void remove_input_routing_type_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_input_routings_listener(self, listener: Callable) -> None:
        """
        remove_input_routings_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "input_routings".

            C++ signature :
                void remove_input_routings_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_input_sub_routings_listener(self, listener: Callable) -> None:
        """
        remove_input_sub_routings_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "input_sub_routings".

            C++ signature :
                void remove_input_sub_routings_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_is_frozen_listener(self, listener: Callable) -> None:
        """
        remove_is_frozen_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "is_frozen".

            C++ signature :
                void remove_is_frozen_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_is_showing_chains_listener(self, listener: Callable) -> None:
        """
        remove_is_showing_chains_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "is_showing_chains".

            C++ signature :
                void remove_is_showing_chains_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_mute_listener(self, listener: Callable) -> None:
        """
        remove_mute_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "mute".

            C++ signature :
                void remove_mute_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_muted_via_solo_listener(self, listener: Callable) -> None:
        """
        remove_muted_via_solo_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "muted_via_solo".

            C++ signature :
                void remove_muted_via_solo_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_name_listener(self, listener: Callable) -> None:
        """
        remove_name_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "name".

            C++ signature :
                void remove_name_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_output_meter_left_listener(self, listener: Callable) -> None:
        """
        remove_output_meter_left_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "output_meter_left".

            C++ signature :
                void remove_output_meter_left_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_output_meter_level_listener(self, listener: Callable) -> None:
        """
        remove_output_meter_level_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "output_meter_level".

            C++ signature :
                void remove_output_meter_level_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_output_meter_right_listener(self, listener: Callable) -> None:
        """
        remove_output_meter_right_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "output_meter_right".

            C++ signature :
                void remove_output_meter_right_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_output_routing_channel_listener(self, listener: Callable) -> None:
        """
        remove_output_routing_channel_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "output_routing_channel".

            C++ signature :
                void remove_output_routing_channel_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_output_routing_type_listener(self, listener: Callable) -> None:
        """
        remove_output_routing_type_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "output_routing_type".

            C++ signature :
                void remove_output_routing_type_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_output_routings_listener(self, listener: Callable) -> None:
        """
        remove_output_routings_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "output_routings".

            C++ signature :
                void remove_output_routings_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_output_sub_routings_listener(self, listener: Callable) -> None:
        """
        remove_output_sub_routings_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "output_sub_routings".

            C++ signature :
                void remove_output_sub_routings_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_performance_impact_listener(self, listener: Callable) -> None:
        """
        remove_performance_impact_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "performance_impact".

            C++ signature :
                void remove_performance_impact_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_playing_slot_index_listener(self, listener: Callable) -> None:
        """
        remove_playing_slot_index_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "playing_slot_index".

            C++ signature :
                void remove_playing_slot_index_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_solo_listener(self, listener: Callable) -> None:
        """
        remove_solo_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "solo".

            C++ signature :
                void remove_solo_listener(TTrackPyHandle,boost::python::api::object)
        """

    def remove_take_lanes_listener(self, listener: Callable) -> None:
        """
        remove_take_lanes_listener( (Track)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "take_lanes".

            C++ signature :
                void remove_take_lanes_listener(TTrackPyHandle,boost::python::api::object)
        """

    def set_data(self, key: object, value: object) -> None:
        """
        set_data( (Track)arg1, (object)key, (object)value) -> None :
            Store data for the given key in this object. The data is persistent and will be restored when loading the Live Set.

            C++ signature :
                void set_data(TTrackPyHandle,TString,boost::python::api::object)
        """

    def solo_has_listener(self, listener: Callable) -> bool:
        """
        solo_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "solo".

            C++ signature :
                bool solo_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    def stop_all_clips(self, Quantized: bool = True) -> None:
        """
        stop_all_clips( (Track)arg1 [, (bool)Quantized=True]) -> None :
            Stop running and triggered clip and slots on this track.

            C++ signature :
                void stop_all_clips(TTrackPyHandle [,bool=True])
        """

    def take_lanes_has_listener(self, listener: Callable) -> bool:
        """
        take_lanes_has_listener( (Track)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "take_lanes".

            C++ signature :
                bool take_lanes_has_listener(TTrackPyHandle,boost::python::api::object)
        """

    @property
    def arm(self) -> Any:
        """
        Arm the track for recording. Not available for Main- and Send Tracks.
        """

    @property
    def arrangement_clips(self) -> list[Clip]:
        """
        const access to the list of clips in arrangement viewThe list will be empty for the main, send and group tracks.
        """

    @property
    def available_input_routing_channels(self) -> Any:
        """
        Return a list of source channels for input routing.
        """

    @property
    def available_input_routing_types(self) -> Any:
        """
        Return a list of source types for input routing.
        """

    @property
    def available_output_routing_channels(self) -> Any:
        """
        Return a list of destination channels for output routing.
        """

    @property
    def available_output_routing_types(self) -> Any:
        """
        Return a list of destination types for output routing.
        """

    @property
    def back_to_arranger(self) -> Any:
        """
        Indicates if it's possible to go back to playing back the clips in the Arranger.Setting a value 0 will go back to the Arranger playback. Setting on grouptracks will go back to the Arranger on all grouped tracks.
        """

    @property
    def can_be_armed(self) -> bool:
        """
        return True, if this Track has a valid arm property. Not all tracks
        can be armed (for example return Tracks or the Main Tracks).
        """

    @property
    def can_be_frozen(self) -> bool:
        """
        return True, if this Track can be frozen.
        """

    @property
    def can_show_chains(self) -> bool:
        """
        return True, if this Track contains a rack instrument device that is capable of showing its chains in session view.
        """

    @property
    def canonical_parent(self) -> Any:
        """
        Get the canonical parent of the track.
        """

    @property
    def clip_slots(self) -> list[ClipSlot]:
        """
        const access to the list of clipslots (see class AClipSlot) for this track.
        The list will be empty for the main and sendtracks.
        """

    @property
    def color(self) -> Any:
        """
        Get/set access to the color of the Track (RGB).
        """

    @color.setter
    def color(self, value: Any) -> None:
        pass

    @property
    def color_index(self) -> Any:
        """
        Get/Set access to the color index of the track. Can be None for no color.
        """

    @color_index.setter
    def color_index(self, value: Any) -> None:
        pass

    @property
    def current_input_routing(self) -> Any:
        """
        Get/Set the name of the current active input routing.
        When setting a new routing, the new routing must be one of the available ones.
        """

    @current_input_routing.setter
    def current_input_routing(self, value: Any) -> None:
        pass

    @property
    def current_input_sub_routing(self) -> Any:
        """
        Get/Set the current active input sub routing.
        When setting a new routing, the new routing must be one of the available ones.
        """

    @current_input_sub_routing.setter
    def current_input_sub_routing(self, value: Any) -> None:
        pass

    @property
    def current_monitoring_state(self) -> Any:
        """
        Get/Set the track's current monitoring state.
        """

    @current_monitoring_state.setter
    def current_monitoring_state(self, value: Any) -> None:
        pass

    @property
    def current_output_routing(self) -> Any:
        """
        Get/Set the current active output routing.
        When setting a new routing, the new routing must be one of the available ones.
        """

    @current_output_routing.setter
    def current_output_routing(self, value: Any) -> None:
        pass

    @property
    def current_output_sub_routing(self) -> Any:
        """
        Get/Set the current active output sub routing.
        When setting a new routing, the new routing must be one of the available ones.
        """

    @current_output_sub_routing.setter
    def current_output_sub_routing(self, value: Any) -> None:
        pass

    @property
    def devices(self) -> list[Device]:
        """
        Return const access to all available Devices that are present in the Tracks
        Devicechain. This tuple will also include the 'mixer_device' that every Track
        always has.
        """

    @property
    def fired_slot_index(self) -> Any:
        """
        const access to the index of the fired (and thus blinking) clipslot in this track.
        This index is -1 if no slot is fired and -2 if the track's stop button has been fired.
        """

    @property
    def fold_state(self) -> Any:
        """
        Get/Set whether the track is folded or not. Only available if is_foldable is True.
        """

    @fold_state.setter
    def fold_state(self, value: Any) -> None:
        pass

    @property
    def group_track(self) -> Track:
        """
        return the group track if is_grouped.
        """

    @property
    def has_audio_input(self) -> bool:
        """
        return True, if this Track can be feed with an Audio signal. This is
        true for all Audio Tracks.
        """

    @property
    def has_audio_output(self) -> bool:
        """
        return True, if this Track sends out an Audio signal. This is
        true for all Audio Tracks, and MIDI tracks with an Instrument.
        """

    @property
    def has_midi_input(self) -> bool:
        """
        return True, if this Track can be feed with an Audio signal. This is
        true for all MIDI Tracks.
        """

    @property
    def has_midi_output(self) -> bool:
        """
        return True, if this Track sends out MIDI events. This is
        true for all MIDI Tracks with no Instruments.
        """

    @property
    def implicit_arm(self) -> Any:
        """
        Arm the track for recording. When The track is implicitly armed, it showsin a weaker color in the live GUI and is not saved in the set.
        """

    @property
    def input_meter_left(self) -> Any:
        """
        Momentary value of left input channel meter, 0.0 to 1.0. For Audio Tracks only.
        """

    @property
    def input_meter_level(self) -> Any:
        """
        Return the MIDI or Audio meter value of the Tracks input, depending on the
        type of the Track input. Meter values (MIDI or Audio) are always scaled
        from 0.0 to 1.0.
        """

    @property
    def input_meter_right(self) -> Any:
        """
        Momentary value of right input channel meter, 0.0 to 1.0. For Audio Tracks only.
        """

    @property
    def input_routing_channel(self) -> Any:
        """
        Get and set the current source channel for input routing.
        Raises ValueError if the type isn't one of the current values in
        available_input_routing_channels.
        """

    @property
    def input_routing_type(self) -> Any:
        """
        Get and set the current source type for input routing.
        Raises ValueError if the type isn't one of the current values in
        available_input_routing_types.
        """

    @property
    def input_routings(self) -> Any:
        """
        Const access to the list of available input routings.
        """

    @property
    def input_sub_routings(self) -> Any:
        """
        Return a list of all available input sub routings.
        """

    @property
    def is_foldable(self) -> bool:
        """
        return True if the track can be (un)folded to hide/reveal contained tracks.
        """

    @property
    def is_frozen(self) -> bool:
        """
        return True if this Track is currently frozen. No changes should be applied to the track's devices or clips while it is frozen.
        """

    @property
    def is_grouped(self) -> bool:
        """
        return True if this Track is current part of a group track.
        """

    @property
    def is_part_of_selection(self) -> bool:
        """
        return False if the track is not selected.
        """

    @property
    def is_showing_chains(self) -> bool:
        """
        Get/Set whether a track with a rack device is showing its chains in session view.
        """

    @is_showing_chains.setter
    def is_showing_chains(self, value: bool) -> None:
        pass

    @property
    def is_visible(self) -> bool:
        """
        return False if the track is hidden within a folded group track.
        """

    @property
    def mixer_device(self) -> Device:
        """
        Return access to the special Device that every Track has: This Device contains
        the Volume, Pan, Sendamounts, and Crossfade assignment parameters.
        """

    @property
    def mute(self) -> Any:
        """
        Mute/unmute the track.
        """

    @property
    def muted_via_solo(self) -> Any:
        """
        Returns true if the track is muted because another track is soloed.
        """

    @property
    def name(self) -> str:
        """
        Read/write access to the name of the Track, as visible in the track header.
        """

    @name.setter
    def name(self, value: str) -> None:
        pass

    @property
    def output_meter_left(self) -> Any:
        """
        Momentary value of left output channel meter, 0.0 to 1.0.
        For tracks with audio output only.
        """

    @property
    def output_meter_level(self) -> Any:
        """
        Return the MIDI or Audio meter value of the Track output (behind the
        mixer_device), depending on the type of the Track input, this can be a MIDI
        or Audio meter. Meter values (MIDI or Audio) are always scaled from 0.0 to 1.0.
        """

    @property
    def output_meter_right(self) -> Any:
        """
        Momentary value of right output channel meter, 0.0 to 1.0.
        For tracks with audio output only.
        """

    @property
    def output_routing_channel(self) -> Any:
        """
        Get and set the current destination channel for output routing.
        Raises ValueError if the channel isn't one of the current values in
        available_output_routing_channels.
        """

    @property
    def output_routing_type(self) -> Any:
        """
        Get and set the current destination type for output routing.
        Raises ValueError if the type isn't one of the current values in
        available_output_routing_types.
        """

    @property
    def output_routings(self) -> Any:
        """
        Const access to the list of all available output routings.
        """

    @property
    def output_sub_routings(self) -> Any:
        """
        Return a list of all available output sub routings.
        """

    @property
    def performance_impact(self) -> Any:
        """
        Reports the performance impact of this track.
        """

    @property
    def playing_slot_index(self) -> Any:
        """
        const access to the index of the currently playing clip in the track.
        Will be -1 when no clip is playing.
        """

    @property
    def solo(self) -> Any:
        """
        Get/Set the solo status of the track. Note that this will not disable the
        solo state of any other track. If you want exclusive solo, you have to
        disable the solo state of the other Tracks manually.
        """

    @solo.setter
    def solo(self, value: Any) -> None:
        pass

    @property
    def take_lanes(self) -> Any:
        """
        returns the take lanes.
        """

    @property
    def view(self) -> View:
        """
        Representing the view aspects of a Track.
        """

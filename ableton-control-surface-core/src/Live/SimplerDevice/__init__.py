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
from Live.Song import *
from Live.SpectralResonatorDevice import *
from Live.Track import *
from Live.WavetableDevice import *


class PlaybackMode:
    """
    Class that represent an enumeration of values for PlaybackMode
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

    classic = 0
    one_shot = 1
    slicing = 2


class SimplerDevice:
    """
    This class represents a Simpler device.
    """

    class View:
        """
        Representing the view aspects of a simpler device.
        """

        def add_is_collapsed_listener(self, listener: Callable) -> None:
            """
            add_is_collapsed_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "is_collapsed" has changed.

                C++ signature :
                    void add_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
            """

        def add_sample_end_listener(self, listener: Callable) -> None:
            """
            add_sample_end_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "sample_end" has changed.

                C++ signature :
                    void add_sample_end_listener(TSimplerDevicePyViewData,boost::python::api::object)
            """

        def add_sample_env_fade_in_listener(self, listener: Callable) -> None:
            """
            add_sample_env_fade_in_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "sample_env_fade_in" has changed.

                C++ signature :
                    void add_sample_env_fade_in_listener(TSimplerDevicePyViewData,boost::python::api::object)
            """

        def add_sample_env_fade_out_listener(self, listener: Callable) -> None:
            """
            add_sample_env_fade_out_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "sample_env_fade_out" has changed.

                C++ signature :
                    void add_sample_env_fade_out_listener(TSimplerDevicePyViewData,boost::python::api::object)
            """

        def add_sample_loop_end_listener(self, listener: Callable) -> None:
            """
            add_sample_loop_end_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "sample_loop_end" has changed.

                C++ signature :
                    void add_sample_loop_end_listener(TSimplerDevicePyViewData,boost::python::api::object)
            """

        def add_sample_loop_fade_listener(self, listener: Callable) -> None:
            """
            add_sample_loop_fade_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "sample_loop_fade" has changed.

                C++ signature :
                    void add_sample_loop_fade_listener(TSimplerDevicePyViewData,boost::python::api::object)
            """

        def add_sample_loop_start_listener(self, listener: Callable) -> None:
            """
            add_sample_loop_start_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "sample_loop_start" has changed.

                C++ signature :
                    void add_sample_loop_start_listener(TSimplerDevicePyViewData,boost::python::api::object)
            """

        def add_sample_start_listener(self, listener: Callable) -> None:
            """
            add_sample_start_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "sample_start" has changed.

                C++ signature :
                    void add_sample_start_listener(TSimplerDevicePyViewData,boost::python::api::object)
            """

        def add_selected_slice_listener(self, listener: Callable) -> None:
            """
            add_selected_slice_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "selected_slice" has changed.

                C++ signature :
                    void add_selected_slice_listener(TSimplerDevicePyViewData,boost::python::api::object)
            """

        def is_collapsed_has_listener(self, listener: Callable) -> bool:
            """
            is_collapsed_has_listener( (View)arg1, (object)arg2) -> bool :
                Returns true, if the given listener function or method is connected
                to the property "is_collapsed".

                C++ signature :
                    bool is_collapsed_has_listener(TPyViewData<ADevice>,boost::python::api::object)
            """

        def remove_is_collapsed_listener(self, listener: Callable) -> None:
            """
            remove_is_collapsed_listener( (View)arg1, (object)arg2) -> None :
                Remove a previously set listener function or method from
                property "is_collapsed".

                C++ signature :
                    void remove_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
            """

        def remove_sample_end_listener(self, listener: Callable) -> None:
            """
            remove_sample_end_listener( (View)arg1, (object)arg2) -> None :
                Remove a previously set listener function or method from
                property "sample_end".

                C++ signature :
                    void remove_sample_end_listener(TSimplerDevicePyViewData,boost::python::api::object)
            """

        def remove_sample_env_fade_in_listener(self, listener: Callable) -> None:
            """
            remove_sample_env_fade_in_listener( (View)arg1, (object)arg2) -> None :
                Remove a previously set listener function or method from
                property "sample_env_fade_in".

                C++ signature :
                    void remove_sample_env_fade_in_listener(TSimplerDevicePyViewData,boost::python::api::object)
            """

        def remove_sample_env_fade_out_listener(self, listener: Callable) -> None:
            """
            remove_sample_env_fade_out_listener( (View)arg1, (object)arg2) -> None :
                Remove a previously set listener function or method from
                property "sample_env_fade_out".

                C++ signature :
                    void remove_sample_env_fade_out_listener(TSimplerDevicePyViewData,boost::python::api::object)
            """

        def remove_sample_loop_end_listener(self, listener: Callable) -> None:
            """
            remove_sample_loop_end_listener( (View)arg1, (object)arg2) -> None :
                Remove a previously set listener function or method from
                property "sample_loop_end".

                C++ signature :
                    void remove_sample_loop_end_listener(TSimplerDevicePyViewData,boost::python::api::object)
            """

        def remove_sample_loop_fade_listener(self, listener: Callable) -> None:
            """
            remove_sample_loop_fade_listener( (View)arg1, (object)arg2) -> None :
                Remove a previously set listener function or method from
                property "sample_loop_fade".

                C++ signature :
                    void remove_sample_loop_fade_listener(TSimplerDevicePyViewData,boost::python::api::object)
            """

        def remove_sample_loop_start_listener(self, listener: Callable) -> None:
            """
            remove_sample_loop_start_listener( (View)arg1, (object)arg2) -> None :
                Remove a previously set listener function or method from
                property "sample_loop_start".

                C++ signature :
                    void remove_sample_loop_start_listener(TSimplerDevicePyViewData,boost::python::api::object)
            """

        def remove_sample_start_listener(self, listener: Callable) -> None:
            """
            remove_sample_start_listener( (View)arg1, (object)arg2) -> None :
                Remove a previously set listener function or method from
                property "sample_start".

                C++ signature :
                    void remove_sample_start_listener(TSimplerDevicePyViewData,boost::python::api::object)
            """

        def remove_selected_slice_listener(self, listener: Callable) -> None:
            """
            remove_selected_slice_listener( (View)arg1, (object)arg2) -> None :
                Remove a previously set listener function or method from
                property "selected_slice".

                C++ signature :
                    void remove_selected_slice_listener(TSimplerDevicePyViewData,boost::python::api::object)
            """

        def sample_end_has_listener(self, listener: Callable) -> bool:
            """
            sample_end_has_listener( (View)arg1, (object)arg2) -> bool :
                Returns true, if the given listener function or method is connected
                to the property "sample_end".

                C++ signature :
                    bool sample_end_has_listener(TSimplerDevicePyViewData,boost::python::api::object)
            """

        def sample_env_fade_in_has_listener(self, listener: Callable) -> bool:
            """
            sample_env_fade_in_has_listener( (View)arg1, (object)arg2) -> bool :
                Returns true, if the given listener function or method is connected
                to the property "sample_env_fade_in".

                C++ signature :
                    bool sample_env_fade_in_has_listener(TSimplerDevicePyViewData,boost::python::api::object)
            """

        def sample_env_fade_out_has_listener(self, listener: Callable) -> bool:
            """
            sample_env_fade_out_has_listener( (View)arg1, (object)arg2) -> bool :
                Returns true, if the given listener function or method is connected
                to the property "sample_env_fade_out".

                C++ signature :
                    bool sample_env_fade_out_has_listener(TSimplerDevicePyViewData,boost::python::api::object)
            """

        def sample_loop_end_has_listener(self, listener: Callable) -> bool:
            """
            sample_loop_end_has_listener( (View)arg1, (object)arg2) -> bool :
                Returns true, if the given listener function or method is connected
                to the property "sample_loop_end".

                C++ signature :
                    bool sample_loop_end_has_listener(TSimplerDevicePyViewData,boost::python::api::object)
            """

        def sample_loop_fade_has_listener(self, listener: Callable) -> bool:
            """
            sample_loop_fade_has_listener( (View)arg1, (object)arg2) -> bool :
                Returns true, if the given listener function or method is connected
                to the property "sample_loop_fade".

                C++ signature :
                    bool sample_loop_fade_has_listener(TSimplerDevicePyViewData,boost::python::api::object)
            """

        def sample_loop_start_has_listener(self, listener: Callable) -> bool:
            """
            sample_loop_start_has_listener( (View)arg1, (object)arg2) -> bool :
                Returns true, if the given listener function or method is connected
                to the property "sample_loop_start".

                C++ signature :
                    bool sample_loop_start_has_listener(TSimplerDevicePyViewData,boost::python::api::object)
            """

        def sample_start_has_listener(self, listener: Callable) -> bool:
            """
            sample_start_has_listener( (View)arg1, (object)arg2) -> bool :
                Returns true, if the given listener function or method is connected
                to the property "sample_start".

                C++ signature :
                    bool sample_start_has_listener(TSimplerDevicePyViewData,boost::python::api::object)
            """

        def selected_slice_has_listener(self, listener: Callable) -> bool:
            """
            selected_slice_has_listener( (View)arg1, (object)arg2) -> bool :
                Returns true, if the given listener function or method is connected
                to the property "selected_slice".

                C++ signature :
                    bool selected_slice_has_listener(TSimplerDevicePyViewData,boost::python::api::object)
            """

        @property
        def canonical_parent(self) -> Any:
            """
            Get the canonical parent of the View.
            """

        @property
        def is_collapsed(self) -> bool:
            """
            Get/Set/Listen if the device is shown collapsed in the device chain.
            """

        @is_collapsed.setter
        def is_collapsed(self, value: bool) -> None:
            pass

        @property
        def sample_end(self) -> Any:
            """
            Access to the modulated samples end position in samples. Returns -1 in case there is no sample loaded.
            """

        @property
        def sample_env_fade_in(self) -> Any:
            """
            Access to the envelope fade-in time in samples. Returned value is only in use when Simpler is in one-shot mode. Returns -1 in case there is no sample loaded.
            """

        @property
        def sample_env_fade_out(self) -> Any:
            """
            Access to the envelope fade-out time in samples. Returned value is only in use when Simpler is in one-shot mode. Returns -1 in case there is no sample loaded.
            """

        @property
        def sample_loop_end(self) -> Any:
            """
            Access to the modulated samples loop end position in samples. Returns -1 in case there is no sample loaded.
            """

        @property
        def sample_loop_fade(self) -> Any:
            """
            Access to the modulated samples loop fade position in samples. Returns -1 in case there is no sample loaded.
            """

        @property
        def sample_loop_start(self) -> Any:
            """
            Access to the modulated samples loop start position in samples. Returns -1 in case there is no sample loaded.
            """

        @property
        def sample_start(self) -> Any:
            """
            Access to the modulated samples start position in samples. Returns -1 in case there is no sample loaded.
            """

        @property
        def selected_slice(self) -> Any:
            """
            Access to the selected slice.
            """

    def add_can_warp_as_listener(self, listener: Callable) -> None:
        """
        add_can_warp_as_listener( (SimplerDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "can_warp_as" has changed.

            C++ signature :
                void add_can_warp_as_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def add_can_warp_double_listener(self, listener: Callable) -> None:
        """
        add_can_warp_double_listener( (SimplerDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "can_warp_double" has changed.

            C++ signature :
                void add_can_warp_double_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def add_can_warp_half_listener(self, listener: Callable) -> None:
        """
        add_can_warp_half_listener( (SimplerDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "can_warp_half" has changed.

            C++ signature :
                void add_can_warp_half_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def add_is_active_listener(self, listener: Callable) -> None:
        """
        add_is_active_listener( (Device)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "is_active" has changed.

            C++ signature :
                void add_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def add_latency_in_ms_listener(self, listener: Callable) -> None:
        """
        add_latency_in_ms_listener( (Device)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "latency_in_ms" has changed.

            C++ signature :
                void add_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def add_latency_in_samples_listener(self, listener: Callable) -> None:
        """
        add_latency_in_samples_listener( (Device)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "latency_in_samples" has changed.

            C++ signature :
                void add_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def add_multi_sample_mode_listener(self, listener: Callable) -> None:
        """
        add_multi_sample_mode_listener( (SimplerDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "multi_sample_mode" has changed.

            C++ signature :
                void add_multi_sample_mode_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def add_name_listener(self, listener: Callable) -> None:
        """
        add_name_listener( (Device)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "name" has changed.

            C++ signature :
                void add_name_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def add_note_pitch_bend_range_listener(self, listener: Callable) -> None:
        """
        add_note_pitch_bend_range_listener( (SimplerDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "note_pitch_bend_range" has changed.

            C++ signature :
                void add_note_pitch_bend_range_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def add_pad_slicing_listener(self, listener: Callable) -> None:
        """
        add_pad_slicing_listener( (SimplerDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "pad_slicing" has changed.

            C++ signature :
                void add_pad_slicing_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def add_parameters_listener(self, listener: Callable) -> None:
        """
        add_parameters_listener( (Device)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "parameters" has changed.

            C++ signature :
                void add_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def add_pitch_bend_range_listener(self, listener: Callable) -> None:
        """
        add_pitch_bend_range_listener( (SimplerDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "pitch_bend_range" has changed.

            C++ signature :
                void add_pitch_bend_range_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def add_playback_mode_listener(self, listener: Callable) -> None:
        """
        add_playback_mode_listener( (SimplerDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "playback_mode" has changed.

            C++ signature :
                void add_playback_mode_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def add_playing_position_enabled_listener(self, listener: Callable) -> None:
        """
        add_playing_position_enabled_listener( (SimplerDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "playing_position_enabled" has changed.

            C++ signature :
                void add_playing_position_enabled_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def add_playing_position_listener(self, listener: Callable) -> None:
        """
        add_playing_position_listener( (SimplerDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "playing_position" has changed.

            C++ signature :
                void add_playing_position_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def add_retrigger_listener(self, listener: Callable) -> None:
        """
        add_retrigger_listener( (SimplerDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "retrigger" has changed.

            C++ signature :
                void add_retrigger_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def add_sample_listener(self, listener: Callable) -> None:
        """
        add_sample_listener( (SimplerDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "sample" has changed.

            C++ signature :
                void add_sample_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def add_slicing_playback_mode_listener(self, listener: Callable) -> None:
        """
        add_slicing_playback_mode_listener( (SimplerDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "slicing_playback_mode" has changed.

            C++ signature :
                void add_slicing_playback_mode_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def add_voices_listener(self, listener: Callable) -> None:
        """
        add_voices_listener( (SimplerDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "voices" has changed.

            C++ signature :
                void add_voices_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def can_warp_as_has_listener(self, listener: Callable) -> bool:
        """
        can_warp_as_has_listener( (SimplerDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "can_warp_as".

            C++ signature :
                bool can_warp_as_has_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def can_warp_double_has_listener(self, listener: Callable) -> bool:
        """
        can_warp_double_has_listener( (SimplerDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "can_warp_double".

            C++ signature :
                bool can_warp_double_has_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def can_warp_half_has_listener(self, listener: Callable) -> bool:
        """
        can_warp_half_has_listener( (SimplerDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "can_warp_half".

            C++ signature :
                bool can_warp_half_has_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def crop(self) -> None:
        """
        crop( (SimplerDevice)self) -> None :
            Crop the loaded sample to the active area between start- and end marker.
            Calling this method on an empty simpler raises an error.

            C++ signature :
                void crop(TSimplerDevicePyHandle)
        """

    def guess_playback_length(self) -> float:
        """
        guess_playback_length( (SimplerDevice)self) -> float :
            Return an estimated beat time for the playback length between start- and end-marker.
            Calling this method on an empty simpler raises an error.

            C++ signature :
                double guess_playback_length(TSimplerDevicePyHandle)
        """

    def is_active_has_listener(self, listener: Callable) -> bool:
        """
        is_active_has_listener( (Device)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "is_active".

            C++ signature :
                bool is_active_has_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def latency_in_ms_has_listener(self, listener: Callable) -> bool:
        """
        latency_in_ms_has_listener( (Device)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "latency_in_ms".

            C++ signature :
                bool latency_in_ms_has_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def latency_in_samples_has_listener(self, listener: Callable) -> bool:
        """
        latency_in_samples_has_listener( (Device)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "latency_in_samples".

            C++ signature :
                bool latency_in_samples_has_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def multi_sample_mode_has_listener(self, listener: Callable) -> bool:
        """
        multi_sample_mode_has_listener( (SimplerDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "multi_sample_mode".

            C++ signature :
                bool multi_sample_mode_has_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def name_has_listener(self, listener: Callable) -> bool:
        """
        name_has_listener( (Device)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "name".

            C++ signature :
                bool name_has_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def note_pitch_bend_range_has_listener(self, listener: Callable) -> bool:
        """
        note_pitch_bend_range_has_listener( (SimplerDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "note_pitch_bend_range".

            C++ signature :
                bool note_pitch_bend_range_has_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def pad_slicing_has_listener(self, listener: Callable) -> bool:
        """
        pad_slicing_has_listener( (SimplerDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "pad_slicing".

            C++ signature :
                bool pad_slicing_has_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def parameters_has_listener(self, listener: Callable) -> bool:
        """
        parameters_has_listener( (Device)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "parameters".

            C++ signature :
                bool parameters_has_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def pitch_bend_range_has_listener(self, listener: Callable) -> bool:
        """
        pitch_bend_range_has_listener( (SimplerDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "pitch_bend_range".

            C++ signature :
                bool pitch_bend_range_has_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def playback_mode_has_listener(self, listener: Callable) -> bool:
        """
        playback_mode_has_listener( (SimplerDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "playback_mode".

            C++ signature :
                bool playback_mode_has_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def playing_position_enabled_has_listener(self, listener: Callable) -> bool:
        """
        playing_position_enabled_has_listener( (SimplerDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "playing_position_enabled".

            C++ signature :
                bool playing_position_enabled_has_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def playing_position_has_listener(self, listener: Callable) -> bool:
        """
        playing_position_has_listener( (SimplerDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "playing_position".

            C++ signature :
                bool playing_position_has_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def remove_can_warp_as_listener(self, listener: Callable) -> None:
        """
        remove_can_warp_as_listener( (SimplerDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "can_warp_as".

            C++ signature :
                void remove_can_warp_as_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def remove_can_warp_double_listener(self, listener: Callable) -> None:
        """
        remove_can_warp_double_listener( (SimplerDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "can_warp_double".

            C++ signature :
                void remove_can_warp_double_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def remove_can_warp_half_listener(self, listener: Callable) -> None:
        """
        remove_can_warp_half_listener( (SimplerDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "can_warp_half".

            C++ signature :
                void remove_can_warp_half_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def remove_is_active_listener(self, listener: Callable) -> None:
        """
        remove_is_active_listener( (Device)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "is_active".

            C++ signature :
                void remove_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def remove_latency_in_ms_listener(self, listener: Callable) -> None:
        """
        remove_latency_in_ms_listener( (Device)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "latency_in_ms".

            C++ signature :
                void remove_latency_in_ms_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def remove_latency_in_samples_listener(self, listener: Callable) -> None:
        """
        remove_latency_in_samples_listener( (Device)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "latency_in_samples".

            C++ signature :
                void remove_latency_in_samples_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def remove_multi_sample_mode_listener(self, listener: Callable) -> None:
        """
        remove_multi_sample_mode_listener( (SimplerDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "multi_sample_mode".

            C++ signature :
                void remove_multi_sample_mode_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def remove_name_listener(self, listener: Callable) -> None:
        """
        remove_name_listener( (Device)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "name".

            C++ signature :
                void remove_name_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def remove_note_pitch_bend_range_listener(self, listener: Callable) -> None:
        """
        remove_note_pitch_bend_range_listener( (SimplerDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "note_pitch_bend_range".

            C++ signature :
                void remove_note_pitch_bend_range_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def remove_pad_slicing_listener(self, listener: Callable) -> None:
        """
        remove_pad_slicing_listener( (SimplerDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "pad_slicing".

            C++ signature :
                void remove_pad_slicing_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def remove_parameters_listener(self, listener: Callable) -> None:
        """
        remove_parameters_listener( (Device)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "parameters".

            C++ signature :
                void remove_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def remove_pitch_bend_range_listener(self, listener: Callable) -> None:
        """
        remove_pitch_bend_range_listener( (SimplerDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "pitch_bend_range".

            C++ signature :
                void remove_pitch_bend_range_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def remove_playback_mode_listener(self, listener: Callable) -> None:
        """
        remove_playback_mode_listener( (SimplerDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "playback_mode".

            C++ signature :
                void remove_playback_mode_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def remove_playing_position_enabled_listener(self, listener: Callable) -> None:
        """
        remove_playing_position_enabled_listener( (SimplerDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "playing_position_enabled".

            C++ signature :
                void remove_playing_position_enabled_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def remove_playing_position_listener(self, listener: Callable) -> None:
        """
        remove_playing_position_listener( (SimplerDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "playing_position".

            C++ signature :
                void remove_playing_position_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def remove_retrigger_listener(self, listener: Callable) -> None:
        """
        remove_retrigger_listener( (SimplerDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "retrigger".

            C++ signature :
                void remove_retrigger_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def remove_sample_listener(self, listener: Callable) -> None:
        """
        remove_sample_listener( (SimplerDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "sample".

            C++ signature :
                void remove_sample_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def remove_slicing_playback_mode_listener(self, listener: Callable) -> None:
        """
        remove_slicing_playback_mode_listener( (SimplerDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "slicing_playback_mode".

            C++ signature :
                void remove_slicing_playback_mode_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def remove_voices_listener(self, listener: Callable) -> None:
        """
        remove_voices_listener( (SimplerDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "voices".

            C++ signature :
                void remove_voices_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def retrigger_has_listener(self, listener: Callable) -> bool:
        """
        retrigger_has_listener( (SimplerDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "retrigger".

            C++ signature :
                bool retrigger_has_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def reverse(self) -> None:
        """
        reverse( (SimplerDevice)self) -> None :
            Reverse the loaded sample.
            Calling this method on an empty simpler raises an error.

            C++ signature :
                void reverse(TSimplerDevicePyHandle)
        """

    def sample_has_listener(self, listener: Callable) -> bool:
        """
        sample_has_listener( (SimplerDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "sample".

            C++ signature :
                bool sample_has_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def slicing_playback_mode_has_listener(self, listener: Callable) -> bool:
        """
        slicing_playback_mode_has_listener( (SimplerDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "slicing_playback_mode".

            C++ signature :
                bool slicing_playback_mode_has_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def store_chosen_bank(self, arg2: int, arg3: int) -> None:
        """
        store_chosen_bank( (Device)arg1, (int)arg2, (int)arg3) -> None :
            Set the selected bank in the device for persistency.

            C++ signature :
                void store_chosen_bank(TPyHandle<ADevice>,int,int)
        """

    def voices_has_listener(self, listener: Callable) -> bool:
        """
        voices_has_listener( (SimplerDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "voices".

            C++ signature :
                bool voices_has_listener(TSimplerDevicePyHandle,boost::python::api::object)
        """

    def warp_as(self, beat_time: float) -> None:
        """
        warp_as( (SimplerDevice)self, (float)beat_time) -> None :
            Warp the playback region between start- and end-marker as the given length.
            Calling this method on an empty simpler raises an error.

            C++ signature :
                void warp_as(TSimplerDevicePyHandle,double)
        """

    def warp_double(self) -> None:
        """
        warp_double( (SimplerDevice)self) -> None :
            Doubles the tempo for region between start- and end-marker.

            C++ signature :
                void warp_double(TSimplerDevicePyHandle)
        """

    def warp_half(self) -> None:
        """
        warp_half( (SimplerDevice)self) -> None :
            Halves the tempo for region between start- and end-marker.

            C++ signature :
                void warp_half(TSimplerDevicePyHandle)
        """

    @property
    def can_have_chains(self) -> bool:
        """
        Returns true if the device is a rack.
        """

    @property
    def can_have_drum_pads(self) -> bool:
        """
        Returns true if the device is a drum rack.
        """

    @property
    def can_warp_as(self) -> bool:
        """
        Returns true if warp_as is available.
        """

    @property
    def can_warp_double(self) -> bool:
        """
        Returns true if warp_double is available.
        """

    @property
    def can_warp_half(self) -> bool:
        """
        Returns true if warp_half is available.
        """

    @property
    def canonical_parent(self) -> Any:
        """
        Get the canonical parent of the Device.
        """

    @property
    def class_display_name(self) -> str:
        """
        Return const access to the name of the device's class name as displayed in Live's browser and device chain
        """

    @property
    def class_name(self) -> str:
        """
        Return const access to the name of the device's class.
        """

    @property
    def is_active(self) -> bool:
        """
        Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
        """

    @property
    def latency_in_ms(self) -> Any:
        """
        Returns the latency of the device in ms.
        """

    @property
    def latency_in_samples(self) -> Any:
        """
        Returns the latency of the device in samples.
        """

    @property
    def multi_sample_mode(self) -> Any:
        """
        Returns whether Simpler is in mulit-sample mode.
        """

    @property
    def name(self) -> str:
        """
        Return access to the name of the device.
        """

    @property
    def note_pitch_bend_range(self) -> Any:
        """
        Access to the Note Pitch Bend Range in Simpler.
        """

    @property
    def pad_slicing(self) -> Any:
        """
        When set to true, slices can be added in slicing mode by playing notes
        .that are not assigned to slices, yet.
        """

    @property
    def parameters(self) -> list[DeviceParameter]:
        """
        Const access to the list of available automatable parameters for this device.
        """

    @property
    def pitch_bend_range(self) -> Any:
        """
        Access to the Pitch Bend Range in Simpler.
        """

    @property
    def playback_mode(self) -> Any:
        """
        Access to Simpler's playback mode.
        """

    @property
    def playing_position(self) -> Any:
        """
        Constant access to the current playing position in the sample.
        The returned value is the normalized position between sample start and end.
        """

    @property
    def playing_position_enabled(self) -> Any:
        """
        Returns whether Simpler is showing the playing position.
        The returned value is True while the sample is played back
        """

    @property
    def retrigger(self) -> Any:
        """
        Access to Simpler's retrigger mode.
        """

    @property
    def sample(self) -> Any:
        """
        Get the loaded Sample.
        """

    @property
    def slicing_playback_mode(self) -> Any:
        """
        Access to Simpler's slicing playback mode.
        """

    @property
    def type(self) -> Any:
        """
        Return the type of the device.
        """

    @property
    def view(self) -> View:
        """
        Representing the view aspects of a device.
        """

    @property
    def voices(self) -> Any:
        """
        Access to the number of voices in Simpler.
        """


class SlicingPlaybackMode:
    """
    Class that represent an enumeration of values for SlicingPlaybackMode
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
    poly = 1
    thru = 2


def get_available_voice_numbers() -> IntVector:
    """
    get_available_voice_numbers() -> IntVector :
        Get a vector of valid Simpler voice numbers.

        C++ signature :
            std::__1::vector<int, std::__1::allocator<int>> get_available_voice_numbers()
    """

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
from Live.TuningSystem import *


class EffectMode:
    """
    Class that represent an enumeration of values for EffectMode
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

    none = 0
    frequency_modulation = 1
    sync_and_pulse_width = 2
    warp_and_fold = 3


class FilterRouting:
    """
    Class that represent an enumeration of values for FilterRouting
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

    serial = 0
    parallel = 1
    split = 2


class ModulationSource:
    """
    Class that represent an enumeration of values for ModulationSource
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

    amp_envelope = 0
    envelope_2 = 1
    envelope_3 = 2
    lfo_1 = 3
    lfo_2 = 4
    midi_velocity = 5
    midi_note = 6
    midi_pitch_bend = 7
    midi_channel_pressure = 8
    midi_mod_wheel = 9
    midi_random = 10


class UnisonMode:
    """
    Class that represent an enumeration of values for UnisonMode
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

    none = 0
    classic = 1
    slow_shimmer = 2
    fast_shimmer = 3
    phase_sync = 4
    position_spread = 5
    random_note = 6


class VoiceCount:
    """
    Class that represent an enumeration of values for VoiceCount
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

    two = 0
    three = 1
    four = 2
    five = 3
    six = 4
    seven = 5
    eight = 6


class Voicing:
    """
    Class that represent an enumeration of values for Voicing
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


class WavetableDevice:
    """
    This class represents a Wavetable device.
    """

    class View:
        """
        Representing the view aspects of a device.
        """

        def add_is_collapsed_listener(self, listener: Callable) -> None:
            """
            add_is_collapsed_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "is_collapsed" has changed.

                C++ signature :
                    void add_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
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

    def add_filter_routing_listener(self, listener: Callable) -> None:
        """
        add_filter_routing_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "filter_routing" has changed.

            C++ signature :
                void add_filter_routing_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def add_is_active_listener(self, listener: Callable) -> None:
        """
        add_is_active_listener( (Device)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "is_active" has changed.

            C++ signature :
                void add_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def add_is_using_compare_preset_b_listener(self, listener: Callable) -> None:
        """
        add_is_using_compare_preset_b_listener( (Device)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "is_using_compare_preset_b" has changed.

            C++ signature :
                void add_is_using_compare_preset_b_listener(TPyHandle<ADevice>,boost::python::api::object)
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

    def add_modulation_matrix_changed_listener(self, listener: Callable) -> None:
        """
        add_modulation_matrix_changed_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "modulation_matrix_changed" has changed.

            C++ signature :
                void add_modulation_matrix_changed_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def add_mono_poly_listener(self, listener: Callable) -> None:
        """
        add_mono_poly_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "mono_poly" has changed.

            C++ signature :
                void add_mono_poly_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def add_name_listener(self, listener: Callable) -> None:
        """
        add_name_listener( (Device)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "name" has changed.

            C++ signature :
                void add_name_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def add_oscillator_1_effect_mode_listener(self, listener: Callable) -> None:
        """
        add_oscillator_1_effect_mode_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "oscillator_1_effect_mode" has changed.

            C++ signature :
                void add_oscillator_1_effect_mode_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def add_oscillator_1_wavetable_category_listener(self, listener: Callable) -> None:
        """
        add_oscillator_1_wavetable_category_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "oscillator_1_wavetable_category" has changed.

            C++ signature :
                void add_oscillator_1_wavetable_category_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def add_oscillator_1_wavetable_index_listener(self, listener: Callable) -> None:
        """
        add_oscillator_1_wavetable_index_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "oscillator_1_wavetable_index" has changed.

            C++ signature :
                void add_oscillator_1_wavetable_index_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def add_oscillator_1_wavetables_listener(self, listener: Callable) -> None:
        """
        add_oscillator_1_wavetables_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "oscillator_1_wavetables" has changed.

            C++ signature :
                void add_oscillator_1_wavetables_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def add_oscillator_2_effect_mode_listener(self, listener: Callable) -> None:
        """
        add_oscillator_2_effect_mode_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "oscillator_2_effect_mode" has changed.

            C++ signature :
                void add_oscillator_2_effect_mode_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def add_oscillator_2_wavetable_category_listener(self, listener: Callable) -> None:
        """
        add_oscillator_2_wavetable_category_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "oscillator_2_wavetable_category" has changed.

            C++ signature :
                void add_oscillator_2_wavetable_category_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def add_oscillator_2_wavetable_index_listener(self, listener: Callable) -> None:
        """
        add_oscillator_2_wavetable_index_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "oscillator_2_wavetable_index" has changed.

            C++ signature :
                void add_oscillator_2_wavetable_index_listener(TWavetableDevicePyHandle,boost::python::api::object)

        add_oscillator_2_wavetable_index_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "oscillator_2_wavetable_index" has changed.

            C++ signature :
                void add_oscillator_2_wavetable_index_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def add_oscillator_2_wavetables_listener(self, listener: Callable) -> None:
        """
        add_oscillator_2_wavetables_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "oscillator_2_wavetables" has changed.

            C++ signature :
                void add_oscillator_2_wavetables_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def add_parameter_to_modulation_matrix(self, parameter: object) -> int:
        """
        add_parameter_to_modulation_matrix( (WavetableDevice)self, (DeviceParameter)parameter) -> int :
            Add a non-pitch parameter to the modulation matrix.

            C++ signature :
                int add_parameter_to_modulation_matrix(TWavetableDevicePyHandle,TPyHandle<ATimeableValue>)
        """

    def add_parameters_listener(self, listener: Callable) -> None:
        """
        add_parameters_listener( (Device)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "parameters" has changed.

            C++ signature :
                void add_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def add_poly_voices_listener(self, listener: Callable) -> None:
        """
        add_poly_voices_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "poly_voices" has changed.

            C++ signature :
                void add_poly_voices_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def add_unison_mode_listener(self, listener: Callable) -> None:
        """
        add_unison_mode_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "unison_mode" has changed.

            C++ signature :
                void add_unison_mode_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def add_unison_voice_count_listener(self, listener: Callable) -> None:
        """
        add_unison_voice_count_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "unison_voice_count" has changed.

            C++ signature :
                void add_unison_voice_count_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def add_visible_modulation_target_names_listener(self, listener: Callable) -> None:
        """
        add_visible_modulation_target_names_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "visible_modulation_target_names" has changed.

            C++ signature :
                void add_visible_modulation_target_names_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def filter_routing_has_listener(self, listener: Callable) -> bool:
        """
        filter_routing_has_listener( (WavetableDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "filter_routing".

            C++ signature :
                bool filter_routing_has_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def get_modulation_target_parameter_name(self, target_index: int) -> str:
        """
        get_modulation_target_parameter_name( (WavetableDevice)self, (int)target_index) -> str :
            Get the parameter name of the modulation target at the given index.

            C++ signature :
                TString get_modulation_target_parameter_name(TWavetableDevicePyHandle,int)
        """

    def get_modulation_value(self, target_index: int, source: int) -> float:
        """
        get_modulation_value( (WavetableDevice)self, (int)target_index, (int)source) -> float :
            Get the value of a modulation amount for the given target-source connection.

            C++ signature :
                float get_modulation_value(TWavetableDevicePyHandle,int,int)
        """

    def is_active_has_listener(self, listener: Callable) -> bool:
        """
        is_active_has_listener( (Device)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "is_active".

            C++ signature :
                bool is_active_has_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def is_parameter_modulatable(self, parameter: object) -> bool:
        """
        is_parameter_modulatable( (WavetableDevice)self, (DeviceParameter)parameter) -> bool :
            Indicate whether the parameter is modulatable. Note that pitch parameters only exist in python and must be handled there.

            C++ signature :
                bool is_parameter_modulatable(TWavetableDevicePyHandle,TPyHandle<ATimeableValue>)
        """

    def is_using_compare_preset_b_has_listener(self, listener: Callable) -> bool:
        """
        is_using_compare_preset_b_has_listener( (Device)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "is_using_compare_preset_b".

            C++ signature :
                bool is_using_compare_preset_b_has_listener(TPyHandle<ADevice>,boost::python::api::object)
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

    def modulation_matrix_changed_has_listener(self, listener: Callable) -> bool:
        """
        modulation_matrix_changed_has_listener( (WavetableDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "modulation_matrix_changed".

            C++ signature :
                bool modulation_matrix_changed_has_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def mono_poly_has_listener(self, listener: Callable) -> bool:
        """
        mono_poly_has_listener( (WavetableDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "mono_poly".

            C++ signature :
                bool mono_poly_has_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def name_has_listener(self, listener: Callable) -> bool:
        """
        name_has_listener( (Device)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "name".

            C++ signature :
                bool name_has_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def oscillator_1_effect_mode_has_listener(self, listener: Callable) -> bool:
        """
        oscillator_1_effect_mode_has_listener( (WavetableDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "oscillator_1_effect_mode".

            C++ signature :
                bool oscillator_1_effect_mode_has_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def oscillator_1_wavetable_category_has_listener(self, listener: Callable) -> bool:
        """
        oscillator_1_wavetable_category_has_listener( (WavetableDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "oscillator_1_wavetable_category".

            C++ signature :
                bool oscillator_1_wavetable_category_has_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def oscillator_1_wavetable_index_has_listener(self, listener: Callable) -> bool:
        """
        oscillator_1_wavetable_index_has_listener( (WavetableDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "oscillator_1_wavetable_index".

            C++ signature :
                bool oscillator_1_wavetable_index_has_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def oscillator_1_wavetables_has_listener(self, listener: Callable) -> bool:
        """
        oscillator_1_wavetables_has_listener( (WavetableDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "oscillator_1_wavetables".

            C++ signature :
                bool oscillator_1_wavetables_has_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def oscillator_2_effect_mode_has_listener(self, listener: Callable) -> bool:
        """
        oscillator_2_effect_mode_has_listener( (WavetableDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "oscillator_2_effect_mode".

            C++ signature :
                bool oscillator_2_effect_mode_has_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def oscillator_2_wavetable_category_has_listener(self, listener: Callable) -> bool:
        """
        oscillator_2_wavetable_category_has_listener( (WavetableDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "oscillator_2_wavetable_category".

            C++ signature :
                bool oscillator_2_wavetable_category_has_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def oscillator_2_wavetable_index_has_listener(self, listener: Callable) -> bool:
        """
        oscillator_2_wavetable_index_has_listener( (WavetableDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "oscillator_2_wavetable_index".

            C++ signature :
                bool oscillator_2_wavetable_index_has_listener(TWavetableDevicePyHandle,boost::python::api::object)

        oscillator_2_wavetable_index_has_listener( (WavetableDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "oscillator_2_wavetable_index".

            C++ signature :
                bool oscillator_2_wavetable_index_has_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def oscillator_2_wavetables_has_listener(self, listener: Callable) -> bool:
        """
        oscillator_2_wavetables_has_listener( (WavetableDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "oscillator_2_wavetables".

            C++ signature :
                bool oscillator_2_wavetables_has_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def parameters_has_listener(self, listener: Callable) -> bool:
        """
        parameters_has_listener( (Device)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "parameters".

            C++ signature :
                bool parameters_has_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def poly_voices_has_listener(self, listener: Callable) -> bool:
        """
        poly_voices_has_listener( (WavetableDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "poly_voices".

            C++ signature :
                bool poly_voices_has_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def remove_filter_routing_listener(self, listener: Callable) -> None:
        """
        remove_filter_routing_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "filter_routing".

            C++ signature :
                void remove_filter_routing_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def remove_is_active_listener(self, listener: Callable) -> None:
        """
        remove_is_active_listener( (Device)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "is_active".

            C++ signature :
                void remove_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def remove_is_using_compare_preset_b_listener(self, listener: Callable) -> None:
        """
        remove_is_using_compare_preset_b_listener( (Device)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "is_using_compare_preset_b".

            C++ signature :
                void remove_is_using_compare_preset_b_listener(TPyHandle<ADevice>,boost::python::api::object)
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

    def remove_modulation_matrix_changed_listener(self, listener: Callable) -> None:
        """
        remove_modulation_matrix_changed_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "modulation_matrix_changed".

            C++ signature :
                void remove_modulation_matrix_changed_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def remove_mono_poly_listener(self, listener: Callable) -> None:
        """
        remove_mono_poly_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "mono_poly".

            C++ signature :
                void remove_mono_poly_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def remove_name_listener(self, listener: Callable) -> None:
        """
        remove_name_listener( (Device)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "name".

            C++ signature :
                void remove_name_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def remove_oscillator_1_effect_mode_listener(self, listener: Callable) -> None:
        """
        remove_oscillator_1_effect_mode_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "oscillator_1_effect_mode".

            C++ signature :
                void remove_oscillator_1_effect_mode_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def remove_oscillator_1_wavetable_category_listener(self, listener: Callable) -> None:
        """
        remove_oscillator_1_wavetable_category_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "oscillator_1_wavetable_category".

            C++ signature :
                void remove_oscillator_1_wavetable_category_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def remove_oscillator_1_wavetable_index_listener(self, listener: Callable) -> None:
        """
        remove_oscillator_1_wavetable_index_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "oscillator_1_wavetable_index".

            C++ signature :
                void remove_oscillator_1_wavetable_index_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def remove_oscillator_1_wavetables_listener(self, listener: Callable) -> None:
        """
        remove_oscillator_1_wavetables_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "oscillator_1_wavetables".

            C++ signature :
                void remove_oscillator_1_wavetables_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def remove_oscillator_2_effect_mode_listener(self, listener: Callable) -> None:
        """
        remove_oscillator_2_effect_mode_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "oscillator_2_effect_mode".

            C++ signature :
                void remove_oscillator_2_effect_mode_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def remove_oscillator_2_wavetable_category_listener(self, listener: Callable) -> None:
        """
        remove_oscillator_2_wavetable_category_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "oscillator_2_wavetable_category".

            C++ signature :
                void remove_oscillator_2_wavetable_category_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def remove_oscillator_2_wavetable_index_listener(self, listener: Callable) -> None:
        """
        remove_oscillator_2_wavetable_index_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "oscillator_2_wavetable_index".

            C++ signature :
                void remove_oscillator_2_wavetable_index_listener(TWavetableDevicePyHandle,boost::python::api::object)

        remove_oscillator_2_wavetable_index_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "oscillator_2_wavetable_index".

            C++ signature :
                void remove_oscillator_2_wavetable_index_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def remove_oscillator_2_wavetables_listener(self, listener: Callable) -> None:
        """
        remove_oscillator_2_wavetables_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "oscillator_2_wavetables".

            C++ signature :
                void remove_oscillator_2_wavetables_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def remove_parameters_listener(self, listener: Callable) -> None:
        """
        remove_parameters_listener( (Device)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "parameters".

            C++ signature :
                void remove_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def remove_poly_voices_listener(self, listener: Callable) -> None:
        """
        remove_poly_voices_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "poly_voices".

            C++ signature :
                void remove_poly_voices_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def remove_unison_mode_listener(self, listener: Callable) -> None:
        """
        remove_unison_mode_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "unison_mode".

            C++ signature :
                void remove_unison_mode_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def remove_unison_voice_count_listener(self, listener: Callable) -> None:
        """
        remove_unison_voice_count_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "unison_voice_count".

            C++ signature :
                void remove_unison_voice_count_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def remove_visible_modulation_target_names_listener(self, listener: Callable) -> None:
        """
        remove_visible_modulation_target_names_listener( (WavetableDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "visible_modulation_target_names".

            C++ signature :
                void remove_visible_modulation_target_names_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def save_preset_to_compare_ab_slot(self) -> None:
        """
        save_preset_to_compare_ab_slot( (Device)arg1) -> None :
            Saves the current state of the device to the compare AB slot. Only relevant if can_compare_ab, otherwise throws.

            C++ signature :
                void save_preset_to_compare_ab_slot(TPyHandle<ADevice>)
        """

    def set_modulation_value(self, target_index: int, source: int, value: float) -> None:
        """
        set_modulation_value( (WavetableDevice)self, (int)target_index, (int)source, (float)value) -> None :
            Set the value of a modulation amount for the given target-source connection.

            C++ signature :
                void set_modulation_value(TWavetableDevicePyHandle,int,int,float)
        """

    def store_chosen_bank(self, arg2: int, arg3: int) -> None:
        """
        store_chosen_bank( (Device)arg1, (int)arg2, (int)arg3) -> None :
            Set the selected bank in the device for persistency.

            C++ signature :
                void store_chosen_bank(TPyHandle<ADevice>,int,int)
        """

    def unison_mode_has_listener(self, listener: Callable) -> bool:
        """
        unison_mode_has_listener( (WavetableDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "unison_mode".

            C++ signature :
                bool unison_mode_has_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def unison_voice_count_has_listener(self, listener: Callable) -> bool:
        """
        unison_voice_count_has_listener( (WavetableDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "unison_voice_count".

            C++ signature :
                bool unison_voice_count_has_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    def visible_modulation_target_names_has_listener(self, listener: Callable) -> bool:
        """
        visible_modulation_target_names_has_listener( (WavetableDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "visible_modulation_target_names".

            C++ signature :
                bool visible_modulation_target_names_has_listener(TWavetableDevicePyHandle,boost::python::api::object)
        """

    @property
    def can_compare_ab(self) -> bool:
        """
        Returns true if the Device has the capability to AB compare.
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
    def filter_routing(self) -> Any:
        """
        Return the current filter routing.
        """

    @property
    def is_active(self) -> bool:
        """
        Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
        """

    @property
    def is_using_compare_preset_b(self) -> bool:
        """
        Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors.
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
    def mono_poly(self) -> Any:
        """
        Return the current voicing mode.
        """

    @property
    def name(self) -> str:
        """
        Return access to the name of the device.
        """

    @property
    def oscillator_1_effect_mode(self) -> Any:
        """
        Return the current effect mode of the oscillator 1.
        """

    @property
    def oscillator_1_wavetable_category(self) -> Any:
        """
        Return the current wavetable category of the oscillator 1.
        """

    @property
    def oscillator_1_wavetable_index(self) -> Any:
        """
        Return the current wavetable index of the oscillator 1.
        """

    @property
    def oscillator_1_wavetables(self) -> Any:
        """
        Get a vector of oscillator 1's wavetable names.
        """

    @property
    def oscillator_2_effect_mode(self) -> Any:
        """
        Return the current effect mode of the oscillator 2.
        """

    @property
    def oscillator_2_wavetable_category(self) -> Any:
        """
        Return the current wavetable category of the oscillator 2.
        """

    @property
    def oscillator_2_wavetable_index(self) -> Any:
        """
        Return the current wavetable index of the oscillator 2.
        """

    @property
    def oscillator_2_wavetables(self) -> Any:
        """
        Get a vector of oscillator 2's wavetable names.
        """

    @property
    def oscillator_wavetable_categories(self) -> Any:
        """
        Get a vector of the available wavetable categories.
        """

    @property
    def parameters(self) -> list[DeviceParameter]:
        """
        Const access to the list of available automatable parameters for this device.
        """

    @property
    def poly_voices(self) -> Any:
        """
        Return the current number of polyphonic voices. Uses the VoiceCount enumeration.
        """

    @property
    def type(self) -> Any:
        """
        Return the type of the device.
        """

    @property
    def unison_mode(self) -> Any:
        """
        Return the current unison mode.
        """

    @property
    def unison_voice_count(self) -> Any:
        """
        Return the current number of unison voices.
        """

    @property
    def view(self) -> View:
        """
        Representing the view aspects of a device.
        """

    @property
    def visible_modulation_target_names(self) -> Any:
        """
        Get the names of all the visible modulation targets.
        """

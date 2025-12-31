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
from Live.TakeLane import *
from Live.Track import *
from Live.TuningSystem import *
from Live.WavetableDevice import *


class SpectralResonatorDevice:
    """
    This class represents a Spectral Resonator device.
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

    def add_frequency_dial_mode_list_listener(self, listener: Callable) -> None:
        """
        add_frequency_dial_mode_list_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "frequency_dial_mode_list" has changed.

            C++ signature :
                void add_frequency_dial_mode_list_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def add_frequency_dial_mode_listener(self, listener: Callable) -> None:
        """
        add_frequency_dial_mode_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "frequency_dial_mode" has changed.

            C++ signature :
                void add_frequency_dial_mode_listener(TTransmuteDevicePyHandle,boost::python::api::object)
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

    def add_midi_gate_list_listener(self, listener: Callable) -> None:
        """
        add_midi_gate_list_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "midi_gate_list" has changed.

            C++ signature :
                void add_midi_gate_list_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def add_midi_gate_listener(self, listener: Callable) -> None:
        """
        add_midi_gate_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "midi_gate" has changed.

            C++ signature :
                void add_midi_gate_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def add_mod_mode_list_listener(self, listener: Callable) -> None:
        """
        add_mod_mode_list_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "mod_mode_list" has changed.

            C++ signature :
                void add_mod_mode_list_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def add_mod_mode_listener(self, listener: Callable) -> None:
        """
        add_mod_mode_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "mod_mode" has changed.

            C++ signature :
                void add_mod_mode_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def add_mono_poly_list_listener(self, listener: Callable) -> None:
        """
        add_mono_poly_list_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "mono_poly_list" has changed.

            C++ signature :
                void add_mono_poly_list_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def add_mono_poly_listener(self, listener: Callable) -> None:
        """
        add_mono_poly_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "mono_poly" has changed.

            C++ signature :
                void add_mono_poly_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def add_name_listener(self, listener: Callable) -> None:
        """
        add_name_listener( (Device)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "name" has changed.

            C++ signature :
                void add_name_listener(TPyHandle<ADevice>,boost::python::api::object)
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
        add_pitch_bend_range_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "pitch_bend_range" has changed.

            C++ signature :
                void add_pitch_bend_range_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def add_pitch_mode_list_listener(self, listener: Callable) -> None:
        """
        add_pitch_mode_list_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "pitch_mode_list" has changed.

            C++ signature :
                void add_pitch_mode_list_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def add_pitch_mode_listener(self, listener: Callable) -> None:
        """
        add_pitch_mode_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "pitch_mode" has changed.

            C++ signature :
                void add_pitch_mode_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def add_polyphony_listener(self, listener: Callable) -> None:
        """
        add_polyphony_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "polyphony" has changed.

            C++ signature :
                void add_polyphony_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def frequency_dial_mode_has_listener(self, listener: Callable) -> bool:
        """
        frequency_dial_mode_has_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "frequency_dial_mode".

            C++ signature :
                bool frequency_dial_mode_has_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def frequency_dial_mode_list_has_listener(self, listener: Callable) -> bool:
        """
        frequency_dial_mode_list_has_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "frequency_dial_mode_list".

            C++ signature :
                bool frequency_dial_mode_list_has_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def is_active_has_listener(self, listener: Callable) -> bool:
        """
        is_active_has_listener( (Device)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "is_active".

            C++ signature :
                bool is_active_has_listener(TPyHandle<ADevice>,boost::python::api::object)
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

    def midi_gate_has_listener(self, listener: Callable) -> bool:
        """
        midi_gate_has_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "midi_gate".

            C++ signature :
                bool midi_gate_has_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def midi_gate_list_has_listener(self, listener: Callable) -> bool:
        """
        midi_gate_list_has_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "midi_gate_list".

            C++ signature :
                bool midi_gate_list_has_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def mod_mode_has_listener(self, listener: Callable) -> bool:
        """
        mod_mode_has_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "mod_mode".

            C++ signature :
                bool mod_mode_has_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def mod_mode_list_has_listener(self, listener: Callable) -> bool:
        """
        mod_mode_list_has_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "mod_mode_list".

            C++ signature :
                bool mod_mode_list_has_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def mono_poly_has_listener(self, listener: Callable) -> bool:
        """
        mono_poly_has_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "mono_poly".

            C++ signature :
                bool mono_poly_has_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def mono_poly_list_has_listener(self, listener: Callable) -> bool:
        """
        mono_poly_list_has_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "mono_poly_list".

            C++ signature :
                bool mono_poly_list_has_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def name_has_listener(self, listener: Callable) -> bool:
        """
        name_has_listener( (Device)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "name".

            C++ signature :
                bool name_has_listener(TPyHandle<ADevice>,boost::python::api::object)
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
        pitch_bend_range_has_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "pitch_bend_range".

            C++ signature :
                bool pitch_bend_range_has_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def pitch_mode_has_listener(self, listener: Callable) -> bool:
        """
        pitch_mode_has_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "pitch_mode".

            C++ signature :
                bool pitch_mode_has_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def pitch_mode_list_has_listener(self, listener: Callable) -> bool:
        """
        pitch_mode_list_has_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "pitch_mode_list".

            C++ signature :
                bool pitch_mode_list_has_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def polyphony_has_listener(self, listener: Callable) -> bool:
        """
        polyphony_has_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "polyphony".

            C++ signature :
                bool polyphony_has_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def remove_frequency_dial_mode_list_listener(self, listener: Callable) -> None:
        """
        remove_frequency_dial_mode_list_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "frequency_dial_mode_list".

            C++ signature :
                void remove_frequency_dial_mode_list_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def remove_frequency_dial_mode_listener(self, listener: Callable) -> None:
        """
        remove_frequency_dial_mode_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "frequency_dial_mode".

            C++ signature :
                void remove_frequency_dial_mode_listener(TTransmuteDevicePyHandle,boost::python::api::object)
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

    def remove_midi_gate_list_listener(self, listener: Callable) -> None:
        """
        remove_midi_gate_list_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "midi_gate_list".

            C++ signature :
                void remove_midi_gate_list_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def remove_midi_gate_listener(self, listener: Callable) -> None:
        """
        remove_midi_gate_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "midi_gate".

            C++ signature :
                void remove_midi_gate_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def remove_mod_mode_list_listener(self, listener: Callable) -> None:
        """
        remove_mod_mode_list_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "mod_mode_list".

            C++ signature :
                void remove_mod_mode_list_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def remove_mod_mode_listener(self, listener: Callable) -> None:
        """
        remove_mod_mode_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "mod_mode".

            C++ signature :
                void remove_mod_mode_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def remove_mono_poly_list_listener(self, listener: Callable) -> None:
        """
        remove_mono_poly_list_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "mono_poly_list".

            C++ signature :
                void remove_mono_poly_list_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def remove_mono_poly_listener(self, listener: Callable) -> None:
        """
        remove_mono_poly_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "mono_poly".

            C++ signature :
                void remove_mono_poly_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def remove_name_listener(self, listener: Callable) -> None:
        """
        remove_name_listener( (Device)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "name".

            C++ signature :
                void remove_name_listener(TPyHandle<ADevice>,boost::python::api::object)
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
        remove_pitch_bend_range_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "pitch_bend_range".

            C++ signature :
                void remove_pitch_bend_range_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def remove_pitch_mode_list_listener(self, listener: Callable) -> None:
        """
        remove_pitch_mode_list_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "pitch_mode_list".

            C++ signature :
                void remove_pitch_mode_list_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def remove_pitch_mode_listener(self, listener: Callable) -> None:
        """
        remove_pitch_mode_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "pitch_mode".

            C++ signature :
                void remove_pitch_mode_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def remove_polyphony_listener(self, listener: Callable) -> None:
        """
        remove_polyphony_listener( (SpectralResonatorDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "polyphony".

            C++ signature :
                void remove_polyphony_listener(TTransmuteDevicePyHandle,boost::python::api::object)
        """

    def save_preset_to_compare_ab_slot(self) -> None:
        """
        save_preset_to_compare_ab_slot( (Device)arg1) -> None :
            Saves the current state of the device to the compare AB slot. Only relevant if can_compare_ab, otherwise throws.

            C++ signature :
                void save_preset_to_compare_ab_slot(TPyHandle<ADevice>)
        """

    def store_chosen_bank(self, arg2: int, arg3: int) -> None:
        """
        store_chosen_bank( (Device)arg1, (int)arg2, (int)arg3) -> None :
            Set the selected bank in the device for persistency.

            C++ signature :
                void store_chosen_bank(TPyHandle<ADevice>,int,int)
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
    def frequency_dial_mode(self) -> Any:
        """
        Return the current frequency dial mode index
        """

    @property
    def frequency_dial_mode_list(self) -> Any:
        """
        Return the current frequency dial mode list
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
    def midi_gate(self) -> Any:
        """
        Return the current midi gate index
        """

    @property
    def midi_gate_list(self) -> Any:
        """
        Return the current midi gate list
        """

    @property
    def mod_mode(self) -> Any:
        """
        Return the current mod mode index
        """

    @property
    def mod_mode_list(self) -> Any:
        """
        Return the current mod mode list
        """

    @property
    def mono_poly(self) -> Any:
        """
        Return the current mono poly mode index
        """

    @property
    def mono_poly_list(self) -> Any:
        """
        Return the current mono poly mode list
        """

    @property
    def name(self) -> str:
        """
        Return access to the name of the device.
        """

    @property
    def parameters(self) -> list[DeviceParameter]:
        """
        Const access to the list of available automatable parameters for this device.
        """

    @property
    def pitch_bend_range(self) -> Any:
        """
        Return the current pitch bend range
        """

    @property
    def pitch_mode(self) -> Any:
        """
        Return the current pitch mode index
        """

    @property
    def pitch_mode_list(self) -> Any:
        """
        Return the current pitch mode list
        """

    @property
    def polyphony(self) -> Any:
        """
        Return the current polyphony
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

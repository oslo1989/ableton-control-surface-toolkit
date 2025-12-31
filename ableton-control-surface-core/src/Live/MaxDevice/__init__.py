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
from Live.WavetableDevice import *


class MaxDevice:
    """
    This class represents a Max for Live device.
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

    def add_audio_inputs_listener(self, listener: Callable) -> None:
        """
        add_audio_inputs_listener( (MaxDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "audio_inputs" has changed.

            C++ signature :
                void add_audio_inputs_listener(TMaxDevicePyHandle,boost::python::api::object)
        """

    def add_audio_outputs_listener(self, listener: Callable) -> None:
        """
        add_audio_outputs_listener( (MaxDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "audio_outputs" has changed.

            C++ signature :
                void add_audio_outputs_listener(TMaxDevicePyHandle,boost::python::api::object)
        """

    def add_bank_parameters_changed_listener(self, listener: Callable) -> None:
        """
        add_bank_parameters_changed_listener( (MaxDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "bank_parameters_changed" has changed.

            C++ signature :
                void add_bank_parameters_changed_listener(TMaxDevicePyHandle,boost::python::api::object)
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

    def add_midi_inputs_listener(self, listener: Callable) -> None:
        """
        add_midi_inputs_listener( (MaxDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "midi_inputs" has changed.

            C++ signature :
                void add_midi_inputs_listener(TMaxDevicePyHandle,boost::python::api::object)
        """

    def add_midi_outputs_listener(self, listener: Callable) -> None:
        """
        add_midi_outputs_listener( (MaxDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "midi_outputs" has changed.

            C++ signature :
                void add_midi_outputs_listener(TMaxDevicePyHandle,boost::python::api::object)
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

    def audio_inputs_has_listener(self, listener: Callable) -> bool:
        """
        audio_inputs_has_listener( (MaxDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "audio_inputs".

            C++ signature :
                bool audio_inputs_has_listener(TMaxDevicePyHandle,boost::python::api::object)
        """

    def audio_outputs_has_listener(self, listener: Callable) -> bool:
        """
        audio_outputs_has_listener( (MaxDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "audio_outputs".

            C++ signature :
                bool audio_outputs_has_listener(TMaxDevicePyHandle,boost::python::api::object)
        """

    def bank_parameters_changed_has_listener(self, listener: Callable) -> bool:
        """
        bank_parameters_changed_has_listener( (MaxDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "bank_parameters_changed".

            C++ signature :
                bool bank_parameters_changed_has_listener(TMaxDevicePyHandle,boost::python::api::object)
        """

    def get_bank_count(self) -> int:
        """
        get_bank_count( (MaxDevice)arg1) -> int :
            Get the number of parameter banks. This is related to hardware control surfaces.

            C++ signature :
                int get_bank_count(TMaxDevicePyHandle)
        """

    def get_bank_name(self, arg2: int) -> str:
        """
        get_bank_name( (MaxDevice)arg1, (int)arg2) -> str :
            Get the name of a parameter bank given by index. This is related to hardware control surfaces.

            C++ signature :
                TString get_bank_name(TMaxDevicePyHandle,int)
        """

    def get_bank_parameters(self, arg2: int) -> list:
        """
        get_bank_parameters( (MaxDevice)arg1, (int)arg2) -> list :
            Get the indices of parameters of the given bank index. Empty slots are marked as -1. Bank index -1 refers to the best-of bank. This function is related to hardware control surfaces.

            C++ signature :
                boost::python::list get_bank_parameters(TMaxDevicePyHandle,int)
        """

    def get_value_item_icons(self, arg2: object) -> list:
        """
        get_value_item_icons( (MaxDevice)arg1, (DeviceParameter)arg2) -> list :
            Get a list of icon identifier strings for a list parameter's values.An empty string is given where no icon should be displayed.An empty list is given when no icons should be displayed.This is related to hardware control surfaces.

            C++ signature :
                boost::python::list get_value_item_icons(TMaxDevicePyHandle,TPyHandle<ATimeableValue>)
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

    def midi_inputs_has_listener(self, listener: Callable) -> bool:
        """
        midi_inputs_has_listener( (MaxDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "midi_inputs".

            C++ signature :
                bool midi_inputs_has_listener(TMaxDevicePyHandle,boost::python::api::object)
        """

    def midi_outputs_has_listener(self, listener: Callable) -> bool:
        """
        midi_outputs_has_listener( (MaxDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "midi_outputs".

            C++ signature :
                bool midi_outputs_has_listener(TMaxDevicePyHandle,boost::python::api::object)
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

    def remove_audio_inputs_listener(self, listener: Callable) -> None:
        """
        remove_audio_inputs_listener( (MaxDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "audio_inputs".

            C++ signature :
                void remove_audio_inputs_listener(TMaxDevicePyHandle,boost::python::api::object)
        """

    def remove_audio_outputs_listener(self, listener: Callable) -> None:
        """
        remove_audio_outputs_listener( (MaxDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "audio_outputs".

            C++ signature :
                void remove_audio_outputs_listener(TMaxDevicePyHandle,boost::python::api::object)
        """

    def remove_bank_parameters_changed_listener(self, listener: Callable) -> None:
        """
        remove_bank_parameters_changed_listener( (MaxDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "bank_parameters_changed".

            C++ signature :
                void remove_bank_parameters_changed_listener(TMaxDevicePyHandle,boost::python::api::object)
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

    def remove_midi_inputs_listener(self, listener: Callable) -> None:
        """
        remove_midi_inputs_listener( (MaxDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "midi_inputs".

            C++ signature :
                void remove_midi_inputs_listener(TMaxDevicePyHandle,boost::python::api::object)
        """

    def remove_midi_outputs_listener(self, listener: Callable) -> None:
        """
        remove_midi_outputs_listener( (MaxDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "midi_outputs".

            C++ signature :
                void remove_midi_outputs_listener(TMaxDevicePyHandle,boost::python::api::object)
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
    def audio_inputs(self) -> Any:
        """
        Const access to a list of all audio inputs of the device.
        """

    @property
    def audio_outputs(self) -> Any:
        """
        Const access to a list of all audio outputs of the device.
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
    def midi_inputs(self) -> Any:
        """
        Const access to a list of all midi outputs of the device.
        """

    @property
    def midi_outputs(self) -> Any:
        """
        Const access to a list of all midi outputs of the device.
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
    def type(self) -> Any:
        """
        Return the type of the device.
        """

    @property
    def view(self) -> View:
        """
        Representing the view aspects of a device.
        """

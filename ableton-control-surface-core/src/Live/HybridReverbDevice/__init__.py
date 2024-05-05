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


class HybridReverbDevice:
    """
    This class represents a Hybrid Reverb device.
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

    def add_ir_attack_time_listener(self, listener: Callable) -> None:
        """
        add_ir_attack_time_listener( (HybridReverbDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "ir_attack_time" has changed.

            C++ signature :
                void add_ir_attack_time_listener(THybridReverbDevicePyHandle,boost::python::api::object)
        """

    def add_ir_category_index_listener(self, listener: Callable) -> None:
        """
        add_ir_category_index_listener( (HybridReverbDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "ir_category_index" has changed.

            C++ signature :
                void add_ir_category_index_listener(THybridReverbDevicePyHandle,boost::python::api::object)
        """

    def add_ir_decay_time_listener(self, listener: Callable) -> None:
        """
        add_ir_decay_time_listener( (HybridReverbDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "ir_decay_time" has changed.

            C++ signature :
                void add_ir_decay_time_listener(THybridReverbDevicePyHandle,boost::python::api::object)
        """

    def add_ir_file_index_listener(self, listener: Callable) -> None:
        """
        add_ir_file_index_listener( (HybridReverbDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "ir_file_index" has changed.

            C++ signature :
                void add_ir_file_index_listener(THybridReverbDevicePyHandle,boost::python::api::object)
        """

    def add_ir_file_list_listener(self, listener: Callable) -> None:
        """
        add_ir_file_list_listener( (HybridReverbDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "ir_file_list" has changed.

            C++ signature :
                void add_ir_file_list_listener(THybridReverbDevicePyHandle,boost::python::api::object)
        """

    def add_ir_size_factor_listener(self, listener: Callable) -> None:
        """
        add_ir_size_factor_listener( (HybridReverbDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "ir_size_factor" has changed.

            C++ signature :
                void add_ir_size_factor_listener(THybridReverbDevicePyHandle,boost::python::api::object)
        """

    def add_ir_time_shaping_on_listener(self, listener: Callable) -> None:
        """
        add_ir_time_shaping_on_listener( (HybridReverbDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "ir_time_shaping_on" has changed.

            C++ signature :
                void add_ir_time_shaping_on_listener(THybridReverbDevicePyHandle,boost::python::api::object)
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

    def ir_attack_time_has_listener(self, listener: Callable) -> bool:
        """
        ir_attack_time_has_listener( (HybridReverbDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "ir_attack_time".

            C++ signature :
                bool ir_attack_time_has_listener(THybridReverbDevicePyHandle,boost::python::api::object)
        """

    def ir_category_index_has_listener(self, listener: Callable) -> bool:
        """
        ir_category_index_has_listener( (HybridReverbDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "ir_category_index".

            C++ signature :
                bool ir_category_index_has_listener(THybridReverbDevicePyHandle,boost::python::api::object)
        """

    def ir_decay_time_has_listener(self, listener: Callable) -> bool:
        """
        ir_decay_time_has_listener( (HybridReverbDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "ir_decay_time".

            C++ signature :
                bool ir_decay_time_has_listener(THybridReverbDevicePyHandle,boost::python::api::object)
        """

    def ir_file_index_has_listener(self, listener: Callable) -> bool:
        """
        ir_file_index_has_listener( (HybridReverbDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "ir_file_index".

            C++ signature :
                bool ir_file_index_has_listener(THybridReverbDevicePyHandle,boost::python::api::object)
        """

    def ir_file_list_has_listener(self, listener: Callable) -> bool:
        """
        ir_file_list_has_listener( (HybridReverbDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "ir_file_list".

            C++ signature :
                bool ir_file_list_has_listener(THybridReverbDevicePyHandle,boost::python::api::object)
        """

    def ir_size_factor_has_listener(self, listener: Callable) -> bool:
        """
        ir_size_factor_has_listener( (HybridReverbDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "ir_size_factor".

            C++ signature :
                bool ir_size_factor_has_listener(THybridReverbDevicePyHandle,boost::python::api::object)
        """

    def ir_time_shaping_on_has_listener(self, listener: Callable) -> bool:
        """
        ir_time_shaping_on_has_listener( (HybridReverbDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "ir_time_shaping_on".

            C++ signature :
                bool ir_time_shaping_on_has_listener(THybridReverbDevicePyHandle,boost::python::api::object)
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

    def remove_ir_attack_time_listener(self, listener: Callable) -> None:
        """
        remove_ir_attack_time_listener( (HybridReverbDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "ir_attack_time".

            C++ signature :
                void remove_ir_attack_time_listener(THybridReverbDevicePyHandle,boost::python::api::object)
        """

    def remove_ir_category_index_listener(self, listener: Callable) -> None:
        """
        remove_ir_category_index_listener( (HybridReverbDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "ir_category_index".

            C++ signature :
                void remove_ir_category_index_listener(THybridReverbDevicePyHandle,boost::python::api::object)
        """

    def remove_ir_decay_time_listener(self, listener: Callable) -> None:
        """
        remove_ir_decay_time_listener( (HybridReverbDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "ir_decay_time".

            C++ signature :
                void remove_ir_decay_time_listener(THybridReverbDevicePyHandle,boost::python::api::object)
        """

    def remove_ir_file_index_listener(self, listener: Callable) -> None:
        """
        remove_ir_file_index_listener( (HybridReverbDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "ir_file_index".

            C++ signature :
                void remove_ir_file_index_listener(THybridReverbDevicePyHandle,boost::python::api::object)
        """

    def remove_ir_file_list_listener(self, listener: Callable) -> None:
        """
        remove_ir_file_list_listener( (HybridReverbDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "ir_file_list".

            C++ signature :
                void remove_ir_file_list_listener(THybridReverbDevicePyHandle,boost::python::api::object)
        """

    def remove_ir_size_factor_listener(self, listener: Callable) -> None:
        """
        remove_ir_size_factor_listener( (HybridReverbDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "ir_size_factor".

            C++ signature :
                void remove_ir_size_factor_listener(THybridReverbDevicePyHandle,boost::python::api::object)
        """

    def remove_ir_time_shaping_on_listener(self, listener: Callable) -> None:
        """
        remove_ir_time_shaping_on_listener( (HybridReverbDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "ir_time_shaping_on".

            C++ signature :
                void remove_ir_time_shaping_on_listener(THybridReverbDevicePyHandle,boost::python::api::object)
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

    def store_chosen_bank(self, arg2: int, arg3: int) -> None:
        """
        store_chosen_bank( (Device)arg1, (int)arg2, (int)arg3) -> None :
            Set the selected bank in the device for persistency.

            C++ signature :
                void store_chosen_bank(TPyHandle<ADevice>,int,int)
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
    def ir_attack_time(self) -> Any:
        """
        Return the current IrAttackTime
        """

    @property
    def ir_category_index(self) -> Any:
        """
        Return the current IR category index
        """

    @property
    def ir_category_list(self) -> Any:
        """
        Return the current IR categories list
        """

    @property
    def ir_decay_time(self) -> Any:
        """
        Return the current IrDecayTime
        """

    @property
    def ir_file_index(self) -> Any:
        """
        Return the current IR file index
        """

    @property
    def ir_file_list(self) -> Any:
        """
        Return the current IR file list
        """

    @property
    def ir_size_factor(self) -> Any:
        """
        Return the current IrSizeFactor
        """

    @property
    def ir_time_shaping_on(self) -> Any:
        """
        Return the current IrTimeShapingOn
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

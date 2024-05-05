from __future__ import annotations

from typing import Any, Callable

from Live import *
from Live.Application import *
from Live.Base import *
from Live.Browser import *
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
from Live.Song import *
from Live.SpectralResonatorDevice import *
from Live.Track import *
from Live.WavetableDevice import *


class CcControlDevice:
    """
    This class represents a CcControl device.
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

    def add_custom_bool_target_listener(self, listener: Callable) -> None:
        """
        add_custom_bool_target_listener( (CcControlDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "custom_bool_target" has changed.

            C++ signature :
                void add_custom_bool_target_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def add_custom_float_target_0_listener(self, listener: Callable) -> None:
        """
        add_custom_float_target_0_listener( (CcControlDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "custom_float_target_0" has changed.

            C++ signature :
                void add_custom_float_target_0_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def add_custom_float_target_10_listener(self, listener: Callable) -> None:
        """
        add_custom_float_target_10_listener( (CcControlDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "custom_float_target_10" has changed.

            C++ signature :
                void add_custom_float_target_10_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def add_custom_float_target_11_listener(self, listener: Callable) -> None:
        """
        add_custom_float_target_11_listener( (CcControlDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "custom_float_target_11" has changed.

            C++ signature :
                void add_custom_float_target_11_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def add_custom_float_target_1_listener(self, listener: Callable) -> None:
        """
        add_custom_float_target_1_listener( (CcControlDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "custom_float_target_1" has changed.

            C++ signature :
                void add_custom_float_target_1_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def add_custom_float_target_2_listener(self, listener: Callable) -> None:
        """
        add_custom_float_target_2_listener( (CcControlDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "custom_float_target_2" has changed.

            C++ signature :
                void add_custom_float_target_2_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def add_custom_float_target_3_listener(self, listener: Callable) -> None:
        """
        add_custom_float_target_3_listener( (CcControlDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "custom_float_target_3" has changed.

            C++ signature :
                void add_custom_float_target_3_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def add_custom_float_target_4_listener(self, listener: Callable) -> None:
        """
        add_custom_float_target_4_listener( (CcControlDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "custom_float_target_4" has changed.

            C++ signature :
                void add_custom_float_target_4_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def add_custom_float_target_5_listener(self, listener: Callable) -> None:
        """
        add_custom_float_target_5_listener( (CcControlDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "custom_float_target_5" has changed.

            C++ signature :
                void add_custom_float_target_5_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def add_custom_float_target_6_listener(self, listener: Callable) -> None:
        """
        add_custom_float_target_6_listener( (CcControlDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "custom_float_target_6" has changed.

            C++ signature :
                void add_custom_float_target_6_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def add_custom_float_target_7_listener(self, listener: Callable) -> None:
        """
        add_custom_float_target_7_listener( (CcControlDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "custom_float_target_7" has changed.

            C++ signature :
                void add_custom_float_target_7_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def add_custom_float_target_8_listener(self, listener: Callable) -> None:
        """
        add_custom_float_target_8_listener( (CcControlDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "custom_float_target_8" has changed.

            C++ signature :
                void add_custom_float_target_8_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def add_custom_float_target_9_listener(self, listener: Callable) -> None:
        """
        add_custom_float_target_9_listener( (CcControlDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "custom_float_target_9" has changed.

            C++ signature :
                void add_custom_float_target_9_listener(TCcControlDevicePyHandle,boost::python::api::object)
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

    def custom_bool_target_has_listener(self, listener: Callable) -> bool:
        """
        custom_bool_target_has_listener( (CcControlDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "custom_bool_target".

            C++ signature :
                bool custom_bool_target_has_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def custom_float_target_0_has_listener(self, listener: Callable) -> bool:
        """
        custom_float_target_0_has_listener( (CcControlDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "custom_float_target_0".

            C++ signature :
                bool custom_float_target_0_has_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def custom_float_target_10_has_listener(self, listener: Callable) -> bool:
        """
        custom_float_target_10_has_listener( (CcControlDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "custom_float_target_10".

            C++ signature :
                bool custom_float_target_10_has_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def custom_float_target_11_has_listener(self, listener: Callable) -> bool:
        """
        custom_float_target_11_has_listener( (CcControlDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "custom_float_target_11".

            C++ signature :
                bool custom_float_target_11_has_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def custom_float_target_1_has_listener(self, listener: Callable) -> bool:
        """
        custom_float_target_1_has_listener( (CcControlDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "custom_float_target_1".

            C++ signature :
                bool custom_float_target_1_has_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def custom_float_target_2_has_listener(self, listener: Callable) -> bool:
        """
        custom_float_target_2_has_listener( (CcControlDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "custom_float_target_2".

            C++ signature :
                bool custom_float_target_2_has_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def custom_float_target_3_has_listener(self, listener: Callable) -> bool:
        """
        custom_float_target_3_has_listener( (CcControlDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "custom_float_target_3".

            C++ signature :
                bool custom_float_target_3_has_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def custom_float_target_4_has_listener(self, listener: Callable) -> bool:
        """
        custom_float_target_4_has_listener( (CcControlDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "custom_float_target_4".

            C++ signature :
                bool custom_float_target_4_has_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def custom_float_target_5_has_listener(self, listener: Callable) -> bool:
        """
        custom_float_target_5_has_listener( (CcControlDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "custom_float_target_5".

            C++ signature :
                bool custom_float_target_5_has_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def custom_float_target_6_has_listener(self, listener: Callable) -> bool:
        """
        custom_float_target_6_has_listener( (CcControlDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "custom_float_target_6".

            C++ signature :
                bool custom_float_target_6_has_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def custom_float_target_7_has_listener(self, listener: Callable) -> bool:
        """
        custom_float_target_7_has_listener( (CcControlDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "custom_float_target_7".

            C++ signature :
                bool custom_float_target_7_has_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def custom_float_target_8_has_listener(self, listener: Callable) -> bool:
        """
        custom_float_target_8_has_listener( (CcControlDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "custom_float_target_8".

            C++ signature :
                bool custom_float_target_8_has_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def custom_float_target_9_has_listener(self, listener: Callable) -> bool:
        """
        custom_float_target_9_has_listener( (CcControlDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "custom_float_target_9".

            C++ signature :
                bool custom_float_target_9_has_listener(TCcControlDevicePyHandle,boost::python::api::object)
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

    def remove_custom_bool_target_listener(self, listener: Callable) -> None:
        """
        remove_custom_bool_target_listener( (CcControlDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "custom_bool_target".

            C++ signature :
                void remove_custom_bool_target_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def remove_custom_float_target_0_listener(self, listener: Callable) -> None:
        """
        remove_custom_float_target_0_listener( (CcControlDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "custom_float_target_0".

            C++ signature :
                void remove_custom_float_target_0_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def remove_custom_float_target_10_listener(self, listener: Callable) -> None:
        """
        remove_custom_float_target_10_listener( (CcControlDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "custom_float_target_10".

            C++ signature :
                void remove_custom_float_target_10_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def remove_custom_float_target_11_listener(self, listener: Callable) -> None:
        """
        remove_custom_float_target_11_listener( (CcControlDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "custom_float_target_11".

            C++ signature :
                void remove_custom_float_target_11_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def remove_custom_float_target_1_listener(self, listener: Callable) -> None:
        """
        remove_custom_float_target_1_listener( (CcControlDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "custom_float_target_1".

            C++ signature :
                void remove_custom_float_target_1_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def remove_custom_float_target_2_listener(self, listener: Callable) -> None:
        """
        remove_custom_float_target_2_listener( (CcControlDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "custom_float_target_2".

            C++ signature :
                void remove_custom_float_target_2_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def remove_custom_float_target_3_listener(self, listener: Callable) -> None:
        """
        remove_custom_float_target_3_listener( (CcControlDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "custom_float_target_3".

            C++ signature :
                void remove_custom_float_target_3_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def remove_custom_float_target_4_listener(self, listener: Callable) -> None:
        """
        remove_custom_float_target_4_listener( (CcControlDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "custom_float_target_4".

            C++ signature :
                void remove_custom_float_target_4_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def remove_custom_float_target_5_listener(self, listener: Callable) -> None:
        """
        remove_custom_float_target_5_listener( (CcControlDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "custom_float_target_5".

            C++ signature :
                void remove_custom_float_target_5_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def remove_custom_float_target_6_listener(self, listener: Callable) -> None:
        """
        remove_custom_float_target_6_listener( (CcControlDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "custom_float_target_6".

            C++ signature :
                void remove_custom_float_target_6_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def remove_custom_float_target_7_listener(self, listener: Callable) -> None:
        """
        remove_custom_float_target_7_listener( (CcControlDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "custom_float_target_7".

            C++ signature :
                void remove_custom_float_target_7_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def remove_custom_float_target_8_listener(self, listener: Callable) -> None:
        """
        remove_custom_float_target_8_listener( (CcControlDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "custom_float_target_8".

            C++ signature :
                void remove_custom_float_target_8_listener(TCcControlDevicePyHandle,boost::python::api::object)
        """

    def remove_custom_float_target_9_listener(self, listener: Callable) -> None:
        """
        remove_custom_float_target_9_listener( (CcControlDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "custom_float_target_9".

            C++ signature :
                void remove_custom_float_target_9_listener(TCcControlDevicePyHandle,boost::python::api::object)
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

    def resend(self) -> None:
        """
        resend( (CcControlDevice)self) -> None :
            Resend all CC values.

            C++ signature :
                void resend(TCcControlDevicePyHandle)
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
    def custom_bool_target(self) -> Any:
        """
        Return the custom bool target
        """

    @property
    def custom_bool_target_list(self) -> Any:
        """
        Return the custom bool target list
        """

    @property
    def custom_float_target_0(self) -> Any:
        """
        Return the custom float target 0
        """

    @property
    def custom_float_target_0_list(self) -> Any:
        """
        Return the custom float target 0 list
        """

    @property
    def custom_float_target_1(self) -> Any:
        """
        Return the custom float target 1
        """

    @property
    def custom_float_target_10(self) -> Any:
        """
        Return the custom float target 10
        """

    @property
    def custom_float_target_10_list(self) -> Any:
        """
        Return the custom float target 10 list
        """

    @property
    def custom_float_target_11(self) -> Any:
        """
        Return the custom float target 11
        """

    @property
    def custom_float_target_11_list(self) -> Any:
        """
        Return the custom float target 11 list
        """

    @property
    def custom_float_target_1_list(self) -> Any:
        """
        Return the custom float target 1 list
        """

    @property
    def custom_float_target_2(self) -> Any:
        """
        Return the custom float target 2
        """

    @property
    def custom_float_target_2_list(self) -> Any:
        """
        Return the custom float target 2 list
        """

    @property
    def custom_float_target_3(self) -> Any:
        """
        Return the custom float target 3
        """

    @property
    def custom_float_target_3_list(self) -> Any:
        """
        Return the custom float target 3 list
        """

    @property
    def custom_float_target_4(self) -> Any:
        """
        Return the custom float target 4
        """

    @property
    def custom_float_target_4_list(self) -> Any:
        """
        Return the custom float target 4 list
        """

    @property
    def custom_float_target_5(self) -> Any:
        """
        Return the custom float target 5
        """

    @property
    def custom_float_target_5_list(self) -> Any:
        """
        Return the custom float target 5 list
        """

    @property
    def custom_float_target_6(self) -> Any:
        """
        Return the custom float target 6
        """

    @property
    def custom_float_target_6_list(self) -> Any:
        """
        Return the custom float target 6 list
        """

    @property
    def custom_float_target_7(self) -> Any:
        """
        Return the custom float target 7
        """

    @property
    def custom_float_target_7_list(self) -> Any:
        """
        Return the custom float target 7 list
        """

    @property
    def custom_float_target_8(self) -> Any:
        """
        Return the custom float target 8
        """

    @property
    def custom_float_target_8_list(self) -> Any:
        """
        Return the custom float target 8 list
        """

    @property
    def custom_float_target_9(self) -> Any:
        """
        Return the custom float target 9
        """

    @property
    def custom_float_target_9_list(self) -> Any:
        """
        Return the custom float target 9 list
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

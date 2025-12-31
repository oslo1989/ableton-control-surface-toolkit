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


class RackDevice:
    """
    This class represents a Rack device.
    """

    class View:
        """
        Representing the view aspects of a rack device.
        """

        def add_drum_pads_scroll_position_listener(self, listener: Callable) -> None:
            """
            add_drum_pads_scroll_position_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "drum_pads_scroll_position" has changed.

                C++ signature :
                    void add_drum_pads_scroll_position_listener(TRackDevicePyViewData,boost::python::api::object)
            """

        def add_is_collapsed_listener(self, listener: Callable) -> None:
            """
            add_is_collapsed_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "is_collapsed" has changed.

                C++ signature :
                    void add_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
            """

        def add_is_showing_chain_devices_listener(self, listener: Callable) -> None:
            """
            add_is_showing_chain_devices_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "is_showing_chain_devices" has changed.

                C++ signature :
                    void add_is_showing_chain_devices_listener(TRackDevicePyViewData,boost::python::api::object)
            """

        def add_selected_chain_listener(self, listener: Callable) -> None:
            """
            add_selected_chain_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "selected_chain" has changed.

                C++ signature :
                    void add_selected_chain_listener(TRackDevicePyViewData,boost::python::api::object)
            """

        def add_selected_drum_pad_listener(self, listener: Callable) -> None:
            """
            add_selected_drum_pad_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "selected_drum_pad" has changed.

                C++ signature :
                    void add_selected_drum_pad_listener(TRackDevicePyViewData,boost::python::api::object)
            """

        def drum_pads_scroll_position_has_listener(self, listener: Callable) -> bool:
            """
            drum_pads_scroll_position_has_listener( (View)arg1, (object)arg2) -> bool :
                Returns true, if the given listener function or method is connected
                to the property "drum_pads_scroll_position".

                C++ signature :
                    bool drum_pads_scroll_position_has_listener(TRackDevicePyViewData,boost::python::api::object)
            """

        def is_collapsed_has_listener(self, listener: Callable) -> bool:
            """
            is_collapsed_has_listener( (View)arg1, (object)arg2) -> bool :
                Returns true, if the given listener function or method is connected
                to the property "is_collapsed".

                C++ signature :
                    bool is_collapsed_has_listener(TPyViewData<ADevice>,boost::python::api::object)
            """

        def is_showing_chain_devices_has_listener(self, listener: Callable) -> bool:
            """
            is_showing_chain_devices_has_listener( (View)arg1, (object)arg2) -> bool :
                Returns true, if the given listener function or method is connected
                to the property "is_showing_chain_devices".

                C++ signature :
                    bool is_showing_chain_devices_has_listener(TRackDevicePyViewData,boost::python::api::object)
            """

        def remove_drum_pads_scroll_position_listener(self, listener: Callable) -> None:
            """
            remove_drum_pads_scroll_position_listener( (View)arg1, (object)arg2) -> None :
                Remove a previously set listener function or method from
                property "drum_pads_scroll_position".

                C++ signature :
                    void remove_drum_pads_scroll_position_listener(TRackDevicePyViewData,boost::python::api::object)
            """

        def remove_is_collapsed_listener(self, listener: Callable) -> None:
            """
            remove_is_collapsed_listener( (View)arg1, (object)arg2) -> None :
                Remove a previously set listener function or method from
                property "is_collapsed".

                C++ signature :
                    void remove_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
            """

        def remove_is_showing_chain_devices_listener(self, listener: Callable) -> None:
            """
            remove_is_showing_chain_devices_listener( (View)arg1, (object)arg2) -> None :
                Remove a previously set listener function or method from
                property "is_showing_chain_devices".

                C++ signature :
                    void remove_is_showing_chain_devices_listener(TRackDevicePyViewData,boost::python::api::object)
            """

        def remove_selected_chain_listener(self, listener: Callable) -> None:
            """
            remove_selected_chain_listener( (View)arg1, (object)arg2) -> None :
                Remove a previously set listener function or method from
                property "selected_chain".

                C++ signature :
                    void remove_selected_chain_listener(TRackDevicePyViewData,boost::python::api::object)
            """

        def remove_selected_drum_pad_listener(self, listener: Callable) -> None:
            """
            remove_selected_drum_pad_listener( (View)arg1, (object)arg2) -> None :
                Remove a previously set listener function or method from
                property "selected_drum_pad".

                C++ signature :
                    void remove_selected_drum_pad_listener(TRackDevicePyViewData,boost::python::api::object)
            """

        def selected_chain_has_listener(self, listener: Callable) -> bool:
            """
            selected_chain_has_listener( (View)arg1, (object)arg2) -> bool :
                Returns true, if the given listener function or method is connected
                to the property "selected_chain".

                C++ signature :
                    bool selected_chain_has_listener(TRackDevicePyViewData,boost::python::api::object)
            """

        def selected_drum_pad_has_listener(self, listener: Callable) -> bool:
            """
            selected_drum_pad_has_listener( (View)arg1, (object)arg2) -> bool :
                Returns true, if the given listener function or method is connected
                to the property "selected_drum_pad".

                C++ signature :
                    bool selected_drum_pad_has_listener(TRackDevicePyViewData,boost::python::api::object)
            """

        @property
        def canonical_parent(self) -> Any:
            """
            Get the canonical parent of the View.
            """

        @property
        def drum_pads_scroll_position(self) -> Any:
            """
            Access to the index of the lowest visible row of pads. Throws an exception if can_have_drum_pads is false.
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
        def is_showing_chain_devices(self) -> bool:
            """
            Return whether the devices in the currently selected chain are visible. Throws an exception if can_have_chains is false.
            """

        @property
        def selected_chain(self) -> Any:
            """
            Return access to the currently selected chain.
            """

        @property
        def selected_drum_pad(self) -> Any:
            """
            Return access to the currently selected drum pad. Throws an exception if can_have_drum_pads is false.
            """

    def add_chains_listener(self, listener: Callable) -> None:
        """
        add_chains_listener( (RackDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "chains" has changed.

            C++ signature :
                void add_chains_listener(TRackDevicePyHandle,boost::python::api::object)
        """

    def add_drum_pads_listener(self, listener: Callable) -> None:
        """
        add_drum_pads_listener( (RackDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "drum_pads" has changed.

            C++ signature :
                void add_drum_pads_listener(TRackDevicePyHandle,boost::python::api::object)
        """

    def add_has_drum_pads_listener(self, listener: Callable) -> None:
        """
        add_has_drum_pads_listener( (RackDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "has_drum_pads" has changed.

            C++ signature :
                void add_has_drum_pads_listener(TRackDevicePyHandle,boost::python::api::object)
        """

    def add_has_macro_mappings_listener(self, listener: Callable) -> None:
        """
        add_has_macro_mappings_listener( (RackDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "has_macro_mappings" has changed.

            C++ signature :
                void add_has_macro_mappings_listener(TRackDevicePyHandle,boost::python::api::object)
        """

    def add_is_active_listener(self, listener: Callable) -> None:
        """
        add_is_active_listener( (Device)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "is_active" has changed.

            C++ signature :
                void add_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def add_is_showing_chains_listener(self, listener: Callable) -> None:
        """
        add_is_showing_chains_listener( (RackDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "is_showing_chains" has changed.

            C++ signature :
                void add_is_showing_chains_listener(TRackDevicePyHandle,boost::python::api::object)
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

    def add_macro(self) -> None:
        """
        add_macro( (RackDevice)arg1) -> None :
            Increases the number of visible macro controls in the rack. Throws an exception if the maximum number of macro controls is reached.

            C++ signature :
                void add_macro(TRackDevicePyHandle)
        """

    def add_macros_mapped_listener(self, listener: Callable) -> None:
        """
        add_macros_mapped_listener( (RackDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "macros_mapped" has changed.

            C++ signature :
                void add_macros_mapped_listener(TRackDevicePyHandle,boost::python::api::object)
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

    def add_return_chains_listener(self, listener: Callable) -> None:
        """
        add_return_chains_listener( (RackDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "return_chains" has changed.

            C++ signature :
                void add_return_chains_listener(TRackDevicePyHandle,boost::python::api::object)
        """

    def add_variation_count_listener(self, listener: Callable) -> None:
        """
        add_variation_count_listener( (RackDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "variation_count" has changed.

            C++ signature :
                void add_variation_count_listener(TRackDevicePyHandle,boost::python::api::object)
        """

    def add_visible_drum_pads_listener(self, listener: Callable) -> None:
        """
        add_visible_drum_pads_listener( (RackDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "visible_drum_pads" has changed.

            C++ signature :
                void add_visible_drum_pads_listener(TRackDevicePyHandle,boost::python::api::object)
        """

    def add_visible_macro_count_listener(self, listener: Callable) -> None:
        """
        add_visible_macro_count_listener( (RackDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "visible_macro_count" has changed.

            C++ signature :
                void add_visible_macro_count_listener(TRackDevicePyHandle,boost::python::api::object)
        """

    def chains_has_listener(self, listener: Callable) -> bool:
        """
        chains_has_listener( (RackDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "chains".

            C++ signature :
                bool chains_has_listener(TRackDevicePyHandle,boost::python::api::object)
        """

    def copy_pad(self, arg2: int, arg3: int) -> None:
        """
        copy_pad( (RackDevice)arg1, (int)arg2, (int)arg3) -> None :
            Copies all contents of a drum pad from a source pad into a destination pad. copy_pad(source_index, destination_index) where source_index and destination_index correspond to the note number/index of the drum pad in a drum rack. Throws an exception when the source pad is empty, or when the source or destination indices are not between 0 - 127.

            C++ signature :
                void copy_pad(TRackDevicePyHandle,int,int)
        """

    def delete_selected_variation(self) -> None:
        """
        delete_selected_variation( (Device)arg1) -> None :
            Deletes the currently selected macro variation.Does nothing if there is no selected variation.

            C++ signature :
                void delete_selected_variation(TPyHandle<ADevice>)
        """

    def drum_pads_has_listener(self, listener: Callable) -> bool:
        """
        drum_pads_has_listener( (RackDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "drum_pads".

            C++ signature :
                bool drum_pads_has_listener(TRackDevicePyHandle,boost::python::api::object)
        """

    def has_drum_pads_has_listener(self, listener: Callable) -> bool:
        """
        has_drum_pads_has_listener( (RackDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "has_drum_pads".

            C++ signature :
                bool has_drum_pads_has_listener(TRackDevicePyHandle,boost::python::api::object)
        """

    def has_macro_mappings_has_listener(self, listener: Callable) -> bool:
        """
        has_macro_mappings_has_listener( (RackDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "has_macro_mappings".

            C++ signature :
                bool has_macro_mappings_has_listener(TRackDevicePyHandle,boost::python::api::object)
        """

    def insert_chain(self, Index: int = 0) -> LomObject:
        """
        insert_chain( (RackDevice)arg1 [, (int)Index=-1]) -> LomObject :
            Inserts a new chain, either at the specified index or, if not index was specified, at the end of the chain sequence.

            C++ signature :
                TWeakPtr<TPyHandleBase> insert_chain(TRackDevicePyHandle [,int=-1])
        """

    def is_active_has_listener(self, listener: Callable) -> bool:
        """
        is_active_has_listener( (Device)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "is_active".

            C++ signature :
                bool is_active_has_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def is_showing_chains_has_listener(self, listener: Callable) -> bool:
        """
        is_showing_chains_has_listener( (RackDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "is_showing_chains".

            C++ signature :
                bool is_showing_chains_has_listener(TRackDevicePyHandle,boost::python::api::object)
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

    def macros_mapped_has_listener(self, listener: Callable) -> bool:
        """
        macros_mapped_has_listener( (RackDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "macros_mapped".

            C++ signature :
                bool macros_mapped_has_listener(TRackDevicePyHandle,boost::python::api::object)
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

    def randomize_macros(self) -> None:
        """
        randomize_macros( (RackDevice)arg1) -> None :
            Randomizes the values for all macro controls not excluded from randomization.

            C++ signature :
                void randomize_macros(TRackDevicePyHandle)
        """

    def recall_last_used_variation(self) -> None:
        """
        recall_last_used_variation( (Device)arg1) -> None :
            Recalls the macro variation that was recalled most recently.Does nothing if no variation has been recalled yet.

            C++ signature :
                void recall_last_used_variation(TPyHandle<ADevice>)
        """

    def recall_selected_variation(self) -> None:
        """
        recall_selected_variation( (Device)arg1) -> None :
            Recalls the currently selected macro variation.Does nothing if there are no variations.

            C++ signature :
                void recall_selected_variation(TPyHandle<ADevice>)
        """

    def remove_chains_listener(self, listener: Callable) -> None:
        """
        remove_chains_listener( (RackDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "chains".

            C++ signature :
                void remove_chains_listener(TRackDevicePyHandle,boost::python::api::object)
        """

    def remove_drum_pads_listener(self, listener: Callable) -> None:
        """
        remove_drum_pads_listener( (RackDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "drum_pads".

            C++ signature :
                void remove_drum_pads_listener(TRackDevicePyHandle,boost::python::api::object)
        """

    def remove_has_drum_pads_listener(self, listener: Callable) -> None:
        """
        remove_has_drum_pads_listener( (RackDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "has_drum_pads".

            C++ signature :
                void remove_has_drum_pads_listener(TRackDevicePyHandle,boost::python::api::object)
        """

    def remove_has_macro_mappings_listener(self, listener: Callable) -> None:
        """
        remove_has_macro_mappings_listener( (RackDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "has_macro_mappings".

            C++ signature :
                void remove_has_macro_mappings_listener(TRackDevicePyHandle,boost::python::api::object)
        """

    def remove_is_active_listener(self, listener: Callable) -> None:
        """
        remove_is_active_listener( (Device)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "is_active".

            C++ signature :
                void remove_is_active_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def remove_is_showing_chains_listener(self, listener: Callable) -> None:
        """
        remove_is_showing_chains_listener( (RackDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "is_showing_chains".

            C++ signature :
                void remove_is_showing_chains_listener(TRackDevicePyHandle,boost::python::api::object)
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

    def remove_macro(self) -> None:
        """
        remove_macro( (RackDevice)arg1) -> None :
            Decreases the number of visible macro controls in the rack. Throws an exception if the minimum number of macro controls is reached.

            C++ signature :
                void remove_macro(TRackDevicePyHandle)
        """

    def remove_macros_mapped_listener(self, listener: Callable) -> None:
        """
        remove_macros_mapped_listener( (RackDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "macros_mapped".

            C++ signature :
                void remove_macros_mapped_listener(TRackDevicePyHandle,boost::python::api::object)
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

    def remove_return_chains_listener(self, listener: Callable) -> None:
        """
        remove_return_chains_listener( (RackDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "return_chains".

            C++ signature :
                void remove_return_chains_listener(TRackDevicePyHandle,boost::python::api::object)
        """

    def remove_variation_count_listener(self, listener: Callable) -> None:
        """
        remove_variation_count_listener( (RackDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "variation_count".

            C++ signature :
                void remove_variation_count_listener(TRackDevicePyHandle,boost::python::api::object)
        """

    def remove_visible_drum_pads_listener(self, listener: Callable) -> None:
        """
        remove_visible_drum_pads_listener( (RackDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "visible_drum_pads".

            C++ signature :
                void remove_visible_drum_pads_listener(TRackDevicePyHandle,boost::python::api::object)
        """

    def remove_visible_macro_count_listener(self, listener: Callable) -> None:
        """
        remove_visible_macro_count_listener( (RackDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "visible_macro_count".

            C++ signature :
                void remove_visible_macro_count_listener(TRackDevicePyHandle,boost::python::api::object)
        """

    def return_chains_has_listener(self, listener: Callable) -> bool:
        """
        return_chains_has_listener( (RackDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "return_chains".

            C++ signature :
                bool return_chains_has_listener(TRackDevicePyHandle,boost::python::api::object)
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

    def store_variation(self) -> None:
        """
        store_variation( (Device)arg1) -> None :
            Stores a new variation of the values of all currently mapped macros

            C++ signature :
                void store_variation(TPyHandle<ADevice>)
        """

    def variation_count_has_listener(self, listener: Callable) -> bool:
        """
        variation_count_has_listener( (RackDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "variation_count".

            C++ signature :
                bool variation_count_has_listener(TRackDevicePyHandle,boost::python::api::object)
        """

    def visible_drum_pads_has_listener(self, listener: Callable) -> bool:
        """
        visible_drum_pads_has_listener( (RackDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "visible_drum_pads".

            C++ signature :
                bool visible_drum_pads_has_listener(TRackDevicePyHandle,boost::python::api::object)
        """

    def visible_macro_count_has_listener(self, listener: Callable) -> bool:
        """
        visible_macro_count_has_listener( (RackDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "visible_macro_count".

            C++ signature :
                bool visible_macro_count_has_listener(TRackDevicePyHandle,boost::python::api::object)
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
    def can_show_chains(self) -> bool:
        """
        return True, if this Rack contains a rack instrument device that is capable of showing its chains in session view.
        """

    @property
    def canonical_parent(self) -> Any:
        """
        Get the canonical parent of the Device.
        """

    @property
    def chain_selector(self) -> Any:
        """
        Const access to the chain selector parameter.
        """

    @property
    def chains(self) -> Any:
        """
        Return const access to the list of chains in this device. Throws an exception if can_have_chains is false.
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
    def drum_pads(self) -> Any:
        """
        Return const access to the list of drum pads in this device. Throws an exception if can_have_drum_pads is false.
        """

    @property
    def has_drum_pads(self) -> bool:
        """
        Returns true if the device is a drum rack which has drum pads. Throws an exception if can_have_drum_pads is false.
        """

    @property
    def has_macro_mappings(self) -> bool:
        """
        Returns true if any of the rack's macros are mapped to a parameter.
        """

    @property
    def is_active(self) -> bool:
        """
        Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
        """

    @property
    def is_showing_chains(self) -> bool:
        """
        Returns True, if it is showing chains.
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
    def macros_mapped(self) -> Any:
        """
        A list of booleans, one for each macro parameter, which is True iffthat macro is mapped to something
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
    def return_chains(self) -> Any:
        """
        Return const access to the list of return chains in this device. Throws an exception if can_have_chains is false.
        """

    @property
    def selected_variation_index(self) -> Any:
        """
        Access to the index of the currently selected macro variation.Throws an exception if the index is out of range.
        """

    @property
    def type(self) -> Any:
        """
        Return the type of the device.
        """

    @property
    def variation_count(self) -> Any:
        """
        Access to the number of macro variations currently stored.
        """

    @property
    def view(self) -> View:
        """
        Representing the view aspects of a device.
        """

    @property
    def visible_drum_pads(self) -> Any:
        """
        Return const access to the list of visible drum pads in this device. Throws an exception if can_have_drum_pads is false.
        """

    @property
    def visible_macro_count(self) -> Any:
        """
        Access to the number of macros that are currently visible.
        """

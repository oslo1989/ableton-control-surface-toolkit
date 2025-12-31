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
from Live.WavetableDevice import *


class LooperDevice:
    """
    This class represents a Looper device.
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

    def add_loop_length_listener(self, listener: Callable) -> None:
        """
        add_loop_length_listener( (LooperDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "loop_length" has changed.

            C++ signature :
                void add_loop_length_listener(TLooperDevicePyHandle,boost::python::api::object)
        """

    def add_name_listener(self, listener: Callable) -> None:
        """
        add_name_listener( (Device)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "name" has changed.

            C++ signature :
                void add_name_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def add_overdub_after_record_listener(self, listener: Callable) -> None:
        """
        add_overdub_after_record_listener( (LooperDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "overdub_after_record" has changed.

            C++ signature :
                void add_overdub_after_record_listener(TLooperDevicePyHandle,boost::python::api::object)
        """

    def add_parameters_listener(self, listener: Callable) -> None:
        """
        add_parameters_listener( (Device)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "parameters" has changed.

            C++ signature :
                void add_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def add_record_length_index_listener(self, listener: Callable) -> None:
        """
        add_record_length_index_listener( (LooperDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "record_length_index" has changed.

            C++ signature :
                void add_record_length_index_listener(TLooperDevicePyHandle,boost::python::api::object)
        """

    def add_tempo_listener(self, listener: Callable) -> None:
        """
        add_tempo_listener( (LooperDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "tempo" has changed.

            C++ signature :
                void add_tempo_listener(TLooperDevicePyHandle,boost::python::api::object)
        """

    def clear(self) -> None:
        """
        clear( (LooperDevice)arg1) -> None :
            Erase Looper's recorded content.

            C++ signature :
                void clear(TLooperDevicePyHandle)
        """

    def double_length(self) -> None:
        """
        double_length( (LooperDevice)arg1) -> None :
            Double the length of Looper's buffer.

            C++ signature :
                void double_length(TLooperDevicePyHandle)
        """

    def double_speed(self) -> None:
        """
        double_speed( (LooperDevice)arg1) -> None :
            Double the speed of Looper's playback.

            C++ signature :
                void double_speed(TLooperDevicePyHandle)
        """

    def export_to_clip_slot(self, arg2: object) -> None:
        """
        export_to_clip_slot( (LooperDevice)arg1, (ClipSlot)arg2) -> None :
            Export Looper's content to a Session Clip Slot.

            C++ signature :
                void export_to_clip_slot(TLooperDevicePyHandle,TPyHandle<AGroupAndClipSlotBase>)
        """

    def half_length(self) -> None:
        """
        half_length( (LooperDevice)arg1) -> None :
            Halve the length of Looper's buffer.

            C++ signature :
                void half_length(TLooperDevicePyHandle)
        """

    def half_speed(self) -> None:
        """
        half_speed( (LooperDevice)arg1) -> None :
            Halve the speed of Looper's playback.

            C++ signature :
                void half_speed(TLooperDevicePyHandle)
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

    def loop_length_has_listener(self, listener: Callable) -> bool:
        """
        loop_length_has_listener( (LooperDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "loop_length".

            C++ signature :
                bool loop_length_has_listener(TLooperDevicePyHandle,boost::python::api::object)
        """

    def name_has_listener(self, listener: Callable) -> bool:
        """
        name_has_listener( (Device)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "name".

            C++ signature :
                bool name_has_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def overdub(self) -> None:
        """
        overdub( (LooperDevice)arg1) -> None :
            Play back while adding additional layers of incoming audio.

            C++ signature :
                void overdub(TLooperDevicePyHandle)
        """

    def overdub_after_record_has_listener(self, listener: Callable) -> bool:
        """
        overdub_after_record_has_listener( (LooperDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "overdub_after_record".

            C++ signature :
                bool overdub_after_record_has_listener(TLooperDevicePyHandle,boost::python::api::object)
        """

    def parameters_has_listener(self, listener: Callable) -> bool:
        """
        parameters_has_listener( (Device)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "parameters".

            C++ signature :
                bool parameters_has_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def play(self) -> None:
        """
        play( (LooperDevice)arg1) -> None :
            Play back without overdubbing.

            C++ signature :
                void play(TLooperDevicePyHandle)
        """

    def record(self) -> None:
        """
        record( (LooperDevice)arg1) -> None :
            Record incoming audio.

            C++ signature :
                void record(TLooperDevicePyHandle)
        """

    def record_length_index_has_listener(self, listener: Callable) -> bool:
        """
        record_length_index_has_listener( (LooperDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "record_length_index".

            C++ signature :
                bool record_length_index_has_listener(TLooperDevicePyHandle,boost::python::api::object)
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

    def remove_loop_length_listener(self, listener: Callable) -> None:
        """
        remove_loop_length_listener( (LooperDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "loop_length".

            C++ signature :
                void remove_loop_length_listener(TLooperDevicePyHandle,boost::python::api::object)
        """

    def remove_name_listener(self, listener: Callable) -> None:
        """
        remove_name_listener( (Device)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "name".

            C++ signature :
                void remove_name_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def remove_overdub_after_record_listener(self, listener: Callable) -> None:
        """
        remove_overdub_after_record_listener( (LooperDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "overdub_after_record".

            C++ signature :
                void remove_overdub_after_record_listener(TLooperDevicePyHandle,boost::python::api::object)
        """

    def remove_parameters_listener(self, listener: Callable) -> None:
        """
        remove_parameters_listener( (Device)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "parameters".

            C++ signature :
                void remove_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def remove_record_length_index_listener(self, listener: Callable) -> None:
        """
        remove_record_length_index_listener( (LooperDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "record_length_index".

            C++ signature :
                void remove_record_length_index_listener(TLooperDevicePyHandle,boost::python::api::object)
        """

    def remove_tempo_listener(self, listener: Callable) -> None:
        """
        remove_tempo_listener( (LooperDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "tempo".

            C++ signature :
                void remove_tempo_listener(TLooperDevicePyHandle,boost::python::api::object)
        """

    def save_preset_to_compare_ab_slot(self) -> None:
        """
        save_preset_to_compare_ab_slot( (Device)arg1) -> None :
            Saves the current state of the device to the compare AB slot. Only relevant if can_compare_ab, otherwise throws.

            C++ signature :
                void save_preset_to_compare_ab_slot(TPyHandle<ADevice>)
        """

    def stop(self) -> None:
        """
        stop( (LooperDevice)arg1) -> None :
            Stop Looper's playback.

            C++ signature :
                void stop(TLooperDevicePyHandle)
        """

    def store_chosen_bank(self, arg2: int, arg3: int) -> None:
        """
        store_chosen_bank( (Device)arg1, (int)arg2, (int)arg3) -> None :
            Set the selected bank in the device for persistency.

            C++ signature :
                void store_chosen_bank(TPyHandle<ADevice>,int,int)
        """

    def tempo_has_listener(self, listener: Callable) -> bool:
        """
        tempo_has_listener( (LooperDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "tempo".

            C++ signature :
                bool tempo_has_listener(TLooperDevicePyHandle,boost::python::api::object)
        """

    def undo(self) -> None:
        """
        undo( (LooperDevice)arg1) -> None :
            Erase everything that was recorded since the last time Overdub was enabled. Calling a second time will restore the material erased by the previous undooperation.

            C++ signature :
                void undo(TLooperDevicePyHandle)
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
    def loop_length(self) -> Any:
        """
        The length of Looper's buffer.
        """

    @property
    def name(self) -> str:
        """
        Return access to the name of the device.
        """

    @property
    def overdub_after_record(self) -> Any:
        """
        If true, Looper will switch to overdub after recording, when recording a fixed number of bars. Otherwise, the switch will be to playback without overdubbing.
        """

    @property
    def parameters(self) -> list[DeviceParameter]:
        """
        Const access to the list of available automatable parameters for this device.
        """

    @property
    def record_length_index(self) -> Any:
        """
        Access to the Record Length chooser entry index.
        """

    @property
    def record_length_list(self) -> Any:
        """
        Read-only access to the list of Record Length chooser entry strings.
        """

    @property
    def tempo(self) -> float:
        """
        The tempo of Looper's buffer.
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

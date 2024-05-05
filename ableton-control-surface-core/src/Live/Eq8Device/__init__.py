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


class EditMode:
    """
    Class that represent an enumeration of values for EditMode
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

    a = 0
    b = 1


class Eq8Device:
    """
    This class represents an Eq8 device.
    """

    class View:
        """
        Representing the view aspects of an Eq8 device.
        """

        def add_is_collapsed_listener(self, listener: Callable) -> None:
            """
            add_is_collapsed_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "is_collapsed" has changed.

                C++ signature :
                    void add_is_collapsed_listener(TPyViewData<ADevice>,boost::python::api::object)
            """

        def add_selected_band_listener(self, listener: Callable) -> None:
            """
            add_selected_band_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "selected_band" has changed.

                C++ signature :
                    void add_selected_band_listener(TEq8DevicePyViewData,boost::python::api::object)
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

        def remove_selected_band_listener(self, listener: Callable) -> None:
            """
            remove_selected_band_listener( (View)arg1, (object)arg2) -> None :
                Remove a previously set listener function or method from
                property "selected_band".

                C++ signature :
                    void remove_selected_band_listener(TEq8DevicePyViewData,boost::python::api::object)
            """

        def selected_band_has_listener(self, listener: Callable) -> bool:
            """
            selected_band_has_listener( (View)arg1, (object)arg2) -> bool :
                Returns true, if the given listener function or method is connected
                to the property "selected_band".

                C++ signature :
                    bool selected_band_has_listener(TEq8DevicePyViewData,boost::python::api::object)
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
        def selected_band(self) -> Any:
            """
            Access to the selected filter band.
            """

    def add_edit_mode_listener(self, listener: Callable) -> None:
        """
        add_edit_mode_listener( (Eq8Device)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "edit_mode" has changed.

            C++ signature :
                void add_edit_mode_listener(TEq8DevicePyHandle,boost::python::api::object)
        """

    def add_global_mode_listener(self, listener: Callable) -> None:
        """
        add_global_mode_listener( (Eq8Device)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "global_mode" has changed.

            C++ signature :
                void add_global_mode_listener(TEq8DevicePyHandle,boost::python::api::object)
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

    def add_oversample_listener(self, listener: Callable) -> None:
        """
        add_oversample_listener( (Eq8Device)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "oversample" has changed.

            C++ signature :
                void add_oversample_listener(TEq8DevicePyHandle,boost::python::api::object)
        """

    def add_parameters_listener(self, listener: Callable) -> None:
        """
        add_parameters_listener( (Device)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "parameters" has changed.

            C++ signature :
                void add_parameters_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def edit_mode_has_listener(self, listener: Callable) -> bool:
        """
        edit_mode_has_listener( (Eq8Device)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "edit_mode".

            C++ signature :
                bool edit_mode_has_listener(TEq8DevicePyHandle,boost::python::api::object)
        """

    def global_mode_has_listener(self, listener: Callable) -> bool:
        """
        global_mode_has_listener( (Eq8Device)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "global_mode".

            C++ signature :
                bool global_mode_has_listener(TEq8DevicePyHandle,boost::python::api::object)
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

    def oversample_has_listener(self, listener: Callable) -> bool:
        """
        oversample_has_listener( (Eq8Device)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "oversample".

            C++ signature :
                bool oversample_has_listener(TEq8DevicePyHandle,boost::python::api::object)
        """

    def parameters_has_listener(self, listener: Callable) -> bool:
        """
        parameters_has_listener( (Device)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "parameters".

            C++ signature :
                bool parameters_has_listener(TPyHandle<ADevice>,boost::python::api::object)
        """

    def remove_edit_mode_listener(self, listener: Callable) -> None:
        """
        remove_edit_mode_listener( (Eq8Device)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "edit_mode".

            C++ signature :
                void remove_edit_mode_listener(TEq8DevicePyHandle,boost::python::api::object)
        """

    def remove_global_mode_listener(self, listener: Callable) -> None:
        """
        remove_global_mode_listener( (Eq8Device)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "global_mode".

            C++ signature :
                void remove_global_mode_listener(TEq8DevicePyHandle,boost::python::api::object)
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

    def remove_oversample_listener(self, listener: Callable) -> None:
        """
        remove_oversample_listener( (Eq8Device)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "oversample".

            C++ signature :
                void remove_oversample_listener(TEq8DevicePyHandle,boost::python::api::object)
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
    def edit_mode(self) -> Any:
        """
        Access to Eq8's edit mode.
        """

    @property
    def global_mode(self) -> Any:
        """
        Access to Eq8's global mode.
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
    def oversample(self) -> Any:
        """
        Access to Eq8's oversample value.
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


class GlobalMode:
    """
    Class that represent an enumeration of values for GlobalMode
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

    stereo = 0
    left_right = 1
    mid_side = 2

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


class DeviceIO:
    """
    This class represents a specific input or output bus of a device.
    """

    def add_available_routing_channels_listener(self, listener: Callable) -> None:
        """
        add_available_routing_channels_listener( (DeviceIO)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "available_routing_channels" has changed.

            C++ signature :
                void add_available_routing_channels_listener(TPyHandle<AMxDRoutable>,boost::python::api::object)
        """

    def add_available_routing_types_listener(self, listener: Callable) -> None:
        """
        add_available_routing_types_listener( (DeviceIO)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "available_routing_types" has changed.

            C++ signature :
                void add_available_routing_types_listener(TPyHandle<AMxDRoutable>,boost::python::api::object)
        """

    def add_routing_channel_listener(self, listener: Callable) -> None:
        """
        add_routing_channel_listener( (DeviceIO)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "routing_channel" has changed.

            C++ signature :
                void add_routing_channel_listener(TPyHandle<AMxDRoutable>,boost::python::api::object)
        """

    def add_routing_type_listener(self, listener: Callable) -> None:
        """
        add_routing_type_listener( (DeviceIO)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "routing_type" has changed.

            C++ signature :
                void add_routing_type_listener(TPyHandle<AMxDRoutable>,boost::python::api::object)
        """

    def available_routing_channels_has_listener(self, listener: Callable) -> bool:
        """
        available_routing_channels_has_listener( (DeviceIO)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "available_routing_channels".

            C++ signature :
                bool available_routing_channels_has_listener(TPyHandle<AMxDRoutable>,boost::python::api::object)
        """

    def available_routing_types_has_listener(self, listener: Callable) -> bool:
        """
        available_routing_types_has_listener( (DeviceIO)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "available_routing_types".

            C++ signature :
                bool available_routing_types_has_listener(TPyHandle<AMxDRoutable>,boost::python::api::object)
        """

    def remove_available_routing_channels_listener(self, listener: Callable) -> None:
        """
        remove_available_routing_channels_listener( (DeviceIO)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "available_routing_channels".

            C++ signature :
                void remove_available_routing_channels_listener(TPyHandle<AMxDRoutable>,boost::python::api::object)
        """

    def remove_available_routing_types_listener(self, listener: Callable) -> None:
        """
        remove_available_routing_types_listener( (DeviceIO)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "available_routing_types".

            C++ signature :
                void remove_available_routing_types_listener(TPyHandle<AMxDRoutable>,boost::python::api::object)
        """

    def remove_routing_channel_listener(self, listener: Callable) -> None:
        """
        remove_routing_channel_listener( (DeviceIO)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "routing_channel".

            C++ signature :
                void remove_routing_channel_listener(TPyHandle<AMxDRoutable>,boost::python::api::object)
        """

    def remove_routing_type_listener(self, listener: Callable) -> None:
        """
        remove_routing_type_listener( (DeviceIO)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "routing_type".

            C++ signature :
                void remove_routing_type_listener(TPyHandle<AMxDRoutable>,boost::python::api::object)
        """

    def routing_channel_has_listener(self, listener: Callable) -> bool:
        """
        routing_channel_has_listener( (DeviceIO)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "routing_channel".

            C++ signature :
                bool routing_channel_has_listener(TPyHandle<AMxDRoutable>,boost::python::api::object)
        """

    def routing_type_has_listener(self, listener: Callable) -> bool:
        """
        routing_type_has_listener( (DeviceIO)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "routing_type".

            C++ signature :
                bool routing_type_has_listener(TPyHandle<AMxDRoutable>,boost::python::api::object)
        """

    @property
    def available_routing_channels(self) -> Any:
        """
        Return a list of channels for this IO endpoint.
        """

    @property
    def available_routing_types(self) -> Any:
        """
        Return a list of available routing types for this IO endpoint.
        """

    @property
    def canonical_parent(self) -> Any:
        """
        Get the canonical parent of the device IO.
        """

    @property
    def default_external_routing_channel_is_none(self) -> Any:
        """
        Get and set whether the default routing channel for External routing types is none.
        """

    @property
    def routing_channel(self) -> Any:
        """
        Get and set the current routing channel.
        Raises ValueError if the channel isn't one of the current values in
        available_routing_channels.
        """

    @property
    def routing_type(self) -> Any:
        """
        Get and set the current routing type.
        Raises ValueError if the type isn't one of the current values in
        available_routing_types.
        """

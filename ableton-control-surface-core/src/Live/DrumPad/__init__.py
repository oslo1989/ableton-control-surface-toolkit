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


class DrumPad:
    """
    This class represents a drum group device pad in Live.
    """

    def add_chains_listener(self, listener: Callable) -> None:
        """
        add_chains_listener( (DrumPad)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "chains" has changed.

            C++ signature :
                void add_chains_listener(TPyHandle<ADrumGroupDevicePad>,boost::python::api::object)
        """

    def add_mute_listener(self, listener: Callable) -> None:
        """
        add_mute_listener( (DrumPad)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "mute" has changed.

            C++ signature :
                void add_mute_listener(TPyHandle<ADrumGroupDevicePad>,boost::python::api::object)
        """

    def add_name_listener(self, listener: Callable) -> None:
        """
        add_name_listener( (DrumPad)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "name" has changed.

            C++ signature :
                void add_name_listener(TPyHandle<ADrumGroupDevicePad>,boost::python::api::object)
        """

    def add_solo_listener(self, listener: Callable) -> None:
        """
        add_solo_listener( (DrumPad)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "solo" has changed.

            C++ signature :
                void add_solo_listener(TPyHandle<ADrumGroupDevicePad>,boost::python::api::object)
        """

    def chains_has_listener(self, listener: Callable) -> bool:
        """
        chains_has_listener( (DrumPad)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "chains".

            C++ signature :
                bool chains_has_listener(TPyHandle<ADrumGroupDevicePad>,boost::python::api::object)
        """

    def delete_all_chains(self) -> None:
        """
        delete_all_chains( (DrumPad)arg1) -> None :
            Deletes all chains associated with a drum pad. This is equivalent to deleting a drum rack pad in Live.

            C++ signature :
                void delete_all_chains(TPyHandle<ADrumGroupDevicePad>)
        """

    def mute_has_listener(self, listener: Callable) -> bool:
        """
        mute_has_listener( (DrumPad)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "mute".

            C++ signature :
                bool mute_has_listener(TPyHandle<ADrumGroupDevicePad>,boost::python::api::object)
        """

    def name_has_listener(self, listener: Callable) -> bool:
        """
        name_has_listener( (DrumPad)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "name".

            C++ signature :
                bool name_has_listener(TPyHandle<ADrumGroupDevicePad>,boost::python::api::object)
        """

    def remove_chains_listener(self, listener: Callable) -> None:
        """
        remove_chains_listener( (DrumPad)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "chains".

            C++ signature :
                void remove_chains_listener(TPyHandle<ADrumGroupDevicePad>,boost::python::api::object)
        """

    def remove_mute_listener(self, listener: Callable) -> None:
        """
        remove_mute_listener( (DrumPad)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "mute".

            C++ signature :
                void remove_mute_listener(TPyHandle<ADrumGroupDevicePad>,boost::python::api::object)
        """

    def remove_name_listener(self, listener: Callable) -> None:
        """
        remove_name_listener( (DrumPad)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "name".

            C++ signature :
                void remove_name_listener(TPyHandle<ADrumGroupDevicePad>,boost::python::api::object)
        """

    def remove_solo_listener(self, listener: Callable) -> None:
        """
        remove_solo_listener( (DrumPad)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "solo".

            C++ signature :
                void remove_solo_listener(TPyHandle<ADrumGroupDevicePad>,boost::python::api::object)
        """

    def solo_has_listener(self, listener: Callable) -> bool:
        """
        solo_has_listener( (DrumPad)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "solo".

            C++ signature :
                bool solo_has_listener(TPyHandle<ADrumGroupDevicePad>,boost::python::api::object)
        """

    @property
    def canonical_parent(self) -> Any:
        """
        Get the canonical parent of the drum pad.
        """

    @property
    def chains(self) -> Any:
        """
        Return const access to the list of chains in this drum pad.
        """

    @property
    def mute(self) -> Any:
        """
        Mute/unmute the pad.
        """

    @property
    def name(self) -> str:
        """
        Return const access to the drum pad's name. It depends on the contained chains.
        """

    @property
    def note(self) -> Any:
        """
        Get the MIDI note of the drum pad.
        """

    @property
    def solo(self) -> Any:
        """
        Solo/unsolo the pad.
        """

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


class DrumChain:
    """
    This class represents a drum group device chain in Live.
    """

    def add_choke_group_listener(self, listener: Callable) -> None:
        """
        add_choke_group_listener( (DrumChain)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "choke_group" has changed.

            C++ signature :
                void add_choke_group_listener(TDrumChainPyHandle,boost::python::api::object)
        """

    def add_color_index_listener(self, listener: Callable) -> None:
        """
        add_color_index_listener( (Chain)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "color_index" has changed.

            C++ signature :
                void add_color_index_listener(TChainPyHandle,boost::python::api::object)
        """

    def add_color_listener(self, listener: Callable) -> None:
        """
        add_color_listener( (Chain)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "color" has changed.

            C++ signature :
                void add_color_listener(TChainPyHandle,boost::python::api::object)
        """

    def add_devices_listener(self, listener: Callable) -> None:
        """
        add_devices_listener( (Chain)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "devices" has changed.

            C++ signature :
                void add_devices_listener(TChainPyHandle,boost::python::api::object)
        """

    def add_is_auto_colored_listener(self, listener: Callable) -> None:
        """
        add_is_auto_colored_listener( (Chain)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "is_auto_colored" has changed.

            C++ signature :
                void add_is_auto_colored_listener(TChainPyHandle,boost::python::api::object)
        """

    def add_mute_listener(self, listener: Callable) -> None:
        """
        add_mute_listener( (Chain)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "mute" has changed.

            C++ signature :
                void add_mute_listener(TChainPyHandle,boost::python::api::object)
        """

    def add_muted_via_solo_listener(self, listener: Callable) -> None:
        """
        add_muted_via_solo_listener( (Chain)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "muted_via_solo" has changed.

            C++ signature :
                void add_muted_via_solo_listener(TChainPyHandle,boost::python::api::object)
        """

    def add_name_listener(self, listener: Callable) -> None:
        """
        add_name_listener( (Chain)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "name" has changed.

            C++ signature :
                void add_name_listener(TChainPyHandle,boost::python::api::object)
        """

    def add_out_note_listener(self, listener: Callable) -> None:
        """
        add_out_note_listener( (DrumChain)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "out_note" has changed.

            C++ signature :
                void add_out_note_listener(TDrumChainPyHandle,boost::python::api::object)
        """

    def add_solo_listener(self, listener: Callable) -> None:
        """
        add_solo_listener( (Chain)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "solo" has changed.

            C++ signature :
                void add_solo_listener(TChainPyHandle,boost::python::api::object)
        """

    def choke_group_has_listener(self, listener: Callable) -> bool:
        """
        choke_group_has_listener( (DrumChain)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "choke_group".

            C++ signature :
                bool choke_group_has_listener(TDrumChainPyHandle,boost::python::api::object)
        """

    def color_has_listener(self, listener: Callable) -> bool:
        """
        color_has_listener( (Chain)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "color".

            C++ signature :
                bool color_has_listener(TChainPyHandle,boost::python::api::object)
        """

    def color_index_has_listener(self, listener: Callable) -> bool:
        """
        color_index_has_listener( (Chain)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "color_index".

            C++ signature :
                bool color_index_has_listener(TChainPyHandle,boost::python::api::object)
        """

    def delete_device(self, arg2: int) -> None:
        """
        delete_device( (Chain)arg1, (int)arg2) -> None :
            Remove a device identified by its index from the chain. Throws runtime error if bad index.


            C++ signature :
                void delete_device(TChainPyHandle,int)
        """

    def devices_has_listener(self, listener: Callable) -> bool:
        """
        devices_has_listener( (Chain)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "devices".

            C++ signature :
                bool devices_has_listener(TChainPyHandle,boost::python::api::object)
        """

    def is_auto_colored_has_listener(self, listener: Callable) -> bool:
        """
        is_auto_colored_has_listener( (Chain)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "is_auto_colored".

            C++ signature :
                bool is_auto_colored_has_listener(TChainPyHandle,boost::python::api::object)
        """

    def mute_has_listener(self, listener: Callable) -> bool:
        """
        mute_has_listener( (Chain)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "mute".

            C++ signature :
                bool mute_has_listener(TChainPyHandle,boost::python::api::object)
        """

    def muted_via_solo_has_listener(self, listener: Callable) -> bool:
        """
        muted_via_solo_has_listener( (Chain)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "muted_via_solo".

            C++ signature :
                bool muted_via_solo_has_listener(TChainPyHandle,boost::python::api::object)
        """

    def name_has_listener(self, listener: Callable) -> bool:
        """
        name_has_listener( (Chain)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "name".

            C++ signature :
                bool name_has_listener(TChainPyHandle,boost::python::api::object)
        """

    def out_note_has_listener(self, listener: Callable) -> bool:
        """
        out_note_has_listener( (DrumChain)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "out_note".

            C++ signature :
                bool out_note_has_listener(TDrumChainPyHandle,boost::python::api::object)
        """

    def remove_choke_group_listener(self, listener: Callable) -> None:
        """
        remove_choke_group_listener( (DrumChain)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "choke_group".

            C++ signature :
                void remove_choke_group_listener(TDrumChainPyHandle,boost::python::api::object)
        """

    def remove_color_index_listener(self, listener: Callable) -> None:
        """
        remove_color_index_listener( (Chain)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "color_index".

            C++ signature :
                void remove_color_index_listener(TChainPyHandle,boost::python::api::object)
        """

    def remove_color_listener(self, listener: Callable) -> None:
        """
        remove_color_listener( (Chain)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "color".

            C++ signature :
                void remove_color_listener(TChainPyHandle,boost::python::api::object)
        """

    def remove_devices_listener(self, listener: Callable) -> None:
        """
        remove_devices_listener( (Chain)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "devices".

            C++ signature :
                void remove_devices_listener(TChainPyHandle,boost::python::api::object)
        """

    def remove_is_auto_colored_listener(self, listener: Callable) -> None:
        """
        remove_is_auto_colored_listener( (Chain)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "is_auto_colored".

            C++ signature :
                void remove_is_auto_colored_listener(TChainPyHandle,boost::python::api::object)
        """

    def remove_mute_listener(self, listener: Callable) -> None:
        """
        remove_mute_listener( (Chain)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "mute".

            C++ signature :
                void remove_mute_listener(TChainPyHandle,boost::python::api::object)
        """

    def remove_muted_via_solo_listener(self, listener: Callable) -> None:
        """
        remove_muted_via_solo_listener( (Chain)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "muted_via_solo".

            C++ signature :
                void remove_muted_via_solo_listener(TChainPyHandle,boost::python::api::object)
        """

    def remove_name_listener(self, listener: Callable) -> None:
        """
        remove_name_listener( (Chain)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "name".

            C++ signature :
                void remove_name_listener(TChainPyHandle,boost::python::api::object)
        """

    def remove_out_note_listener(self, listener: Callable) -> None:
        """
        remove_out_note_listener( (DrumChain)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "out_note".

            C++ signature :
                void remove_out_note_listener(TDrumChainPyHandle,boost::python::api::object)
        """

    def remove_solo_listener(self, listener: Callable) -> None:
        """
        remove_solo_listener( (Chain)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "solo".

            C++ signature :
                void remove_solo_listener(TChainPyHandle,boost::python::api::object)
        """

    def solo_has_listener(self, listener: Callable) -> bool:
        """
        solo_has_listener( (Chain)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "solo".

            C++ signature :
                bool solo_has_listener(TChainPyHandle,boost::python::api::object)
        """

    @property
    def canonical_parent(self) -> Any:
        """
        Get the canonical parent of the chain.
        """

    @property
    def choke_group(self) -> Any:
        """
        Access to the chain's choke group setting.
        """

    @property
    def color(self) -> Any:
        """
        Access the color index of the Chain.
        """

    @property
    def color_index(self) -> Any:
        """
        Access the color index of the Chain.
        """

    @property
    def devices(self) -> list[Device]:
        """
        Return const access to all available Devices that are present in the chains
        """

    @property
    def has_audio_input(self) -> bool:
        """
        return True, if this Chain can be feed with an Audio signal. This is
        true for all Audio Chains.
        """

    @property
    def has_audio_output(self) -> bool:
        """
        return True, if this Chain sends out an Audio signal. This is
        true for all Audio Chains, and MIDI chains with an Instrument.
        """

    @property
    def has_midi_input(self) -> bool:
        """
        return True, if this Chain can be feed with an Audio signal. This is
        true for all MIDI Chains.
        """

    @property
    def has_midi_output(self) -> bool:
        """
        return True, if this Chain sends out MIDI events. This is
        true for all MIDI Chains with no Instruments.
        """

    @property
    def is_auto_colored(self) -> bool:
        """
        Get/set access to the auto color flag of the Chain.
        If True, the Chain will always have the same color as the containing
        Track or Chain.
        """

    @is_auto_colored.setter
    def is_auto_colored(self, value: bool) -> None:
        pass

    @property
    def mixer_device(self) -> Device:
        """
        Return access to the mixer device that holds the chain's mixer parameters:
        the Volume, Pan, and Sendamounts.
        """

    @property
    def mute(self) -> Any:
        """
        Mute/unmute the chain.
        """

    @property
    def muted_via_solo(self) -> Any:
        """
        Return const access to whether this chain is muted due to some other chain
        being soloed.
        """

    @property
    def name(self) -> str:
        """
        Read/write access to the name of the Chain, as visible in the track header.
        """

    @name.setter
    def name(self, value: str) -> None:
        pass

    @property
    def out_note(self) -> Any:
        """
        Access to the MIDI note sent to the devices in the chain.
        """

    @property
    def solo(self) -> Any:
        """
        Get/Set the solo status of the chain. Note that this will not disable the
        solo state of any other Chain in the same rack. If you want exclusive solo,
        you have to disable the solo state of the other Chains manually.
        """

    @solo.setter
    def solo(self, value: Any) -> None:
        pass

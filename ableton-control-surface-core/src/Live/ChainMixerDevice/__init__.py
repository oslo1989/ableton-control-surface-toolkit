from __future__ import annotations

from typing import Any, Callable

from Live import *
from Live.Application import *
from Live.Base import *
from Live.Browser import *
from Live.CcControlDevice import *
from Live.Chain import *
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


class ChainMixerDevice:
    """
    This class represents a Chain's Mixer Device in Live, which gives you
    access to the Volume, Panning, and Send properties of a Chain.
    """

    def add_sends_listener(self, listener: Callable) -> None:
        """
        add_sends_listener( (ChainMixerDevice)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "sends" has changed.

            C++ signature :
                void add_sends_listener(TPyHandle<ABranchMixerDevice>,boost::python::api::object)
        """

    def remove_sends_listener(self, listener: Callable) -> None:
        """
        remove_sends_listener( (ChainMixerDevice)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "sends".

            C++ signature :
                void remove_sends_listener(TPyHandle<ABranchMixerDevice>,boost::python::api::object)
        """

    def sends_has_listener(self, listener: Callable) -> bool:
        """
        sends_has_listener( (ChainMixerDevice)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "sends".

            C++ signature :
                bool sends_has_listener(TPyHandle<ABranchMixerDevice>,boost::python::api::object)
        """

    @property
    def canonical_parent(self) -> Any:
        """
        Get the canonical parent of the mixer device.
        """

    @property
    def chain_activator(self) -> Any:
        """
        Const access to the Chain's Activator Device Parameter.
        """

    @property
    def panning(self) -> Any:
        """
        Const access to the Chain's Panning Device Parameter.
        """

    @property
    def sends(self) -> Any:
        """
        Const access to the Chain's list of Send Amount Device Parameters.
        """

    @property
    def volume(self) -> Any:
        """
        Const access to the Chain's Volume Device Parameter.
        """

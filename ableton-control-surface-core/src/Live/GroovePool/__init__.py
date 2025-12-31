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


class GroovePool:
    """
    This class represents the groove pool in Live.
    """

    def add_grooves_listener(self, listener: Callable) -> None:
        """
        add_grooves_listener( (GroovePool)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "grooves" has changed.

            C++ signature :
                void add_grooves_listener(TPyHandle<AGroovePool>,boost::python::api::object)
        """

    def grooves_has_listener(self, listener: Callable) -> bool:
        """
        grooves_has_listener( (GroovePool)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "grooves".

            C++ signature :
                bool grooves_has_listener(TPyHandle<AGroovePool>,boost::python::api::object)
        """

    def remove_grooves_listener(self, listener: Callable) -> None:
        """
        remove_grooves_listener( (GroovePool)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "grooves".

            C++ signature :
                void remove_grooves_listener(TPyHandle<AGroovePool>,boost::python::api::object)
        """

    @property
    def canonical_parent(self) -> Any:
        """
        Get the canonical parent of the groove pool.
        """

    @property
    def grooves(self) -> Any:
        """
        Access to the list of grooves
        """

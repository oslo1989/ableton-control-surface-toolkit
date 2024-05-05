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
from Live.HybridReverbDevice import *
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


class ListenerHandle:
    """
    This class represents a Python listener when connected to a Live property.
    """

    def disconnect(self) -> None:
        """
        disconnect( (ListenerHandle)arg1) -> None :
            Disconnects the listener from its property

            C++ signature :
                void disconnect(LPythonRemote {lvalue})
        """

    @property
    def listener_func(self) -> Any:
        """
        Returns the original function
        """

    @property
    def listener_self(self) -> Any:
        """
        Returns the weak reference to original self, if it was a bound method
        """

    @property
    def name(self) -> str:
        """
        Prints the name of the property that this listener is connected to
        """


class ListenerVector:
    """
    A read only container for accessing a list of listeners.
    """

    def append(self, arg2: object) -> None:
        """
        append( (ListenerVector)arg1, (object)arg2) -> None :

            C++ signature :
                void append(std::__1::vector<TWeakPtr<LPythonRemote>, std::__1::allocator<TWeakPtr<LPythonRemote>>> {lvalue},boost::python::api::object)
        """

    def extend(self, arg2: object) -> None:
        """
        extend( (ListenerVector)arg1, (object)arg2) -> None :

            C++ signature :
                void extend(std::__1::vector<TWeakPtr<LPythonRemote>, std::__1::allocator<TWeakPtr<LPythonRemote>>> {lvalue},boost::python::api::object)
        """

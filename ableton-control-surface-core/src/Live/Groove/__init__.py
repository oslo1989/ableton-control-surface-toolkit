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


class Base:
    """
    Class that represent an enumeration of values for Base
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

    gb_four = 0
    gb_eight = 1
    gb_eight_triplet = 2
    gb_sixteen = 3
    gb_sixteen_triplet = 4
    gb_thirtytwo = 5
    count = 6


class Groove:
    """
    This class represents a groove in Live.
    """

    def add_name_listener(self, listener: Callable) -> None:
        """
        add_name_listener( (Groove)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "name" has changed.

            C++ signature :
                void add_name_listener(TPyHandle<AGroove>,boost::python::api::object)
        """

    def add_quantization_amount_listener(self, listener: Callable) -> None:
        """
        add_quantization_amount_listener( (Groove)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "quantization_amount" has changed.

            C++ signature :
                void add_quantization_amount_listener(TPyHandle<AGroove>,boost::python::api::object)
        """

    def add_random_amount_listener(self, listener: Callable) -> None:
        """
        add_random_amount_listener( (Groove)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "random_amount" has changed.

            C++ signature :
                void add_random_amount_listener(TPyHandle<AGroove>,boost::python::api::object)
        """

    def add_timing_amount_listener(self, listener: Callable) -> None:
        """
        add_timing_amount_listener( (Groove)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "timing_amount" has changed.

            C++ signature :
                void add_timing_amount_listener(TPyHandle<AGroove>,boost::python::api::object)
        """

    def add_velocity_amount_listener(self, listener: Callable) -> None:
        """
        add_velocity_amount_listener( (Groove)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "velocity_amount" has changed.

            C++ signature :
                void add_velocity_amount_listener(TPyHandle<AGroove>,boost::python::api::object)
        """

    def name_has_listener(self, listener: Callable) -> bool:
        """
        name_has_listener( (Groove)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "name".

            C++ signature :
                bool name_has_listener(TPyHandle<AGroove>,boost::python::api::object)
        """

    def quantization_amount_has_listener(self, listener: Callable) -> bool:
        """
        quantization_amount_has_listener( (Groove)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "quantization_amount".

            C++ signature :
                bool quantization_amount_has_listener(TPyHandle<AGroove>,boost::python::api::object)
        """

    def random_amount_has_listener(self, listener: Callable) -> bool:
        """
        random_amount_has_listener( (Groove)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "random_amount".

            C++ signature :
                bool random_amount_has_listener(TPyHandle<AGroove>,boost::python::api::object)
        """

    def remove_name_listener(self, listener: Callable) -> None:
        """
        remove_name_listener( (Groove)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "name".

            C++ signature :
                void remove_name_listener(TPyHandle<AGroove>,boost::python::api::object)
        """

    def remove_quantization_amount_listener(self, listener: Callable) -> None:
        """
        remove_quantization_amount_listener( (Groove)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "quantization_amount".

            C++ signature :
                void remove_quantization_amount_listener(TPyHandle<AGroove>,boost::python::api::object)
        """

    def remove_random_amount_listener(self, listener: Callable) -> None:
        """
        remove_random_amount_listener( (Groove)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "random_amount".

            C++ signature :
                void remove_random_amount_listener(TPyHandle<AGroove>,boost::python::api::object)
        """

    def remove_timing_amount_listener(self, listener: Callable) -> None:
        """
        remove_timing_amount_listener( (Groove)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "timing_amount".

            C++ signature :
                void remove_timing_amount_listener(TPyHandle<AGroove>,boost::python::api::object)
        """

    def remove_velocity_amount_listener(self, listener: Callable) -> None:
        """
        remove_velocity_amount_listener( (Groove)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "velocity_amount".

            C++ signature :
                void remove_velocity_amount_listener(TPyHandle<AGroove>,boost::python::api::object)
        """

    def timing_amount_has_listener(self, listener: Callable) -> bool:
        """
        timing_amount_has_listener( (Groove)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "timing_amount".

            C++ signature :
                bool timing_amount_has_listener(TPyHandle<AGroove>,boost::python::api::object)
        """

    def velocity_amount_has_listener(self, listener: Callable) -> bool:
        """
        velocity_amount_has_listener( (Groove)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "velocity_amount".

            C++ signature :
                bool velocity_amount_has_listener(TPyHandle<AGroove>,boost::python::api::object)
        """

    @property
    def base(self) -> Any:
        """
        Get/set the groove's base grid.
        """

    @base.setter
    def base(self, value: Any) -> None:
        pass

    @property
    def canonical_parent(self) -> Any:
        """
        Get the canonical parent of the groove.
        """

    @property
    def name(self) -> str:
        """
        Read/write/listen access to the groove's name
        """

    @name.setter
    def name(self, value: str) -> None:
        pass

    @property
    def quantization_amount(self) -> Any:
        """
        Read/write/listen access to the groove's quantization amount.
        """

    @quantization_amount.setter
    def quantization_amount(self, value: Any) -> None:
        pass

    @property
    def random_amount(self) -> Any:
        """
        Read/write/listen access to the groove's random amount.
        """

    @random_amount.setter
    def random_amount(self, value: Any) -> None:
        pass

    @property
    def timing_amount(self) -> Any:
        """
        Read/write/listen access to the groove's timing amount.
        """

    @timing_amount.setter
    def timing_amount(self, value: Any) -> None:
        pass

    @property
    def velocity_amount(self) -> Any:
        """
        Read/write/listen access to the groove's velocity amount.
        """

    @velocity_amount.setter
    def velocity_amount(self, value: Any) -> None:
        pass

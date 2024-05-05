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


class AutomationState:
    """
    Class that represent an enumeration of values for AutomationState
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

    none = 0
    playing = 1
    overridden = 2


class DeviceParameter:
    """
    This class represents a (automatable) parameter within a MIDI or
    Audio DSP-Device.
    """

    def add_automation_state_listener(self, listener: Callable) -> None:
        """
        add_automation_state_listener( (DeviceParameter)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "automation_state" has changed.

            C++ signature :
                void add_automation_state_listener(TPyHandle<ATimeableValue>,boost::python::api::object)
        """

    def add_name_listener(self, listener: Callable) -> None:
        """
        add_name_listener( (DeviceParameter)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "name" has changed.

            C++ signature :
                void add_name_listener(TPyHandle<ATimeableValue>,boost::python::api::object)
        """

    def add_state_listener(self, listener: Callable) -> None:
        """
        add_state_listener( (DeviceParameter)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "state" has changed.

            C++ signature :
                void add_state_listener(TPyHandle<ATimeableValue>,boost::python::api::object)
        """

    def add_value_listener(self, listener: Callable) -> None:
        """
        add_value_listener( (DeviceParameter)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "value" has changed.

            C++ signature :
                void add_value_listener(TPyHandle<ATimeableValue>,boost::python::api::object)
        """

    def automation_state_has_listener(self, listener: Callable) -> bool:
        """
        automation_state_has_listener( (DeviceParameter)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "automation_state".

            C++ signature :
                bool automation_state_has_listener(TPyHandle<ATimeableValue>,boost::python::api::object)
        """

    def begin_gesture(self) -> None:
        """
        begin_gesture( (DeviceParameter)arg1) -> None :
            Notify the begin of a modification of the parameter, when a sequence of modifications have to be consider a consistent group -- for Sexample, when recording automation.

            C++ signature :
                void begin_gesture(TPyHandle<ATimeableValue>)
        """

    def end_gesture(self) -> None:
        """
        end_gesture( (DeviceParameter)arg1) -> None :
            Notify the end of a modification of the parameter. See begin_gesture.

            C++ signature :
                void end_gesture(TPyHandle<ATimeableValue>)
        """

    def name_has_listener(self, listener: Callable) -> bool:
        """
        name_has_listener( (DeviceParameter)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "name".

            C++ signature :
                bool name_has_listener(TPyHandle<ATimeableValue>,boost::python::api::object)
        """

    def re_enable_automation(self) -> None:
        """
        re_enable_automation( (DeviceParameter)arg1) -> None :
            Reenable automation for this parameter.

            C++ signature :
                void re_enable_automation(TPyHandle<ATimeableValue>)
        """

    def remove_automation_state_listener(self, listener: Callable) -> None:
        """
        remove_automation_state_listener( (DeviceParameter)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "automation_state".

            C++ signature :
                void remove_automation_state_listener(TPyHandle<ATimeableValue>,boost::python::api::object)
        """

    def remove_name_listener(self, listener: Callable) -> None:
        """
        remove_name_listener( (DeviceParameter)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "name".

            C++ signature :
                void remove_name_listener(TPyHandle<ATimeableValue>,boost::python::api::object)
        """

    def remove_state_listener(self, listener: Callable) -> None:
        """
        remove_state_listener( (DeviceParameter)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "state".

            C++ signature :
                void remove_state_listener(TPyHandle<ATimeableValue>,boost::python::api::object)
        """

    def remove_value_listener(self, listener: Callable) -> None:
        """
        remove_value_listener( (DeviceParameter)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "value".

            C++ signature :
                void remove_value_listener(TPyHandle<ATimeableValue>,boost::python::api::object)
        """

    def state_has_listener(self, listener: Callable) -> bool:
        """
        state_has_listener( (DeviceParameter)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "state".

            C++ signature :
                bool state_has_listener(TPyHandle<ATimeableValue>,boost::python::api::object)
        """

    def str_for_value(self, arg2: float) -> str:
        """
        str_for_value( (DeviceParameter)arg1, (float)arg2) -> str :
            Return a string representation of the given value. To be used
            for display purposes only.  This value can include characters like 'db' or
            'hz', depending on the type of the parameter.

            C++ signature :
                TString str_for_value(TPyHandle<ATimeableValue>,float)
        """

    def value_has_listener(self, listener: Callable) -> bool:
        """
        value_has_listener( (DeviceParameter)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "value".

            C++ signature :
                bool value_has_listener(TPyHandle<ATimeableValue>,boost::python::api::object)
        """

    @property
    def automation_state(self) -> Any:
        """
        Returns state of type AutomationState.
        """

    @property
    def canonical_parent(self) -> Any:
        """
        Get the canonical parent of the device parameter.
        """

    @property
    def default_value(self) -> int | float:
        """
        Return the default value for this parameter.  A Default value is only
        available for non-quantized parameter types (see 'is_quantized').
        """

    @property
    def is_enabled(self) -> bool:
        """
        Returns false if the parameter has been macro mapped or disabled by Max.
        """

    @property
    def is_quantized(self) -> bool:
        """
        Returns True, if this value is a boolean or integer like switch.
        Non quantized values are continues float values.
        """

    @property
    def max(self) -> int | float:
        """
        Returns const access to the upper value of the allowed range for
        this parameter
        """

    @property
    def min(self) -> int | float:
        """
        Returns const access to the lower value of the allowed range for
        this parameter
        """

    @property
    def name(self) -> str:
        """
        Returns const access the name of this parameter, as visible in Lives
        automation choosers.
        """

    @property
    def original_name(self) -> str:
        """
        Returns const access the original name of this parameter, unaffected of
        any renamings.
        """

    @property
    def short_value_items(self) -> Any:
        """
        Return the list of possible values for this parameter. Like value_items, but prefers short value names if available. Raises an error if 'is_quantized' is False.
        """

    @property
    def state(self) -> Any:
        """
        Returns the state of the parameter:
        - enabled - the parameter's value can be changed,
        - irrelevant - the parameter is enabled, but value changes will not take any effect until it gets enabled,
        - disabled - the parameter's value cannot be changed.
        """

    @property
    def value(self) -> int | float:
        """
        Get/Set the current value (as visible in the GUI) this parameter.
        The value must be inside the min/max properties of this device.
        """

    @value.setter
    def value(self, value: int | float) -> None:
        pass

    @property
    def value_items(self) -> Any:
        """
        Return the list of possible values for this parameter. Raises an error if 'is_quantized' is False.
        """


class ParameterState:
    """
    Class that represent an enumeration of values for ParameterState
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

    enabled = 0
    irrelevant = 1
    disabled = 2

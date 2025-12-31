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
from Live.Eq8Device import *
from Live.Groove import *
from Live.GroovePool import *
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


class Envelope:
    """
    This class represents an automation or modulation envelope in Live.
    """

    def delete_events_in_range(self, arg2: float, arg3: float) -> None:
        """
        delete_events_in_range( (Envelope)arg1, (float)arg2, (float)arg3) -> None :
            Deletes the events in the specified time range.

            C++ signature :
                void delete_events_in_range(TPyHandle<AAutomation> {lvalue},double,double)
        """

    def events_in_range(self, arg2: float, arg3: float) -> EnvelopeEventVector:
        """
        events_in_range( (Envelope)arg1, (float)arg2, (float)arg3) -> EnvelopeEventVector :
            Returns the events in the specified time range.

            C++ signature :
                std::__1::vector<NApiHelpers::TEnvelopeEvent, std::__1::allocator<NApiHelpers::TEnvelopeEvent>> events_in_range(TPyHandle<AAutomation> {lvalue},double,double)
        """

    def insert_step(self, arg2: float, arg3: float, arg4: float) -> None:
        """
        insert_step( (Envelope)arg1, (float)arg2, (float)arg3, (float)arg4) -> None :
            Given a start time, a step length and a value, creates a step in the envelope.

            C++ signature :
                void insert_step(TPyHandle<AAutomation> {lvalue},double,double,double)
        """

    def value_at_time(self, arg2: float) -> float:
        """
        value_at_time( (Envelope)arg1, (float)arg2) -> float :
            Returns the parameter value at the specified time.

            C++ signature :
                double value_at_time(TPyHandle<AAutomation> {lvalue},double)
        """

    @property
    def canonical_parent(self) -> Any:
        """
        Get the canonical parent of the envelope.
        """


class EnvelopeEvent:
    """
    This is a class that represents an envelope event.
    """

    @property
    def control_coefficients(self) -> Any:
        pass

    @property
    def time(self) -> Any:
        pass

    @property
    def value(self) -> int | float:
        pass


class EnvelopeEventControlCoefficients:
    """
    This class represents the control coefficients of an envelope event.
    """

    @property
    def x1(self) -> Any:
        pass

    @property
    def x2(self) -> Any:
        pass

    @property
    def y1(self) -> Any:
        pass

    @property
    def y2(self) -> Any:
        pass


class EnvelopeEventVector:
    """
    A container for holding envelope events.
    """

    def append(self, arg2: object) -> None:
        """
        append( (EnvelopeEventVector)arg1, (object)arg2) -> None :

            C++ signature :
                void append(std::__1::vector<NApiHelpers::TEnvelopeEvent, std::__1::allocator<NApiHelpers::TEnvelopeEvent>> {lvalue},boost::python::api::object)
        """

    def extend(self, arg2: object) -> None:
        """
        extend( (EnvelopeEventVector)arg1, (object)arg2) -> None :

            C++ signature :
                void extend(std::__1::vector<NApiHelpers::TEnvelopeEvent, std::__1::allocator<NApiHelpers::TEnvelopeEvent>> {lvalue},boost::python::api::object)
        """

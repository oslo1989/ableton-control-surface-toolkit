from __future__ import annotations

from typing import Any, Callable

from Live import *
from Live.Application import *
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


class FloatVector:
    """
    A simple container for returning floats from Live.
    """

    def append(self, arg2: object) -> None:
        """
        append( (FloatVector)arg1, (object)arg2) -> None :

            C++ signature :
                void append(std::__1::vector<float, std::__1::allocator<float>> {lvalue},boost::python::api::object)
        """

    def extend(self, arg2: object) -> None:
        """
        extend( (FloatVector)arg1, (object)arg2) -> None :

            C++ signature :
                void extend(std::__1::vector<float, std::__1::allocator<float>> {lvalue},boost::python::api::object)
        """


class IntU64Vector:
    """
    A simple container for returning unsigned long integers from Live.
    """

    def append(self, arg2: object) -> None:
        """
        append( (IntU64Vector)arg1, (object)arg2) -> None :

            C++ signature :
                void append(std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long>> {lvalue},boost::python::api::object)
        """

    def extend(self, arg2: object) -> None:
        """
        extend( (IntU64Vector)arg1, (object)arg2) -> None :

            C++ signature :
                void extend(std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long>> {lvalue},boost::python::api::object)
        """


class IntVector:
    """
    A simple container for returning integers from Live.
    """

    def append(self, arg2: object) -> None:
        """
        append( (IntVector)arg1, (object)arg2) -> None :

            C++ signature :
                void append(std::__1::vector<int, std::__1::allocator<int>> {lvalue},boost::python::api::object)
        """

    def extend(self, arg2: object) -> None:
        """
        extend( (IntVector)arg1, (object)arg2) -> None :

            C++ signature :
                void extend(std::__1::vector<int, std::__1::allocator<int>> {lvalue},boost::python::api::object)
        """


class LimitationError:
    """
    Common base class for all non-exit exceptions.
    """

    def with_traceback(self) -> Any:
        """
        Exception.with_traceback(tb) --
        set self.__traceback__ to tb and return self.
        """

    args = None


class ObjectVector:
    """
    A simple read only container for returning python objects.
    """

    def append(self, arg2: object) -> None:
        """
        append( (ObjectVector)arg1, (object)arg2) -> None :

            C++ signature :
                void append(std::__1::vector<boost::python::api::object, std::__1::allocator<boost::python::api::object>> {lvalue},boost::python::api::object)
        """

    def extend(self, arg2: object) -> None:
        """
        extend( (ObjectVector)arg1, (object)arg2) -> None :

            C++ signature :
                void extend(std::__1::vector<boost::python::api::object, std::__1::allocator<boost::python::api::object>> {lvalue},boost::python::api::object)
        """


class StringVector:
    """
    A simple container for returning strings from Live.
    """

    def append(self, arg2: object) -> None:
        """
        append( (StringVector)arg1, (object)arg2) -> None :

            C++ signature :
                void append(std::__1::vector<TString, std::__1::allocator<TString>> {lvalue},boost::python::api::object)
        """

    def extend(self, arg2: object) -> None:
        """
        extend( (StringVector)arg1, (object)arg2) -> None :

            C++ signature :
                void extend(std::__1::vector<TString, std::__1::allocator<TString>> {lvalue},boost::python::api::object)
        """


class Text:
    """
    A translatable, immutable string.
    """

    @property
    def text(self) -> Any:
        pass


class Timer:
    """
    A timer that will trigger a callback after a certain inverval. The timer can be repeated and will trigger the callback every interval. Errors in the callback will stop the timer.
    """

    def restart(self) -> None:
        """
        restart( (Timer)arg1) -> None :

            C++ signature :
                void restart(PythonTimer {lvalue})
        """

    def start(self) -> None:
        """
        start( (Timer)arg1) -> None :

            C++ signature :
                void start(PythonTimer {lvalue})
        """

    def stop(self) -> None:
        """
        stop( (Timer)arg1) -> None :

            C++ signature :
                void stop(PythonTimer {lvalue})
        """

    @property
    def running(self) -> Any:
        pass


class Vector:
    """
    A simple read only container for returning objects from Live.
    """

    def append(self, arg2: object) -> None:
        """
        append( (Vector)arg1, (object)arg2) -> None :

            C++ signature :
                void append(std::__1::vector<TWeakPtr<TPyHandleBase>, std::__1::allocator<TWeakPtr<TPyHandleBase>>> {lvalue},boost::python::api::object)
        """

    def extend(self, arg2: object) -> None:
        """
        extend( (Vector)arg1, (object)arg2) -> None :

            C++ signature :
                void extend(std::__1::vector<TWeakPtr<TPyHandleBase>, std::__1::allocator<TWeakPtr<TPyHandleBase>>> {lvalue},boost::python::api::object)
        """


def get_text(classname: str, textname: str) -> Text:
    """
    get_text( (str)classname, (str)textname) -> Text :
        Retrieves the (translated) Text identified by `classname` and `textname`.

        C++ signature :
            TText const* get_text(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>,std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>)
    """


def log(arg1: str) -> None:
    """
    log( (str)arg1) -> None :

        C++ signature :
            void log(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>)
    """


def subst_args(arg1: str = "", arg2: str = "", arg3: str = "", arg4: str = "", arg5: str = "") -> str:
    """
    subst_args( (Text)text [, (str)arg1='' [, (str)arg2='' [, (str)arg3='' [, (str)arg4='' [, (str)arg5='']]]]]) -> str :

        C++ signature :
            std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>> subst_args(TText [,std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>='' [,std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>='' [,std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>='' [,std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>='' [,std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>='']]]]])
    """

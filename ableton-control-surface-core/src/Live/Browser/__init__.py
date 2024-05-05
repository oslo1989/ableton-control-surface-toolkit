from __future__ import annotations

from typing import Any, Callable

from Live import *
from Live.Application import *
from Live.Base import *
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


class Browser:
    """
    This class represents the live browser data base.
    """

    def add_filter_type_listener(self, listener: Callable) -> None:
        """
        add_filter_type_listener( (Browser)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "filter_type" has changed.

            C++ signature :
                void add_filter_type_listener(TPyHandle<ABrowserDelegate>,boost::python::api::object)
        """

    def add_full_refresh_listener(self, listener: Callable) -> None:
        """
        add_full_refresh_listener( (Browser)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "full_refresh" has changed.

            C++ signature :
                void add_full_refresh_listener(TPyHandle<ABrowserDelegate>,boost::python::api::object)
        """

    def add_hotswap_target_listener(self, listener: Callable) -> None:
        """
        add_hotswap_target_listener( (Browser)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "hotswap_target" has changed.

            C++ signature :
                void add_hotswap_target_listener(TPyHandle<ABrowserDelegate>,boost::python::api::object)
        """

    def filter_type_has_listener(self, listener: Callable) -> bool:
        """
        filter_type_has_listener( (Browser)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "filter_type".

            C++ signature :
                bool filter_type_has_listener(TPyHandle<ABrowserDelegate>,boost::python::api::object)
        """

    def full_refresh_has_listener(self, listener: Callable) -> bool:
        """
        full_refresh_has_listener( (Browser)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "full_refresh".

            C++ signature :
                bool full_refresh_has_listener(TPyHandle<ABrowserDelegate>,boost::python::api::object)
        """

    def hotswap_target_has_listener(self, listener: Callable) -> bool:
        """
        hotswap_target_has_listener( (Browser)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "hotswap_target".

            C++ signature :
                bool hotswap_target_has_listener(TPyHandle<ABrowserDelegate>,boost::python::api::object)
        """

    def load_item(self, arg2: object) -> None:
        """
        load_item( (Browser)arg1, (BrowserItem)arg2) -> None :
            Loads the provided browser item.

            C++ signature :
                void load_item(TPyHandle<ABrowserDelegate>,NPythonBrowser::TPythonBrowserItem)
        """

    def preview_item(self, arg2: object) -> None:
        """
        preview_item( (Browser)arg1, (BrowserItem)arg2) -> None :
            Previews the provided browser item.

            C++ signature :
                void preview_item(TPyHandle<ABrowserDelegate>,NPythonBrowser::TPythonBrowserItem)
        """

    def relation_to_hotswap_target(self, arg2: object) -> Relation:
        """
        relation_to_hotswap_target( (Browser)arg1, (BrowserItem)arg2) -> Relation :
            Returns the relation between the given browser item and the current hotswap target

            C++ signature :
                ableton::live_library::Relation relation_to_hotswap_target(TPyHandle<ABrowserDelegate>,NPythonBrowser::TPythonBrowserItem)
        """

    def remove_filter_type_listener(self, listener: Callable) -> None:
        """
        remove_filter_type_listener( (Browser)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "filter_type".

            C++ signature :
                void remove_filter_type_listener(TPyHandle<ABrowserDelegate>,boost::python::api::object)
        """

    def remove_full_refresh_listener(self, listener: Callable) -> None:
        """
        remove_full_refresh_listener( (Browser)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "full_refresh".

            C++ signature :
                void remove_full_refresh_listener(TPyHandle<ABrowserDelegate>,boost::python::api::object)
        """

    def remove_hotswap_target_listener(self, listener: Callable) -> None:
        """
        remove_hotswap_target_listener( (Browser)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "hotswap_target".

            C++ signature :
                void remove_hotswap_target_listener(TPyHandle<ABrowserDelegate>,boost::python::api::object)
        """

    def stop_preview(self) -> None:
        """
        stop_preview( (Browser)arg1) -> None :
            Stop the current preview.

            C++ signature :
                void stop_preview(TPyHandle<ABrowserDelegate>)
        """

    @property
    def audio_effects(self) -> Any:
        """
        Returns a browser item with access to all the Audio Effects content.
        """

    @property
    def clips(self) -> list[Clip]:
        """
        Returns a browser item with access to all the Clips content.
        """

    @property
    def colors(self) -> Any:
        """
        Returns a list of browser items containing the configured colors.
        """

    @property
    def current_project(self) -> Any:
        """
        Returns a browser item with access to all the Current Project content.
        """

    @property
    def drums(self) -> Any:
        """
        Returns a browser item with access to all the Drums content.
        """

    @property
    def filter_type(self) -> Any:
        """
        Bang triggered when the hotswap target has changed.
        """

    @property
    def hotswap_target(self) -> Any:
        """
        Bang triggered when the hotswap target has changed.
        """

    @property
    def instruments(self) -> Any:
        """
        Returns a browser item with access to all the Instruments content.
        """

    @property
    def legacy_libraries(self) -> Any:
        """
        Returns a list of browser items containing the installed legacy libraries. The list is always empty as legacy library handling has been removed.
        """

    @property
    def max_for_live(self) -> Any:
        """
        Returns a browser item with access to all the Max For Live content.
        """

    @property
    def midi_effects(self) -> Any:
        """
        Returns a browser item with access to all the Midi Effects content.
        """

    @property
    def packs(self) -> Any:
        """
        Returns a browser item with access to all the Packs content.
        """

    @property
    def plugins(self) -> Any:
        """
        Returns a browser item with access to all the Plugins content.
        """

    @property
    def samples(self) -> Any:
        """
        Returns a browser item with access to all the Samples content.
        """

    @property
    def sounds(self) -> Any:
        """
        Returns a browser item with access to all the Sounds content.
        """

    @property
    def user_folders(self) -> Any:
        """
        Returns a list of browser items containing all the user folders.
        """

    @property
    def user_library(self) -> Any:
        """
        Returns a browser item with access to all the User Library content.
        """


class BrowserItem:
    """
    This class represents an item of the browser hierarchy.
    """

    @property
    def children(self) -> Any:
        """
        Const access to the descendants of this browser item.
        """

    @property
    def is_device(self) -> bool:
        """
        Indicates if the browser item represents a device.
        """

    @property
    def is_folder(self) -> bool:
        """
        Indicates if the browser item represents folder.
        """

    @property
    def is_loadable(self) -> bool:
        """
        True if item can be loaded via the Browser's 'load_item' method.
        """

    @property
    def is_selected(self) -> bool:
        """
        True if the item is ancestor of or the actual selection.
        """

    @property
    def iter_children(self) -> Any:
        """
        Const iterable access to the descendants of this browser item.
        """

    @property
    def name(self) -> str:
        """
        Const access to the canonical display name of this browser item.
        """

    @property
    def source(self) -> Any:
        """
        Specifies where does item come from -- i.e. Live pack, user library...
        """

    @property
    def uri(self) -> Any:
        """
        The uri describes a unique identifier for a browser item.
        """


class BrowserItemIterator:
    """
    This class iterates over children of another BrowserItem.
    """


class BrowserItemVector:
    """
    A container for returning browser items from Live.
    """

    def append(self, arg2: object) -> None:
        """
        append( (BrowserItemVector)arg1, (object)arg2) -> None :

            C++ signature :
                void append(std::__1::vector<NPythonBrowser::TPythonBrowserItem, std::__1::allocator<NPythonBrowser::TPythonBrowserItem>> {lvalue},boost::python::api::object)
        """

    def extend(self, arg2: object) -> None:
        """
        extend( (BrowserItemVector)arg1, (object)arg2) -> None :

            C++ signature :
                void extend(std::__1::vector<NPythonBrowser::TPythonBrowserItem, std::__1::allocator<NPythonBrowser::TPythonBrowserItem>> {lvalue},boost::python::api::object)
        """


class FilterType:
    """
    Class that represent an enumeration of values for FilterType
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

    disabled = 0
    hotswap_off = 1
    instrument_hotswap = 2
    audio_effect_hotswap = 3
    midi_effect_hotswap = 4
    drum_pad_hotswap = 5
    midi_track_devices = 6
    samples = 7
    count = 8


class Relation:
    """
    Class that represent an enumeration of values for Relation
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

    ancestor = 0
    equal = 1
    descendant = 2
    none = 3

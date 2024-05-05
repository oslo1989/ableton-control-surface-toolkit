from __future__ import annotations

from typing import Any, Callable

from Live import *
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


class Application:
    """
    This class represents the Live application.
    """

    class View:
        """
        This class represents the view aspects of the Live application.
        """

        class NavDirection:
            """
            Class that represent an enumeration of values for NavDirection
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

            up = 0
            down = 1
            left = 2
            right = 3

        def add_browse_mode_listener(self, listener: Callable) -> None:
            """
            add_browse_mode_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "browse_mode" has changed.

                C++ signature :
                    void add_browse_mode_listener(TPyViewData<ASongApp>,boost::python::api::object)
            """

        def add_focused_document_view_listener(self, listener: Callable) -> None:
            """
            add_focused_document_view_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "focused_document_view" has changed.

                C++ signature :
                    void add_focused_document_view_listener(TPyViewData<ASongApp>,boost::python::api::object)
            """

        def add_is_view_visible_listener(self, arg2: object, listener: Callable) -> None:
            """
            add_is_view_visible_listener( (View)arg1, (object)arg2, (object)arg3) -> None :
                Add a listener function or method, which will be called as soon as the
                property "is_view_visible" has changed.

                C++ signature :
                    void add_is_view_visible_listener(TPyViewData<ASongApp>,TString,boost::python::api::object)
            """

        def add_view_focus_changed_listener(self, listener: Callable) -> None:
            """
            add_view_focus_changed_listener( (View)arg1, (object)arg2) -> None :
                Add a listener function or method, which will be called as soon as the
                property "view_focus_changed" has changed.

                C++ signature :
                    void add_view_focus_changed_listener(TPyViewData<ASongApp>,boost::python::api::object)
            """

        def available_main_views(self) -> StringVector:
            """
            available_main_views( (View)arg1) -> StringVector :
                Return a list of strings with the available subcomponent views, which
                is to be specified, when using the rest of this classes functions.
                A 'subcomponent view' is a main view component of a document view, like
                the Session view, the Arranger or Detailview and so on...

                C++ signature :
                    std::__1::vector<TString, std::__1::allocator<TString>> available_main_views(TPyViewData<ASongApp>)
            """

        def browse_mode_has_listener(self, listener: Callable) -> bool:
            """
            browse_mode_has_listener( (View)arg1, (object)arg2) -> bool :
                Returns true, if the given listener function or method is connected
                to the property "browse_mode".

                C++ signature :
                    bool browse_mode_has_listener(TPyViewData<ASongApp>,boost::python::api::object)
            """

        def focus_view(self, arg2: object) -> None:
            """
            focus_view( (View)arg1, (object)arg2) -> None :
                Show and focus one through the identifier string specified view.

                C++ signature :
                    void focus_view(TPyViewData<ASongApp>,TString)
            """

        def focused_document_view_has_listener(self, listener: Callable) -> bool:
            """
            focused_document_view_has_listener( (View)arg1, (object)arg2) -> bool :
                Returns true, if the given listener function or method is connected
                to the property "focused_document_view".

                C++ signature :
                    bool focused_document_view_has_listener(TPyViewData<ASongApp>,boost::python::api::object)
            """

        def hide_view(self, arg2: object) -> None:
            """
            hide_view( (View)arg1, (object)arg2) -> None :
                Hide one through the identifier string specified view.

                C++ signature :
                    void hide_view(TPyViewData<ASongApp>,TString)
            """

        def is_view_visible(self, identifier: object, main_window_only: bool = True) -> bool:
            """
            is_view_visible( (View)arg1, (object)identifier [, (bool)main_window_only=True]) -> bool :
                Return true if the through the identifier string specified view is currently
                visible. If main_window_only is set to False, this will also check in second
                window. Notifications from the second window are not yet supported.

                C++ signature :
                    bool is_view_visible(TPyViewData<ASongApp>,TString [,bool=True])
            """

        def is_view_visible_has_listener(self, arg2: object, listener: Callable) -> bool:
            """
            is_view_visible_has_listener( (View)arg1, (object)arg2, (object)arg3) -> bool :
                Returns true, if the given listener function or method is connected
                to the property "is_view_visible".

                C++ signature :
                    bool is_view_visible_has_listener(TPyViewData<ASongApp>,TString,boost::python::api::object)
            """

        def remove_browse_mode_listener(self, listener: Callable) -> None:
            """
            remove_browse_mode_listener( (View)arg1, (object)arg2) -> None :
                Remove a previously set listener function or method from
                property "browse_mode".

                C++ signature :
                    void remove_browse_mode_listener(TPyViewData<ASongApp>,boost::python::api::object)
            """

        def remove_focused_document_view_listener(self, listener: Callable) -> None:
            """
            remove_focused_document_view_listener( (View)arg1, (object)arg2) -> None :
                Remove a previously set listener function or method from
                property "focused_document_view".

                C++ signature :
                    void remove_focused_document_view_listener(TPyViewData<ASongApp>,boost::python::api::object)
            """

        def remove_is_view_visible_listener(self, arg2: object, listener: Callable) -> None:
            """
            remove_is_view_visible_listener( (View)arg1, (object)arg2, (object)arg3) -> None :
                Remove a previously set listener function or method from
                property "is_view_visible".

                C++ signature :
                    void remove_is_view_visible_listener(TPyViewData<ASongApp>,TString,boost::python::api::object)
            """

        def remove_view_focus_changed_listener(self, listener: Callable) -> None:
            """
            remove_view_focus_changed_listener( (View)arg1, (object)arg2) -> None :
                Remove a previously set listener function or method from
                property "view_focus_changed".

                C++ signature :
                    void remove_view_focus_changed_listener(TPyViewData<ASongApp>,boost::python::api::object)
            """

        def scroll_view(self, arg2: int, arg3: object, arg4: bool) -> None:
            """
            scroll_view( (View)arg1, (int)arg2, (object)arg3, (bool)arg4) -> None :
                Scroll through the identifier string specified view into the given
                direction, if possible.  Will silently return if the specified view
                can not perform the requested action.

                C++ signature :
                    void scroll_view(TPyViewData<ASongApp>,int,TString,bool)
            """

        def show_view(self, arg2: object) -> None:
            """
            show_view( (View)arg1, (object)arg2) -> None :
                Show one through the identifier string specified view. Will throw a
                runtime error if this is called in Live's initialization scope.

                C++ signature :
                    void show_view(TPyViewData<ASongApp>,TString)
            """

        def toggle_browse(self) -> None:
            """
            toggle_browse( (View)arg1) -> None :
                Reveals the device chain, the browser and starts hot swap for
                the selected device. Calling this function again stops hot swap.

                C++ signature :
                    void toggle_browse(TPyViewData<ASongApp>)
            """

        def view_focus_changed_has_listener(self, listener: Callable) -> bool:
            """
            view_focus_changed_has_listener( (View)arg1, (object)arg2) -> bool :
                Returns true, if the given listener function or method is connected
                to the property "view_focus_changed".

                C++ signature :
                    bool view_focus_changed_has_listener(TPyViewData<ASongApp>,boost::python::api::object)
            """

        def zoom_view(self, arg2: int, arg3: object, arg4: bool) -> None:
            """
            zoom_view( (View)arg1, (int)arg2, (object)arg3, (bool)arg4) -> None :
                Zoom through the identifier string specified view into the given
                direction, if possible.  Will silently return if the specified view
                can not perform the requested action.

                C++ signature :
                    void zoom_view(TPyViewData<ASongApp>,int,TString,bool)
            """

        @property
        def browse_mode(self) -> Any:
            """
            Return true if HotSwap mode is active for any target.
            """

        @property
        def canonical_parent(self) -> Any:
            """
            Get the canonical parent of the application view.
            """

        @property
        def focused_document_view(self) -> Any:
            """
            Return the name of the document view ('Session' or 'Arranger')
            shown in the currently selected window.
            """

    def add_average_process_usage_listener(self, listener: Callable) -> None:
        """
        add_average_process_usage_listener( (Application)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "average_process_usage" has changed.

            C++ signature :
                void add_average_process_usage_listener(TPyHandle<ASongApp>,boost::python::api::object)
        """

    def add_control_surfaces_listener(self, listener: Callable) -> None:
        """
        add_control_surfaces_listener( (Application)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "control_surfaces" has changed.

            C++ signature :
                void add_control_surfaces_listener(TPyHandle<ASongApp>,boost::python::api::object)
        """

    def add_open_dialog_count_listener(self, listener: Callable) -> None:
        """
        add_open_dialog_count_listener( (Application)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "open_dialog_count" has changed.

            C++ signature :
                void add_open_dialog_count_listener(TPyHandle<ASongApp>,boost::python::api::object)
        """

    def add_peak_process_usage_listener(self, listener: Callable) -> None:
        """
        add_peak_process_usage_listener( (Application)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "peak_process_usage" has changed.

            C++ signature :
                void add_peak_process_usage_listener(TPyHandle<ASongApp>,boost::python::api::object)
        """

    def add_unavailable_features_listener(self, listener: Callable) -> None:
        """
        add_unavailable_features_listener( (Application)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "unavailable_features" has changed.

            C++ signature :
                void add_unavailable_features_listener(TPyHandle<ASongApp>,boost::python::api::object)
        """

    def average_process_usage_has_listener(self, listener: Callable) -> bool:
        """
        average_process_usage_has_listener( (Application)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "average_process_usage".

            C++ signature :
                bool average_process_usage_has_listener(TPyHandle<ASongApp>,boost::python::api::object)
        """

    def control_surfaces_has_listener(self, listener: Callable) -> bool:
        """
        control_surfaces_has_listener( (Application)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "control_surfaces".

            C++ signature :
                bool control_surfaces_has_listener(TPyHandle<ASongApp>,boost::python::api::object)
        """

    def get_bugfix_version(self) -> int:
        """
        get_bugfix_version( (Application)arg1) -> int :
            Returns an integer representing the bugfix version of Live.

            C++ signature :
                int get_bugfix_version(TPyHandle<ASongApp>)
        """

    def get_build_id(self) -> str:
        """
        get_build_id( (Application)arg1) -> str :
            Returns a string identifying the build.

            C++ signature :
                TString get_build_id(TPyHandle<ASongApp>)
        """

    def get_document(self) -> Song:
        """
        get_document( (Application)arg1) -> Song :
            Returns the current Live Set.

            C++ signature :
                TWeakPtr<TPyHandle<ASong>> get_document(TPyHandle<ASongApp>)
        """

    def get_major_version(self) -> int:
        """
        get_major_version( (Application)arg1) -> int :
            Returns an integer representing the major version of Live.

            C++ signature :
                int get_major_version(TPyHandle<ASongApp>)
        """

    def get_minor_version(self) -> int:
        """
        get_minor_version( (Application)arg1) -> int :
            Returns an integer representing the minor version of Live.

            C++ signature :
                int get_minor_version(TPyHandle<ASongApp>)
        """

    def get_variant(self) -> str:
        """
        get_variant( (Application)arg1) -> str :
            Returns one of the strings in Live.Application.Variants.

            C++ signature :
                TString get_variant(TPyHandle<ASongApp>)
        """

    def get_version_string(self) -> str:
        """
        get_version_string( (Application)arg1) -> str :
            Returns the full version string of Live.

            C++ signature :
                TString get_version_string(TPyHandle<ASongApp>)
        """

    def has_option(self, arg2: object) -> bool:
        """
        has_option( (Application)arg1, (object)arg2) -> bool :
            Returns True if the given entry exists in Options.txt, False otherwise.

            C++ signature :
                bool has_option(TPyHandle<ASongApp>,TString)
        """

    def open_dialog_count_has_listener(self, listener: Callable) -> bool:
        """
        open_dialog_count_has_listener( (Application)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "open_dialog_count".

            C++ signature :
                bool open_dialog_count_has_listener(TPyHandle<ASongApp>,boost::python::api::object)
        """

    def peak_process_usage_has_listener(self, listener: Callable) -> bool:
        """
        peak_process_usage_has_listener( (Application)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "peak_process_usage".

            C++ signature :
                bool peak_process_usage_has_listener(TPyHandle<ASongApp>,boost::python::api::object)
        """

    def press_current_dialog_button(self, arg2: int) -> None:
        """
        press_current_dialog_button( (Application)arg1, (int)arg2) -> None :
            Press a button, by index, on the current message box.

            C++ signature :
                void press_current_dialog_button(TPyHandle<ASongApp>,int)
        """

    def remove_average_process_usage_listener(self, listener: Callable) -> None:
        """
        remove_average_process_usage_listener( (Application)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "average_process_usage".

            C++ signature :
                void remove_average_process_usage_listener(TPyHandle<ASongApp>,boost::python::api::object)
        """

    def remove_control_surfaces_listener(self, listener: Callable) -> None:
        """
        remove_control_surfaces_listener( (Application)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "control_surfaces".

            C++ signature :
                void remove_control_surfaces_listener(TPyHandle<ASongApp>,boost::python::api::object)
        """

    def remove_open_dialog_count_listener(self, listener: Callable) -> None:
        """
        remove_open_dialog_count_listener( (Application)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "open_dialog_count".

            C++ signature :
                void remove_open_dialog_count_listener(TPyHandle<ASongApp>,boost::python::api::object)
        """

    def remove_peak_process_usage_listener(self, listener: Callable) -> None:
        """
        remove_peak_process_usage_listener( (Application)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "peak_process_usage".

            C++ signature :
                void remove_peak_process_usage_listener(TPyHandle<ASongApp>,boost::python::api::object)
        """

    def remove_unavailable_features_listener(self, listener: Callable) -> None:
        """
        remove_unavailable_features_listener( (Application)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "unavailable_features".

            C++ signature :
                void remove_unavailable_features_listener(TPyHandle<ASongApp>,boost::python::api::object)
        """

    def show_message(
        self, text: object, buttons: int = 0, enable_markup: bool = False, show_success_icon: bool = False
    ) -> int:
        """
        show_message( (Application)arg1, (Text)text [, (int)buttons=Application.MessageButtons.OK_BUTTON [, (bool)enable_markup=False [, (bool)show_success_icon=False]]]) -> int :
            Shows a message box, returning the position of the pressed button.

            C++ signature :
                int show_message(TPyHandle<ASongApp>,TText [,int=Application.MessageButtons.OK_BUTTON [,bool=False [,bool=False]]])
        """

    def show_on_the_fly_message(
        self, message: str, buttons: int = 0, enable_markup: bool = False, show_success_icon: bool = False
    ) -> int:
        """
        show_on_the_fly_message( (Application)arg1, (str)message [, (int)buttons=Application.MessageButtons.OK_BUTTON [, (bool)enable_markup=False [, (bool)show_success_icon=False]]]) -> int :
            Same as show_message, but for when there is no predefined Text object.

            C++ signature :
                int show_on_the_fly_message(TPyHandle<ASongApp>,std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>> [,int=Application.MessageButtons.OK_BUTTON [,bool=False [,bool=False]]])
        """

    def unavailable_features_has_listener(self, listener: Callable) -> bool:
        """
        unavailable_features_has_listener( (Application)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "unavailable_features".

            C++ signature :
                bool unavailable_features_has_listener(TPyHandle<ASongApp>,boost::python::api::object)
        """

    @property
    def average_process_usage(self) -> Any:
        """
        Reports Live's average CPU load.
        """

    @property
    def browser(self) -> Any:
        """
        Returns an interface to the browser.
        """

    @property
    def canonical_parent(self) -> Any:
        """
        Returns the canonical parent of the application.
        """

    @property
    def control_surfaces(self) -> Any:
        """
        Const access to a list of the control surfaces selected in preferences, in the same order.
        The list contains None if no control surface is active at that index.
        """

    @property
    def current_dialog_button_count(self) -> Any:
        """
        Number of buttons on the current dialog.
        """

    @property
    def current_dialog_message(self) -> Any:
        """
        Text of the last dialog that appeared; Empty if all dialogs just disappeared.
        """

    @property
    def number_of_push_apps_running(self) -> Any:
        """
        Returns the number of connected Push apps.
        """

    @property
    def open_dialog_count(self) -> Any:
        """
        The number of open dialogs in Live. 0 if not dialog is open.
        """

    @property
    def peak_process_usage(self) -> Any:
        """
        Reports Live's peak CPU load.
        """

    @property
    def unavailable_features(self) -> Any:
        """
        List of features that are unavailable due to limitations of the current Live edition.
        """

    @property
    def view(self) -> View:
        """
        Returns the applications view component.
        """


class ControlDescription:
    """
    Describes a control present in a control surface proxy
    """

    @property
    def id(self) -> Any:
        pass

    @property
    def name(self) -> str:
        pass


class ControlDescriptionVector:
    """
    A container for returning control descriptions.
    """

    def append(self, arg2: object) -> None:
        """
        append( (ControlDescriptionVector)arg1, (object)arg2) -> None :

            C++ signature :
                void append(std::__1::vector<TControlDescription, std::__1::allocator<TControlDescription>> {lvalue},boost::python::api::object)
        """

    def extend(self, arg2: object) -> None:
        """
        extend( (ControlDescriptionVector)arg1, (object)arg2) -> None :

            C++ signature :
                void extend(std::__1::vector<TControlDescription, std::__1::allocator<TControlDescription>> {lvalue},boost::python::api::object)
        """


class ControlSurfaceProxy:
    """
    Represents a control surface running in a different process. For use by M4L
    """

    def add_control_values_arrived_listener(self, listener: Callable) -> None:
        """
        add_control_values_arrived_listener( (ControlSurfaceProxy)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "control_values_arrived" has changed.

            C++ signature :
                void add_control_values_arrived_listener(APythonControlSurfaceProxy,boost::python::api::object)
        """

    def add_midi_received_listener(self, listener: Callable) -> None:
        """
        add_midi_received_listener( (ControlSurfaceProxy)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "midi_received" has changed.

            C++ signature :
                void add_midi_received_listener(APythonControlSurfaceProxy,boost::python::api::object)
        """

    def control_values_arrived_has_listener(self, listener: Callable) -> bool:
        """
        control_values_arrived_has_listener( (ControlSurfaceProxy)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "control_values_arrived".

            C++ signature :
                bool control_values_arrived_has_listener(APythonControlSurfaceProxy,boost::python::api::object)
        """

    def enable_receive_midi(self, arg2: bool) -> None:
        """
        enable_receive_midi( (ControlSurfaceProxy)arg1, (bool)arg2) -> None :

            C++ signature :
                void enable_receive_midi(APythonControlSurfaceProxy {lvalue},bool)
        """

    def fetch_received_midi_messages(self) -> tuple:
        """
        fetch_received_midi_messages( (ControlSurfaceProxy)arg1) -> tuple :

            C++ signature :
                boost::python::tuple fetch_received_midi_messages(APythonControlSurfaceProxy {lvalue})
        """

    def fetch_received_values(self) -> tuple:
        """
        fetch_received_values( (ControlSurfaceProxy)arg1) -> tuple :

            C++ signature :
                boost::python::tuple fetch_received_values(APythonControlSurfaceProxy {lvalue})
        """

    def grab_control(self, arg2: int) -> None:
        """
        grab_control( (ControlSurfaceProxy)arg1, (int)arg2) -> None :

            C++ signature :
                void grab_control(APythonControlSurfaceProxy {lvalue},int)
        """

    def midi_received_has_listener(self, listener: Callable) -> bool:
        """
        midi_received_has_listener( (ControlSurfaceProxy)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "midi_received".

            C++ signature :
                bool midi_received_has_listener(APythonControlSurfaceProxy,boost::python::api::object)
        """

    def release_control(self, arg2: int) -> None:
        """
        release_control( (ControlSurfaceProxy)arg1, (int)arg2) -> None :

            C++ signature :
                void release_control(APythonControlSurfaceProxy {lvalue},int)
        """

    def remove_control_values_arrived_listener(self, listener: Callable) -> None:
        """
        remove_control_values_arrived_listener( (ControlSurfaceProxy)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "control_values_arrived".

            C++ signature :
                void remove_control_values_arrived_listener(APythonControlSurfaceProxy,boost::python::api::object)
        """

    def remove_midi_received_listener(self, listener: Callable) -> None:
        """
        remove_midi_received_listener( (ControlSurfaceProxy)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "midi_received".

            C++ signature :
                void remove_midi_received_listener(APythonControlSurfaceProxy,boost::python::api::object)
        """

    def send_midi(self, arg2: object) -> None:
        """
        send_midi( (ControlSurfaceProxy)arg1, (tuple)arg2) -> None :

            C++ signature :
                void send_midi(APythonControlSurfaceProxy {lvalue},boost::python::tuple)
        """

    def send_value(self, arg2: object) -> None:
        """
        send_value( (ControlSurfaceProxy)arg1, (tuple)arg2) -> None :

            C++ signature :
                void send_value(APythonControlSurfaceProxy {lvalue},boost::python::tuple)
        """

    def subscribe_to_control(self, arg2: int) -> None:
        """
        subscribe_to_control( (ControlSurfaceProxy)arg1, (int)arg2) -> None :

            C++ signature :
                void subscribe_to_control(APythonControlSurfaceProxy {lvalue},int)
        """

    def unsubscribe_from_control(self, arg2: int) -> None:
        """
        unsubscribe_from_control( (ControlSurfaceProxy)arg1, (int)arg2) -> None :

            C++ signature :
                void unsubscribe_from_control(APythonControlSurfaceProxy {lvalue},int)
        """

    @property
    def control_descriptions(self) -> Any:
        pass

    @property
    def type_name(self) -> str:
        pass


class MessageButtons:
    """
    Class that represent an enumeration of values for MessageButtons
    Specifies the characteristics of the message box, e.g. which buttons to show.
    """

    OK_BUTTON = 0


class UnavailableFeature:
    """
    Class that represent an enumeration of values for UnavailableFeature
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

    note_velocity_ranges_and_probabilities = 0


class UnavailableFeatureVector:
    """
    A container for returning unavailable features.
    """

    def append(self, arg2: object) -> None:
        """
        append( (UnavailableFeatureVector)arg1, (object)arg2) -> None :

            C++ signature :
                void append(std::__1::vector<NPythonApplication::TUnavailableFeature, std::__1::allocator<NPythonApplication::TUnavailableFeature>> {lvalue},boost::python::api::object)
        """

    def extend(self, arg2: object) -> None:
        """
        extend( (UnavailableFeatureVector)arg1, (object)arg2) -> None :

            C++ signature :
                void extend(std::__1::vector<NPythonApplication::TUnavailableFeature, std::__1::allocator<NPythonApplication::TUnavailableFeature>> {lvalue},boost::python::api::object)
        """


class Variants:
    """
    Holds strings representing what type of Live is running.
    """

    BETA = "Beta"
    INTRO = "Intro"
    LITE = "Lite"
    STANDARD = "Standard"
    SUITE = "Suite"
    TRIAL = "Trial"


def combine_apcs() -> bool:
    """
    combine_apcs() -> bool :
        Returns true if multiple APCs should be combined.

        C++ signature :
            bool combine_apcs()
    """


def encrypt_challenge(dongle1: int, dongle2: int, key_index: int = 0) -> tuple:
    """
    encrypt_challenge( (int)dongle1, (int)dongle2 [, (int)key_index=0]) -> tuple :
        Returns an encrypted challenge based on the TEA algortithm

        C++ signature :
            boost::python::tuple encrypt_challenge(int,int [,int=0])
    """


def encrypt_challenge2(arg1: int) -> int:
    """
    encrypt_challenge2( (int)arg1) -> int :
        Returns the UMAC hash for the given challenge.

        C++ signature :
            int encrypt_challenge2(int)
    """


def get_application() -> Application:
    """
    get_application() -> Application :
        Returns the application instance.

        C++ signature :
            TWeakPtr<TPyHandle<ASongApp>> get_application()
    """


def get_random_int(arg1: int, arg2: int) -> int:
    """
    get_random_int( (int)arg1, (int)arg2) -> int :
        Returns a random integer from the given range.

        C++ signature :
            int get_random_int(int,int)
    """

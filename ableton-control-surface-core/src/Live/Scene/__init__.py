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
from Live.ShifterDevice import *
from Live.SimplerDevice import *
from Live.Song import *
from Live.SpectralResonatorDevice import *
from Live.Track import *
from Live.WavetableDevice import *


class Scene:
    """
    This class represents an series of ClipSlots in Lives Sessionview matrix.
    """

    def add_clip_slots_listener(self, listener: Callable) -> None:
        """
        add_clip_slots_listener( (Scene)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "clip_slots" has changed.

            C++ signature :
                void add_clip_slots_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    def add_color_index_listener(self, listener: Callable) -> None:
        """
        add_color_index_listener( (Scene)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "color_index" has changed.

            C++ signature :
                void add_color_index_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    def add_color_listener(self, listener: Callable) -> None:
        """
        add_color_listener( (Scene)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "color" has changed.

            C++ signature :
                void add_color_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    def add_is_triggered_listener(self, listener: Callable) -> None:
        """
        add_is_triggered_listener( (Scene)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "is_triggered" has changed.

            C++ signature :
                void add_is_triggered_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    def add_name_listener(self, listener: Callable) -> None:
        """
        add_name_listener( (Scene)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "name" has changed.

            C++ signature :
                void add_name_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    def add_tempo_enabled_listener(self, listener: Callable) -> None:
        """
        add_tempo_enabled_listener( (Scene)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "tempo_enabled" has changed.

            C++ signature :
                void add_tempo_enabled_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    def add_tempo_listener(self, listener: Callable) -> None:
        """
        add_tempo_listener( (Scene)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "tempo" has changed.

            C++ signature :
                void add_tempo_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    def add_time_signature_denominator_listener(self, listener: Callable) -> None:
        """
        add_time_signature_denominator_listener( (Scene)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "time_signature_denominator" has changed.

            C++ signature :
                void add_time_signature_denominator_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    def add_time_signature_enabled_listener(self, listener: Callable) -> None:
        """
        add_time_signature_enabled_listener( (Scene)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "time_signature_enabled" has changed.

            C++ signature :
                void add_time_signature_enabled_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    def add_time_signature_numerator_listener(self, listener: Callable) -> None:
        """
        add_time_signature_numerator_listener( (Scene)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "time_signature_numerator" has changed.

            C++ signature :
                void add_time_signature_numerator_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    def clip_slots_has_listener(self, listener: Callable) -> bool:
        """
        clip_slots_has_listener( (Scene)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "clip_slots".

            C++ signature :
                bool clip_slots_has_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    def color_has_listener(self, listener: Callable) -> bool:
        """
        color_has_listener( (Scene)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "color".

            C++ signature :
                bool color_has_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    def color_index_has_listener(self, listener: Callable) -> bool:
        """
        color_index_has_listener( (Scene)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "color_index".

            C++ signature :
                bool color_index_has_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    def fire(self, force_legato: bool = False, can_select_scene_on_launch: bool = True) -> None:
        """
        fire( (Scene)arg1 [, (bool)force_legato=False [, (bool)can_select_scene_on_launch=True]]) -> None :
            Fire the scene directly. Will fire all clipslots that this scene owns and
            select the scene itself.

            C++ signature :
                void fire(TPyHandle<AScene> [,bool=False [,bool=True]])
        """

    def fire_as_selected(self, force_legato: bool = False) -> None:
        """
        fire_as_selected( (Scene)arg1 [, (bool)force_legato=False]) -> None :
            Fire the selected scene. Will fire all clipslots that this scene owns and
            select the next scene if necessary.

            C++ signature :
                void fire_as_selected(TPyHandle<AScene> [,bool=False])
        """

    def is_triggered_has_listener(self, listener: Callable) -> bool:
        """
        is_triggered_has_listener( (Scene)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "is_triggered".

            C++ signature :
                bool is_triggered_has_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    def name_has_listener(self, listener: Callable) -> bool:
        """
        name_has_listener( (Scene)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "name".

            C++ signature :
                bool name_has_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    def remove_clip_slots_listener(self, listener: Callable) -> None:
        """
        remove_clip_slots_listener( (Scene)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "clip_slots".

            C++ signature :
                void remove_clip_slots_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    def remove_color_index_listener(self, listener: Callable) -> None:
        """
        remove_color_index_listener( (Scene)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "color_index".

            C++ signature :
                void remove_color_index_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    def remove_color_listener(self, listener: Callable) -> None:
        """
        remove_color_listener( (Scene)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "color".

            C++ signature :
                void remove_color_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    def remove_is_triggered_listener(self, listener: Callable) -> None:
        """
        remove_is_triggered_listener( (Scene)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "is_triggered".

            C++ signature :
                void remove_is_triggered_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    def remove_name_listener(self, listener: Callable) -> None:
        """
        remove_name_listener( (Scene)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "name".

            C++ signature :
                void remove_name_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    def remove_tempo_enabled_listener(self, listener: Callable) -> None:
        """
        remove_tempo_enabled_listener( (Scene)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "tempo_enabled".

            C++ signature :
                void remove_tempo_enabled_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    def remove_tempo_listener(self, listener: Callable) -> None:
        """
        remove_tempo_listener( (Scene)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "tempo".

            C++ signature :
                void remove_tempo_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    def remove_time_signature_denominator_listener(self, listener: Callable) -> None:
        """
        remove_time_signature_denominator_listener( (Scene)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "time_signature_denominator".

            C++ signature :
                void remove_time_signature_denominator_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    def remove_time_signature_enabled_listener(self, listener: Callable) -> None:
        """
        remove_time_signature_enabled_listener( (Scene)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "time_signature_enabled".

            C++ signature :
                void remove_time_signature_enabled_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    def remove_time_signature_numerator_listener(self, listener: Callable) -> None:
        """
        remove_time_signature_numerator_listener( (Scene)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "time_signature_numerator".

            C++ signature :
                void remove_time_signature_numerator_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    def set_fire_button_state(self, arg2: bool) -> None:
        """
        set_fire_button_state( (Scene)arg1, (bool)arg2) -> None :
            Set the scene's fire button state directly. Supports all launch modes.

            C++ signature :
                void set_fire_button_state(TPyHandle<AScene>,bool)
        """

    def tempo_enabled_has_listener(self, listener: Callable) -> bool:
        """
        tempo_enabled_has_listener( (Scene)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "tempo_enabled".

            C++ signature :
                bool tempo_enabled_has_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    def tempo_has_listener(self, listener: Callable) -> bool:
        """
        tempo_has_listener( (Scene)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "tempo".

            C++ signature :
                bool tempo_has_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    def time_signature_denominator_has_listener(self, listener: Callable) -> bool:
        """
        time_signature_denominator_has_listener( (Scene)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "time_signature_denominator".

            C++ signature :
                bool time_signature_denominator_has_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    def time_signature_enabled_has_listener(self, listener: Callable) -> bool:
        """
        time_signature_enabled_has_listener( (Scene)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "time_signature_enabled".

            C++ signature :
                bool time_signature_enabled_has_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    def time_signature_numerator_has_listener(self, listener: Callable) -> bool:
        """
        time_signature_numerator_has_listener( (Scene)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "time_signature_numerator".

            C++ signature :
                bool time_signature_numerator_has_listener(TPyHandle<AScene>,boost::python::api::object)
        """

    @property
    def canonical_parent(self) -> Any:
        """
        Get the canonical parent of the scene.
        """

    @property
    def clip_slots(self) -> list[ClipSlot]:
        """
        return a list of clipslots (see class AClipSlot) that this scene covers.
        """

    @property
    def color(self) -> Any:
        """
        Get/set access to the color of the scene (RGB).
        """

    @color.setter
    def color(self, value: Any) -> None:
        pass

    @property
    def color_index(self) -> Any:
        """
        Get/set access to the color index of the scene. Can be None for no color.
        """

    @color_index.setter
    def color_index(self, value: Any) -> None:
        pass

    @property
    def is_empty(self) -> bool:
        """
        Returns True if all clip slots of this scene are empty.
        """

    @property
    def is_triggered(self) -> bool:
        """
        Const access to the scene's trigger state.
        """

    @property
    def name(self) -> str:
        """
        Get/Set the name of the scene.
        """

    @name.setter
    def name(self, value: str) -> None:
        pass

    @property
    def tempo(self) -> float:
        """
        Get/Set the tempo value of the scene.
        The song will use the scene's tempo as soon as the scene is fired.
        Returns -1 if the scene has no tempo property.
        """

    @tempo.setter
    def tempo(self, value: float) -> None:
        pass

    @property
    def tempo_enabled(self) -> Any:
        """
        Get/Set the active state of the scene tempo.
        When disabled, the scene will use the song's tempo,and the tempo value returned will be -1Returns a bool indicating the state of the scene's tempo
        """

    @tempo_enabled.setter
    def tempo_enabled(self, value: Any) -> None:
        pass

    @property
    def time_signature_denominator(self) -> Any:
        """
        Get/Set the scene's time signature denominator.
        The song will use the scene's time signature as soon as the scene is fired.
        Returns -1 if the scene has no time signature property.
        """

    @time_signature_denominator.setter
    def time_signature_denominator(self, value: Any) -> None:
        pass

    @property
    def time_signature_enabled(self) -> Any:
        """
        Get the active state of the scene time signature.
        When disabled, the scene will use the song's time signature,and the time signature values returned will be -1Returns a bool indicating the state of the scene's time signature
        """

    @property
    def time_signature_numerator(self) -> Any:
        """
        Get/Set the scene's time signature numerator.
        The song will use the scene's time signature as soon as the scene is fired.
        Returns -1 if the scene has no time signature property.
        """

    @time_signature_numerator.setter
    def time_signature_numerator(self, value: Any) -> None:
        pass

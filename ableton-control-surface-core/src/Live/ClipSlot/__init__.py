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


class ClipSlot:
    """
    This class represents an entry in Lives Session view matrix.
    """

    def add_color_index_listener(self, listener: Callable) -> None:
        """
        add_color_index_listener( (ClipSlot)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "color_index" has changed.

            C++ signature :
                void add_color_index_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
        """

    def add_color_listener(self, listener: Callable) -> None:
        """
        add_color_listener( (ClipSlot)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "color" has changed.

            C++ signature :
                void add_color_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
        """

    def add_controls_other_clips_listener(self, listener: Callable) -> None:
        """
        add_controls_other_clips_listener( (ClipSlot)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "controls_other_clips" has changed.

            C++ signature :
                void add_controls_other_clips_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
        """

    def add_has_clip_listener(self, listener: Callable) -> None:
        """
        add_has_clip_listener( (ClipSlot)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "has_clip" has changed.

            C++ signature :
                void add_has_clip_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
        """

    def add_has_stop_button_listener(self, listener: Callable) -> None:
        """
        add_has_stop_button_listener( (ClipSlot)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "has_stop_button" has changed.

            C++ signature :
                void add_has_stop_button_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
        """

    def add_is_triggered_listener(self, listener: Callable) -> None:
        """
        add_is_triggered_listener( (ClipSlot)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "is_triggered" has changed.

            C++ signature :
                void add_is_triggered_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
        """

    def add_playing_status_listener(self, listener: Callable) -> None:
        """
        add_playing_status_listener( (ClipSlot)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "playing_status" has changed.

            C++ signature :
                void add_playing_status_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
        """

    def color_has_listener(self, listener: Callable) -> bool:
        """
        color_has_listener( (ClipSlot)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "color".

            C++ signature :
                bool color_has_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
        """

    def color_index_has_listener(self, listener: Callable) -> bool:
        """
        color_index_has_listener( (ClipSlot)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "color_index".

            C++ signature :
                bool color_index_has_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
        """

    def controls_other_clips_has_listener(self, listener: Callable) -> bool:
        """
        controls_other_clips_has_listener( (ClipSlot)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "controls_other_clips".

            C++ signature :
                bool controls_other_clips_has_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
        """

    def create_clip(self, arg2: float) -> None:
        """
        create_clip( (ClipSlot)arg1, (float)arg2) -> None :
            Creates an empty clip with the given length in the slot.
            Throws an error when called on non-empty slots or slots in non-MIDI tracks.

            C++ signature :
                void create_clip(TPyHandle<AGroupAndClipSlotBase>,double)
        """

    def delete_clip(self) -> None:
        """
        delete_clip( (ClipSlot)arg1) -> None :
            Removes the clip contained in the slot.
            Raises an exception if the slot was empty.

            C++ signature :
                void delete_clip(TPyHandle<AGroupAndClipSlotBase>)
        """

    def duplicate_clip_to(self, arg2: object) -> None:
        """
        duplicate_clip_to( (ClipSlot)arg1, (ClipSlot)arg2) -> None :
            Duplicates the slot's clip to the passed in target slot.
            Overrides the target's clip if it's not empty.
            Raises an exception if the (source) slot itself is empty, or if source and
            target have different track types (audio vs. MIDI). Also raises if the source
            or target slot is in a group track (so called group slot).

            C++ signature :
                void duplicate_clip_to(TPyHandle<AGroupAndClipSlotBase>,TPyHandle<AGroupAndClipSlotBase>)
        """

    def fire(self) -> None:
        """
        fire( (ClipSlot)arg1) -> None :
            Fire a Clip if this Clipslot owns one, else trigger the stop button,
            if we have one.

            C++ signature :
                void fire(TPyHandle<AGroupAndClipSlotBase>)

        fire( (ClipSlot)self [, (float)record_length=1.7976931348623157e+308 [, (int)launch_quantization=-2147483648 [, (bool)force_legato=False]]]) -> None :
            If 'record_length' is passed, the clip will be refired after the given recording length.  Raises an error if the slot owns a clip.
            'launch_quantization' determines the quantization of global transport that is applied overriding the value in the song.
            'force_legato' will make the clip play inmediatelly. The playhead will be moved to keep the clip synchronized.

            C++ signature :
                void fire(TPyHandle<AGroupAndClipSlotBase> [,double=1.7976931348623157e+308 [,int=-2147483648 [,bool=False]]])
        """

    def has_clip_has_listener(self, listener: Callable) -> bool:
        """
        has_clip_has_listener( (ClipSlot)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "has_clip".

            C++ signature :
                bool has_clip_has_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
        """

    def has_stop_button_has_listener(self, listener: Callable) -> bool:
        """
        has_stop_button_has_listener( (ClipSlot)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "has_stop_button".

            C++ signature :
                bool has_stop_button_has_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
        """

    def is_triggered_has_listener(self, listener: Callable) -> bool:
        """
        is_triggered_has_listener( (ClipSlot)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "is_triggered".

            C++ signature :
                bool is_triggered_has_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
        """

    def playing_status_has_listener(self, listener: Callable) -> bool:
        """
        playing_status_has_listener( (ClipSlot)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "playing_status".

            C++ signature :
                bool playing_status_has_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
        """

    def remove_color_index_listener(self, listener: Callable) -> None:
        """
        remove_color_index_listener( (ClipSlot)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "color_index".

            C++ signature :
                void remove_color_index_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
        """

    def remove_color_listener(self, listener: Callable) -> None:
        """
        remove_color_listener( (ClipSlot)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "color".

            C++ signature :
                void remove_color_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
        """

    def remove_controls_other_clips_listener(self, listener: Callable) -> None:
        """
        remove_controls_other_clips_listener( (ClipSlot)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "controls_other_clips".

            C++ signature :
                void remove_controls_other_clips_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
        """

    def remove_has_clip_listener(self, listener: Callable) -> None:
        """
        remove_has_clip_listener( (ClipSlot)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "has_clip".

            C++ signature :
                void remove_has_clip_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
        """

    def remove_has_stop_button_listener(self, listener: Callable) -> None:
        """
        remove_has_stop_button_listener( (ClipSlot)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "has_stop_button".

            C++ signature :
                void remove_has_stop_button_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
        """

    def remove_is_triggered_listener(self, listener: Callable) -> None:
        """
        remove_is_triggered_listener( (ClipSlot)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "is_triggered".

            C++ signature :
                void remove_is_triggered_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
        """

    def remove_playing_status_listener(self, listener: Callable) -> None:
        """
        remove_playing_status_listener( (ClipSlot)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "playing_status".

            C++ signature :
                void remove_playing_status_listener(TPyHandle<AGroupAndClipSlotBase>,boost::python::api::object)
        """

    def set_fire_button_state(self, arg2: bool) -> None:
        """
        set_fire_button_state( (ClipSlot)arg1, (bool)arg2) -> None :
            Set the clipslot's fire button state directly. Supports all launch modes.

            C++ signature :
                void set_fire_button_state(TPyHandle<AGroupAndClipSlotBase>,bool)
        """

    def stop(self) -> None:
        """
        stop( (ClipSlot)arg1) -> None :
            Stop playing the contained Clip, if there is a Clip and its currently
            playing.

            C++ signature :
                void stop(TPyHandle<AGroupAndClipSlotBase>)
        """

    @property
    def canonical_parent(self) -> Any:
        """
        Get the canonical parent of the ClipSlot.
        """

    @property
    def clip(self) -> Clip:
        """
        Returns the Clip which this clipslots currently owns. Might be None.
        """

    @property
    def color(self) -> Any:
        """
        Returns the canonical color for the clip slot or None if it does not exist.
        """

    @property
    def color_index(self) -> Any:
        """
        Returns the canonical color index for the clip slot or None if it does not exist.
        """

    @property
    def controls_other_clips(self) -> list[Clip]:
        """
        Returns true if firing this slot will fire clips in other slots.
        Can only be true for slots in group tracks.
        """

    @property
    def has_clip(self) -> bool:
        """
        Returns true if this Clipslot owns a Clip.
        """

    @property
    def has_stop_button(self) -> bool:
        """
        Get/Set if this Clip has a stop button, which will, if fired, stop any
        other Clip that is currently playing the Track we do belong to.
        """

    @has_stop_button.setter
    def has_stop_button(self, value: bool) -> None:
        pass

    @property
    def is_group_slot(self) -> bool:
        """
        Returns whether this clip slot is a group track slot (group slot).
        """

    @property
    def is_playing(self) -> bool:
        """
        Returns whether the clip associated with the slot is playing.
        """

    @property
    def is_recording(self) -> bool:
        """
        Returns whether the clip associated with the slot is recording.
        """

    @property
    def is_triggered(self) -> bool:
        """
        Const access to the triggering state of the clip slot.
        """

    @property
    def playing_status(self) -> Any:
        """
        Const access to the playing state of the clip slot.
        Can be either stopped, playing, or recording.
        """

    @property
    def will_record_on_start(self) -> Any:
        """
        returns true if the clip slot will record on being fired.
        """


class ClipSlotPlayingState:
    """
    Class that represent an enumeration of values for ClipSlotPlayingState
    """

    stopped = 0
    started = 1
    recording = 2

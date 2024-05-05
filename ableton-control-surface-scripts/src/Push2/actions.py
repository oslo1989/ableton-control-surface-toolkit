# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/actions.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1849 bytes
from ableton.v2.base import liveobj_valid
from pushbase.actions import CaptureAndInsertSceneComponent as CaptureAndInsertSceneComponentBase

from .clip_decoration import ClipDecoratedPropertiesCopier


class CaptureAndInsertSceneComponent(CaptureAndInsertSceneComponentBase):
    def __init__(self, name=None, decorator_factory=None, *a, **k):
        (super().__init__)(name, *a, **k)
        self._decorator_factory = decorator_factory

    def _copy_decorated_properties(self, source_clip, destination_clip):
        ClipDecoratedPropertiesCopier(
            source_clip=source_clip,
            destination_clip=destination_clip,
            decorator_factory=(self._decorator_factory),
        ).post_duplication_action()

    def post_trigger_action(self):
        view = self.song.view
        if liveobj_valid(view.detail_clip) and view.detail_clip.is_arrangement_clip:
            previous_detail_clip = view.detail_clip
            super().post_trigger_action()
            self._copy_decorated_properties(previous_detail_clip, view.detail_clip)
        else:

            def get_playing_clip(track):
                slot_ix = track.playing_slot_index
                if slot_ix > -1:
                    return track.clip_slots[slot_ix].clip
                return None

            played_clips = [get_playing_clip(track) for track in self.song.tracks]
            super().post_trigger_action()
            new_slots = view.selected_scene.clip_slots
            for ix, clip in enumerate(played_clips):
                if liveobj_valid(clip):
                    self._copy_decorated_properties(clip, new_slots[ix].clip)

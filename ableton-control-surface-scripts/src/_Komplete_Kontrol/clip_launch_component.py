# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Komplete_Kontrol/clip_launch_component.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1063 bytes
from ableton.v2.base import liveobj_valid
from ableton.v2.control_surface.component import Component
from ableton.v2.control_surface.control import ButtonControl


class ClipLaunchComponent(Component):
    clip_launch_button = ButtonControl()
    track_stop_button = ButtonControl()

    @clip_launch_button.pressed
    def clip_launch_button(self, _):
        song_view = self.song.view
        slot_or_scene = (
            song_view.selected_scene
            if self.song.view.selected_track == self.song.master_track
            else song_view.highlighted_clip_slot
        )
        if liveobj_valid(slot_or_scene):
            slot_or_scene.fire()

    @track_stop_button.pressed
    def track_stop_button(self, _):
        track = self.song.view.selected_track
        if track == self.song.master_track:
            self.song.stop_all_clips()
        else:
            if track in self.song.tracks:
                track.stop_all_clips()

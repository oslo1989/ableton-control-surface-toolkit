# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Komplete_Kontrol/selection_linked_session_ring_component.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 833 bytes
from ableton.v2.base import listens
from ableton.v2.control_surface.components import SessionRingComponent


class SelectionLinkedSessionRingComponent(SessionRingComponent):
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._SelectionLinkedSessionRingComponent__on_selected_track_changed.subject = self.song.view
        self._SelectionLinkedSessionRingComponent__on_selected_track_changed()

    @listens("selected_track")
    def __on_selected_track_changed(self):
        selected_track = self.song.view.selected_track
        if selected_track not in self.controlled_tracks():
            all_tracks = list(self.tracks_to_use())
            self.track_offset = all_tracks.index(selected_track)

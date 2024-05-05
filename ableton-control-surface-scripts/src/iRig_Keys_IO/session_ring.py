# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/iRig_Keys_IO/session_ring.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 943 bytes
from ableton.v2.base import listens
from ableton.v2.control_surface.components import SessionRingComponent


class SelectedTrackFollowingSessionRingComponent(SessionRingComponent):
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._SelectedTrackFollowingSessionRingComponent__on_selected_track_changed.subject = self.song.view
        self._SelectedTrackFollowingSessionRingComponent__on_selected_track_changed()

    @listens("selected_track")
    def __on_selected_track_changed(self):
        tracks_to_use = self.tracks_to_use()
        selected_track = self.song.view.selected_track
        if selected_track in tracks_to_use:
            track_index = list(tracks_to_use).index(selected_track)
            new_offset = track_index - track_index % self.num_tracks
            self.track_offset = new_offset

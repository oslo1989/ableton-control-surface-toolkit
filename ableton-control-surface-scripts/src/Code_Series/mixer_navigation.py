# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Code_Series/mixer_navigation.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1319 bytes
from ableton.v2.control_surface.components import SessionNavigationComponent, SessionRingScroller
from past.utils import old_div


class WrappingSessionRingTrackPager(SessionRingScroller):
    def can_scroll_up(self):
        return True

    def can_scroll_down(self):
        return True

    def do_scroll_up(self):
        width = self._session_ring.num_tracks
        track_offset = self._session_ring.track_offset
        new_track_offset = track_offset - width
        if new_track_offset < 0:
            new_track_offset = old_div(len(self._session_ring.tracks_to_use()) - 1, width) * width
        self._session_ring.set_offsets(new_track_offset, self._session_ring.scene_offset)

    def do_scroll_down(self):
        new_track_offset = self._session_ring.track_offset + self._session_ring.num_tracks
        if new_track_offset >= len(self._session_ring.tracks_to_use()):
            new_track_offset = 0
        self._session_ring.set_offsets(new_track_offset, self._session_ring.scene_offset)


class MixerNavigationComponent(SessionNavigationComponent):
    track_pager_type = WrappingSessionRingTrackPager

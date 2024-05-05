# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_mkII/channel_strip.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 893 bytes
from ableton.v2.base import liveobj_valid
from ableton.v2.control_surface.control import TextDisplayControl
from KeyLab_Essential.channel_strip import ChannelStripComponent as ChannelStripComponentBase


class ChannelStripComponent(ChannelStripComponentBase):
    track_name_display = TextDisplayControl(" ")

    def set_track_name_display(self, display):
        self.track_name_display.set_control_element(display)
        self._update_track_name_display()

    def set_track(self, track):
        super().set_track(track)
        self._update_track_name_display()

    def _update_track_name_display(self):
        track = self._track
        self.track_name_display[0] = track.name if liveobj_valid(track) else ""

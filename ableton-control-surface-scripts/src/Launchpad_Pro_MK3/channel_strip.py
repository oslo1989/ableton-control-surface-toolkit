# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_Pro_MK3/channel_strip.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 851 bytes
from ableton.v2.base import liveobj_valid
from novation.channel_strip import ChannelStripComponent as ChannelStripComponentBase


class ChannelStripComponent(ChannelStripComponentBase):
    def _track_color_changed(self):
        super()._track_color_changed()
        self._update_select_button()

    def _update_select_button(self):
        if liveobj_valid(self._track) or self.empty_color is None:
            if self.song.view.selected_track == self._track:
                self.select_button.color = self._track_color_value
            else:
                self.select_button.color = "Mixer.TrackNotSelected"
        else:
            self.select_button.color = self.empty_color

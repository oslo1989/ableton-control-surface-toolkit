# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_X/channel_strip.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1106 bytes
from ableton.v2.base import liveobj_valid
from novation.channel_strip import ChannelStripComponent as ChannelStripComponentBase


class ChannelStripComponent(ChannelStripComponentBase):
    def update(self):
        super().update()
        self._update_static_color_control()

    def _update_static_color_control(self):
        valid_track = liveobj_valid(self._track)
        color_value = self._static_color_value if valid_track else 0
        if valid_track:
            if self._send_controls:
                send_index = next((i for i, x in enumerate(self._send_controls) if x), None)
                if send_index is not None:
                    if send_index >= len(self._track.mixer_device.sends):
                        color_value = 0
        self.static_color_control.value = color_value

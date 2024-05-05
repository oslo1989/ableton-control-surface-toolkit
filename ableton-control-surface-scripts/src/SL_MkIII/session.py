# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/SL_MkIII/session.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1011 bytes
from ableton.v2.base import find_if
from ableton.v2.control_surface.components import SessionComponent as SessionComponentBase


class SessionComponent(SessionComponentBase):
    def _update_stop_clips_led(self, index):
        super()._update_stop_clips_led(index)
        self._update_stop_all_clips_button()

    def _update_stop_all_clips_button(self):
        button = self._stop_all_button
        if button:
            value_to_send = self._stop_clip_disabled_value
            tracks = self.song.tracks
            if find_if(lambda x: x.playing_slot_index >= 0 and x.fired_slot_index != -2, tracks):
                value_to_send = self._stop_clip_value
            else:
                if find_if(lambda x: x.fired_slot_index == -2, tracks):
                    value_to_send = self._stop_clip_triggered_value
            button.set_light(value_to_send)

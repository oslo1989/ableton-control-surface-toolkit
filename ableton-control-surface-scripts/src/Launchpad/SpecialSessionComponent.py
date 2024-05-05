# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad/SpecialSessionComponent.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1559 bytes
from _Framework import SessionComponent


class SpecialSessionComponent(SessionComponent):
    def _update_stop_clips_led(self, index):
        if self.is_enabled():
            if self._stop_track_clip_buttons is not None:
                if index < len(self._stop_track_clip_buttons):
                    button = self._stop_track_clip_buttons[index]
                    tracks_to_use = self.tracks_to_use()
                    track_index = index + self.track_offset()
                    if 0 <= track_index < len(tracks_to_use):
                        track = tracks_to_use[track_index]
                        if track.fired_slot_index == -2:
                            button.send_value(self._stop_clip_triggered_value)
                        else:
                            if track.playing_slot_index >= 0:
                                button.send_value(self._stop_clip_value)
                            else:
                                button.turn_off()
                    else:
                        button.send_value(4)

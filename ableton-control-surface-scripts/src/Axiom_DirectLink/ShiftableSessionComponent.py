# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Axiom_DirectLink/ShiftableSessionComponent.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 4395 bytes
from _Framework import SessionComponent


class ShiftableSessionComponent(SessionComponent):
    def __init__(self, num_tracks, num_scenes):
        self._shift_button = None
        self._clip_slot_buttons = None
        SessionComponent.__init__(self, num_tracks, num_scenes)

    def disconnect(self):
        SessionComponent.disconnect(self)
        if self._shift_button is not None:
            self._shift_button.remove_value_listener(self._shift_value)
            self._shift_button = None
        self._clip_slot_buttons = None

    def set_shift_button(self, shift_button):
        if self._shift_button is not None:
            self._shift_button.remove_value_listener(self._shift_value)
        self._shift_button = shift_button
        if self._shift_button is not None:
            self._shift_button.add_value_listener(self._shift_value)

    def set_clip_slot_buttons(self, buttons):
        self._clip_slot_buttons = buttons
        self._shift_value(0)

    def on_selected_track_changed(self):
        SessionComponent.on_selected_track_changed(self)
        selected_track = self.song().view.selected_track
        tracks = self.tracks_to_use()
        if selected_track in tracks:
            track_index = list(tracks).index(selected_track)
            new_offset = track_index - track_index % self._num_tracks
            self.set_offsets(new_offset, self.scene_offset())

    def _shift_value(self, value):
        for index in range(self._num_tracks):
            slot = self.selected_scene().clip_slot(index)
            if value != 0 or self._clip_slot_buttons is None:
                slot.set_launch_button(None)
            else:
                slot.set_launch_button(self._clip_slot_buttons[index])

    def _bank_right_value(self, value):
        if self.is_enabled():
            if not (value != 0 or self._bank_right_button.is_momentary()):
                self.set_offsets(self._track_offset + self._num_tracks, self.scene_offset())

    def _bank_left_value(self, value):
        if self.is_enabled():
            if not (value != 0 or self._bank_left_button.is_momentary()):
                self.set_offsets(max(0, self._track_offset - self._num_tracks), self.scene_offset())

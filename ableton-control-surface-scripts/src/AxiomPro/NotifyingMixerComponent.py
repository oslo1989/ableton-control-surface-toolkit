# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/AxiomPro/NotifyingMixerComponent.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 4638 bytes
from _Framework import MixerComponent


class NotifyingMixerComponent(MixerComponent):
    def __init__(self, num_tracks):
        self._update_callback = None
        MixerComponent.__init__(self, num_tracks)
        self._bank_display = None

    def disconnect(self):
        MixerComponent.disconnect(self)
        self._update_callback = None

    def set_update_callback(self, callback):
        self._update_callback = callback

    def set_bank_display(self, display):
        self._bank_display = display

    def on_selected_track_changed(self):
        MixerComponent.on_selected_track_changed(self)
        selected_track = self.song().view.selected_track
        num_strips = len(self._channel_strips)
        if selected_track in self._tracks_to_use():
            track_index = list(self._tracks_to_use()).index(selected_track)
            new_offset = track_index - track_index % num_strips
            self.set_track_offset(new_offset)

    def update(self):
        super().update()
        if self._update_callback is not None:
            self._update_callback()

    def _tracks_to_use(self):
        return tuple(self.song().visible_tracks) + tuple(self.song().return_tracks)

    def _reassign_tracks(self):
        MixerComponent._reassign_tracks(self)
        if self._update_callback is not None:
            self._update_callback()

    def _bank_up_value(self, value):
        old_offset = int(self._track_offset)
        MixerComponent._bank_up_value(self, value)
        if self._bank_display is not None:
            if value != 0 and old_offset != self._track_offset:
                min_track = self._track_offset + 1
                max_track = min(len(self._tracks_to_use()), min_track + len(self._channel_strips))
                self._bank_display.display_message("Tracks " + str(min_track) + " - " + str(max_track))
            else:
                self._bank_display.update()

    def _bank_down_value(self, value):
        old_offset = int(self._track_offset)
        MixerComponent._bank_down_value(self, value)
        if self._bank_display is not None:
            if value != 0 and old_offset != self._track_offset:
                min_track = self._track_offset + 1
                max_track = min(len(self._tracks_to_use()), min_track + len(self._channel_strips))
                self._bank_display.display_message("Tracks " + str(min_track) + " - " + str(max_track))
            else:
                self._bank_display.update()

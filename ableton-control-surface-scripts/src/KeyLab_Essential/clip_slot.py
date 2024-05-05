# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_Essential/clip_slot.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1817 bytes
from ableton.v2.base import liveobj_valid
from ableton.v2.control_surface.components import ClipSlotComponent as ClipSlotComponentBase


class ClipSlotComponent(ClipSlotComponentBase):
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._led = None

    def set_led(self, led):
        self._led = led

    def update(self):
        super().update()
        self._update_led()

    def _update_launch_button_color(self):
        self._update_led()

    def _update_led(self):
        if self.is_enabled():
            if self._led is not None:
                value_to_send = self._empty_slot_color
                if liveobj_valid(self._clip_slot):
                    track = self._clip_slot.canonical_parent
                    slot_or_clip = self._clip_slot.clip if self.has_clip() else self._clip_slot
                    value_to_send = self._led_feedback_value(track, slot_or_clip)
                self._led.set_light(value_to_send)

    def _led_feedback_value(self, track, slot_or_clip):
        if self.has_clip():
            if slot_or_clip.is_triggered:
                if slot_or_clip.will_record_on_start:
                    return self._triggered_to_record_color
                return self._triggered_to_play_color
            if slot_or_clip.is_playing:
                if slot_or_clip.is_recording:
                    return self._recording_color
                return self._started_value
            return self._stopped_value
        return self._empty_slot_color

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/novation/clip_actions.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 2301 bytes
from ableton.v2.base import duplicate_clip_loop
from ableton.v2.control_surface.components import ClipActionsComponent as ClipActionsComponentBase

from .blinking_button import BlinkingButtonControl


class ClipActionsComponent(ClipActionsComponentBase):
    quantize_button = BlinkingButtonControl(
        color="Action.Quantize",
        blink_on_color="Action.QuantizePressed",
        blink_off_color="Action.Quantize",
    )
    double_loop_button = BlinkingButtonControl(
        color="Action.Double",
        blink_on_color="Action.DoublePressed",
        blink_off_color="Action.Double",
    )
    __events__ = ("can_perform_clip_actions",)

    def __init__(self, quantization_component=None, *a, **k):
        (super().__init__)(*a, **k)
        self._quantization_component = quantization_component
        self.delete_button.color = "Action.Delete"
        self.delete_button.pressed_color = "Action.DeletePressed"
        self.duplicate_button.color = "Action.Duplicate"
        self.duplicate_button.pressed_color = "Action.DuplicatePressed"

    @quantize_button.pressed
    def quantize_button(self, _):
        if self._quantization_component:
            self._quantization_component.quantize_clip(self.clip_slot.clip)
            self.quantize_button.start_blinking()

    @double_loop_button.pressed
    def double_loop_button(self, _):
        duplicate_clip_loop(self.clip_slot.clip)
        self.double_loop_button.start_blinking()

    def delete_pitch(self, pitch):
        clip = self.clip_slot.clip
        loop_length = clip.loop_end - clip.loop_start
        clip.remove_notes_extended(from_time=(clip.loop_start), from_pitch=pitch, time_span=loop_length, pitch_span=1)

    def delete_clip(self):
        self.clip_slot.delete_clip()

    def _update_action_buttons(self):
        super()._update_action_buttons()
        can_perform_clip_action = self._can_perform_clip_action()
        self.quantize_button.enabled = can_perform_clip_action
        self.notify_can_perform_clip_actions(can_perform_clip_action)

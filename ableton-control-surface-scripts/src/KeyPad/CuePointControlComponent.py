# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyPad/CuePointControlComponent.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 2184 bytes
from _Framework import ControlSurfaceComponent
from _Framework.SubjectSlot import subject_slot


class CuePointControlComponent(ControlSurfaceComponent):
    _toggle_cue_button = None
    _prev_cue_button = None
    _next_cue_button = None

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._on_can_jump_to_prev_cue_changed.subject = self.song()
        self._on_can_jump_to_next_cue_changed.subject = self.song()

    def set_toggle_cue_button(self, button):
        self._toggle_cue_button = button
        self._on_toggle_cue.subject = button

    @subject_slot("value")
    def _on_toggle_cue(self, value):
        if not (value or self._toggle_cue_button.is_momentary()):
            self.song().set_or_delete_cue()

    def set_prev_cue_button(self, button):
        self._prev_cue_button = button
        self._on_jump_to_prev_cue.subject = button
        self._on_can_jump_to_prev_cue_changed()

    @subject_slot("can_jump_to_prev_cue")
    def _on_can_jump_to_prev_cue_changed(self):
        if self._prev_cue_button is not None:
            self._prev_cue_button.set_light(self.song().can_jump_to_prev_cue)

    @subject_slot("value")
    def _on_jump_to_prev_cue(self, value):
        if not (value or self._prev_cue_button.is_momentary()):
            if self.song().can_jump_to_prev_cue:
                self.song().jump_to_prev_cue()

    def set_next_cue_button(self, button):
        self._next_cue_button = button
        self._on_jump_to_next_cue.subject = button
        self._on_can_jump_to_next_cue_changed()

    @subject_slot("can_jump_to_next_cue")
    def _on_can_jump_to_next_cue_changed(self):
        if self._next_cue_button is not None:
            self._next_cue_button.set_light(self.song().can_jump_to_next_cue)

    @subject_slot("value")
    def _on_jump_to_next_cue(self, value):
        if not (value or self._next_cue_button.is_momentary()):
            if self.song().can_jump_to_next_cue:
                self.song().jump_to_next_cue()

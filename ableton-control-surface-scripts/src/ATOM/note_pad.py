# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ATOM/note_pad.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 590 bytes
from ableton.v3.control_surface.controls import PlayableControl


class NotePadMixin:
    def set_matrix(self, matrix):
        super().set_matrix(matrix)
        for button in self.matrix:
            button.set_mode(PlayableControl.Mode.playable_and_listenable)
            button.pressed_color = "NotePad.Pressed"

    def _on_matrix_pressed(self, _):
        pass

    def _on_matrix_released(self, button):
        self._update_button_color(button)

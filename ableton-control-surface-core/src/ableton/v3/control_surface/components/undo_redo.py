# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/components/undo_redo.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1331 bytes
from typing import cast

from .. import Component
from ..controls import ButtonControl
from ..display import Renderable


class UndoRedoComponent(Component, Renderable):
    undo_button = ButtonControl(color="UndoRedo.Undo", pressed_color="UndoRedo.UndoPressed")
    redo_button = ButtonControl(color="UndoRedo.Redo", pressed_color="UndoRedo.RedoPressed")

    def __init__(self, name="Undo_Redo", *a, **k):
        (super().__init__)(a, name=name, **k)

    @undo_button.pressed
    def undo_button(self, _):
        if self.song.can_undo:
            self.notify(self.notifications.UndoRedo.undo, cast(str, self.song.undo()))
        else:
            self.notify(self.notifications.UndoRedo.error_undo_no_action)

    @redo_button.pressed
    def redo_button(self, _):
        if self.song.can_redo:
            self.notify(self.notifications.UndoRedo.redo, cast(str, self.song.redo()))
        else:
            self.notify(self.notifications.UndoRedo.error_redo_no_action)

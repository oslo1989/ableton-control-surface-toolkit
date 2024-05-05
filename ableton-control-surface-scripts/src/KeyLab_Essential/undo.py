# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_Essential/undo.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1159 bytes
from functools import partial

from ableton.v2.base import task
from ableton.v2.control_surface import Component
from ableton.v2.control_surface.control import ButtonControl


class UndoComponent(Component):
    undo_button = ButtonControl(color="DefaultButton.Off")

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._light_undo_button_task = self._tasks.add(
            task.sequence(
                task.run(partial(self._set_undo_button_light, "DefaultButton.On")),
                task.wait(1.0),
                task.run(partial(self._set_undo_button_light, "DefaultButton.Off")),
            ),
        )
        self._light_undo_button_task.kill()

    @undo_button.pressed
    def undo_button(self, _):
        if self.song.can_undo:
            self.song.undo()
            if not self._light_undo_button_task.is_running:
                self._light_undo_button_task.restart()

    def _set_undo_button_light(self, value):
        self.undo_button.color = value

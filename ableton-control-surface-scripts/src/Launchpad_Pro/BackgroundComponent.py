# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_Pro/BackgroundComponent.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1679 bytes
import contextlib

from _Framework.BackgroundComponent import BackgroundComponent as BackgroundComponentBase
from _Framework.SubjectSlot import SubjectSlotError


class BackgroundComponent(BackgroundComponentBase):
    def _clear_control(self, name, control):
        if control:
            super()._clear_control(name, control)
        else:
            slot = self._control_slots.get(name, None)
            if slot:
                del self._control_slots[name]
                self.disconnect_disconnectable(slot)
            if name in self._control_map:
                del self._control_map[name]


class ModifierBackgroundComponent(BackgroundComponentBase):
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)

    def _clear_control(self, name, control):
        super()._clear_control(name, control)
        if control:
            with contextlib.suppress(SubjectSlotError):
                self._control_slots[name] = self.register_slot(
                    control,
                    lambda *a, **k: (self._on_value_listener)(control, *a, **k),
                    "value",
                )

    def _reset_control(self, control):
        if len(control.resource.owners) > 1:
            control.set_light(control.is_pressed())
        else:
            control.reset()

    def _on_value_listener(self, sender, value, *a, **k):
        if len(sender.resource.owners) > 1:
            sender.set_light(sender.is_pressed())

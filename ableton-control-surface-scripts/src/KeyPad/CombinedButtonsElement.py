# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyPad/CombinedButtonsElement.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1348 bytes
from _Framework import ButtonMatrixElement
from _Framework.ButtonElement import OFF_VALUE
from _Framework.Util import BooleanContext, const


class CombinedButtonsElement(ButtonMatrixElement):
    def __init__(self, buttons=None, *a, **k):
        (super().__init__)(a, rows=[buttons], **k)
        self._is_pressed = BooleanContext(False)

    def is_momentary(self):
        return True

    def is_pressed(self):
        return any(b__[0].is_pressed() if b__[0] is not None else False for b__ in self.iterbuttons()) or bool(
            self._is_pressed,
        )

    def on_nested_control_element_value(self, value, sender):
        with self._is_pressed():
            self.notify_value(value)
        if value != OFF_VALUE:
            if not getattr(sender, "is_momentary", const(False))():
                self.notify_value(OFF_VALUE)

    def send_value(self, value):
        for button, _ in self.iterbuttons():
            if button:
                button.send_value(value)

    def set_light(self, value):
        for button, _ in self.iterbuttons():
            if button:
                button.set_light(value)

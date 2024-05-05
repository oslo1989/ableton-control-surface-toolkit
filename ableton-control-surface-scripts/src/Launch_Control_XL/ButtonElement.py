# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launch_Control_XL/ButtonElement.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 943 bytes
from _Framework.ButtonElement import OFF_VALUE, ON_VALUE
from _Framework.ButtonElement import ButtonElement as ButtonElementBase


class ButtonElement(ButtonElementBase):
    _on_value = None
    _off_value = None

    def reset(self):
        self._on_value = None
        self._off_value = None
        super().reset()

    def set_on_off_values(self, on_value, off_value):
        self._on_value = on_value
        self._off_value = off_value

    def send_value(self, value, **k):
        if value is ON_VALUE and self._on_value is not None:
            self._skin[self._on_value].draw(self)
        else:
            if value is OFF_VALUE and self._off_value is not None:
                self._skin[self._off_value].draw(self)
            else:
                (super().send_value)(value, **k)

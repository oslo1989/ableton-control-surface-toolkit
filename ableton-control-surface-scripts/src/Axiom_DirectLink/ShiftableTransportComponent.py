# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Axiom_DirectLink/ShiftableTransportComponent.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 2942 bytes
from _Framework import TransportComponent


class ShiftableTransportComponent(TransportComponent):
    def __init__(self):
        self._shift_button = None
        self._shift_pressed = False
        TransportComponent.__init__(self)

    def disconnect(self):
        if self._shift_button is not None:
            self._shift_button.remove_value_listener(self._shift_value)
            self._shift_button = None
        TransportComponent.disconnect(self)

    def set_shift_button(self, button):
        if self._shift_button != button:
            if self._shift_button is not None:
                self._shift_button.remove_value_listener(self._shift_value)
                self._shift_pressed = False
            self._shift_button = button
            if self._shift_button is not None:
                self._shift_button.add_value_listener(self._shift_value)

    def _shift_value(self, value):
        if self.is_enabled():
            self._shift_pressed = value > 0

    def _ffwd_value(self, value):
        if self._shift_pressed:
            self.song().current_song_time = self.song().last_event_time
        else:
            TransportComponent._ffwd_value(self, value)

    def _rwd_value(self, value):
        if self._shift_pressed:
            self.song().current_song_time = 0.0
        else:
            TransportComponent._rwd_value(self, value)

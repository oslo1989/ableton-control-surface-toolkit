# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Framework/ButtonElement.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 3778 bytes
import Live

from .InputControlElement import InputControlElement
from .Skin import Skin, SkinColorMissingError
from .Util import nop


class ButtonValue:
    midi_value = 0

    def __init__(self, midi_value=None, *a, **k):
        (super().__init__)(*a, **k)
        if midi_value is not None:
            self.midi_value = midi_value

    def __int__(self):
        return self.midi_value

    def __eq__(self, other):
        try:
            return id(self) == id(other) or self.midi_value == other
        except NotImplementedError:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __bool__(self):
        return self != OFF_VALUE


ON_VALUE = ButtonValue(127)
OFF_VALUE = ButtonValue(0)


class Color(ButtonValue):
    def draw(self, interface):
        interface.send_value(self.midi_value)


class DummyUndoStepHandler:
    def begin_undo_step(self):
        pass

    def end_undo_step(self):
        pass


class ButtonElementMixin:
    def set_light(self, is_turned_on):
        if is_turned_on:
            self.turn_on()
        else:
            self.turn_off()

    def turn_on(self):
        self.send_value(ON_VALUE)

    def turn_off(self):
        self.send_value(OFF_VALUE)


class ButtonElement(InputControlElement, ButtonElementMixin):
    class ProxiedInterface(InputControlElement.ProxiedInterface, ButtonElementMixin):
        is_momentary = nop
        is_pressed = nop

    def __init__(
        self,
        is_momentary,
        msg_type,
        channel,
        identifier,
        skin=Skin(),
        undo_step_handler=DummyUndoStepHandler(),
        *a,
        **k,
    ):
        (super().__init__)(msg_type, channel, identifier, *a, **k)
        self._ButtonElement__is_momentary = bool(is_momentary)
        self._last_received_value = -1
        self._undo_step_handler = undo_step_handler
        self._skin = skin

    def is_momentary(self):
        return self._ButtonElement__is_momentary

    def message_map_mode(self):
        return Live.MidiMap.MapMode.absolute

    def is_pressed(self):
        return self._ButtonElement__is_momentary and int(self._last_received_value) > 0

    def set_light(self, value):
        self._set_skin_light(value)

    def _set_skin_light(self, value):
        try:
            color = self._skin[value]
            color.draw(self)
        except SkinColorMissingError:
            super().set_light(value)

    def receive_value(self, value):
        pressed_before = self.is_pressed()
        self._last_received_value = value
        if not pressed_before:
            if self.is_pressed():
                self._undo_step_handler.begin_undo_step()
        super().receive_value(value)
        if pressed_before:
            if not self.is_pressed():
                self._undo_step_handler.end_undo_step()

    def disconnect(self):
        super().disconnect()
        self._undo_step_handler = None

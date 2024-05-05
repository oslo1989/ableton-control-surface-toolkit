# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad/PreciseButtonSliderElement.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 7493 bytes
from past.utils import old_div

from _Framework import ButtonSliderElement
from _Framework.InputControlElement import *

SLIDER_MODE_SINGLE = 0
SLIDER_MODE_VOLUME = 1
SLIDER_MODE_PAN = 2


class PreciseButtonSliderElement(ButtonSliderElement):
    def __init__(self, buttons):
        ButtonSliderElement.__init__(self, buttons)
        num_buttons = len(buttons)
        self._disabled = False
        self._mode = SLIDER_MODE_VOLUME
        self._value_map = tuple([float(old_div(index, num_buttons)) for index in range(num_buttons)])

    def set_disabled(self, disabled):
        self._disabled = disabled

    def set_mode(self, mode):
        if mode != self._mode:
            self._mode = mode

    def set_value_map(self, map):
        self._value_map = map

    def send_value(self, value):
        if not self._disabled:
            if value != self._last_sent_value:
                if self._mode == SLIDER_MODE_SINGLE:
                    ButtonSliderElement.send_value(self, value)
                else:
                    if self._mode == SLIDER_MODE_VOLUME:
                        self._send_value_volume(value)
                    else:
                        if self._mode == SLIDER_MODE_PAN:
                            self._send_value_pan(value)
                        else:
                            pass
                self._last_sent_value = value

    def connect_to(self, parameter):
        ButtonSliderElement.connect_to(self, parameter)
        if self._parameter_to_map_to is not None:
            self._last_sent_value = -1
            self._on_parameter_changed()

    def release_parameter(self):
        old_param = self._parameter_to_map_to
        ButtonSliderElement.release_parameter(self)
        if not self._disabled:
            if old_param is not None:
                for button in self._buttons:
                    button.reset()

    def reset(self):
        if not self._disabled:
            if self._buttons is not None:
                for button in self._buttons:
                    if button is not None:
                        button.reset()

    def _send_value_volume(self, value):
        index_to_light = -1
        normalised_value = old_div(float(value), 127.0)
        if normalised_value > 0.0:
            for index in range(len(self._value_map)):
                if normalised_value <= self._value_map[index]:
                    index_to_light = index
                    break

        self._send_mask(tuple([index <= index_to_light for index in range(len(self._buttons))]))

    def _send_value_pan(self, value):
        num_buttons = len(self._buttons)
        button_bits = [False for index in range(num_buttons)]
        normalised_value = float(2 * old_div(value, 127.0)) - 1.0
        if value in (63, 64):
            normalised_value = 0.0
        if normalised_value < 0.0:
            for index in range(len(self._buttons)):
                button_bits[index] = self._value_map[index] >= normalised_value
                if self._value_map[index] >= 0:
                    break

        else:
            if normalised_value > 0.0:
                for index in range(len(self._buttons)):
                    r_index = len(self._buttons) - 1 - index
                    button_bits[r_index] = self._value_map[r_index] <= normalised_value
                    if self._value_map[r_index] <= 0:
                        break

            else:
                for index in range(len(self._buttons)):
                    button_bits[index] = self._value_map[index] == normalised_value

        self._send_mask(tuple(button_bits))

    def _send_mask(self, mask):
        for index in range(len(self._buttons)):
            if mask[index]:
                self._buttons[index].turn_on()
            else:
                self._buttons[index].turn_off()

    def _button_value(self, value, sender):
        self._last_sent_value = -1
        if not (value != 0 or sender.is_momentary()):
            index_of_sender = list(self._buttons).index(sender)
            if self._parameter_to_map_to is not None:
                if self._parameter_to_map_to.is_enabled:
                    self._parameter_to_map_to.value = self._value_map[index_of_sender]
            self.notify_value(value)

    def _on_parameter_changed(self):
        param_range = abs(self._parameter_to_map_to.max - self._parameter_to_map_to.min)
        param_value = self._parameter_to_map_to.value
        param_min = self._parameter_to_map_to.min
        param_mid = old_div(param_range, 2) + param_min
        midi_value = 0
        if self._mode == SLIDER_MODE_PAN:
            if param_value == param_mid:
                midi_value = 64
            else:
                diff = old_div(abs(param_value - param_mid), param_range) * 127
                midi_value = 64 + int(diff) if param_value > param_mid else 63 - int(diff)
        else:
            midi_value = int(old_div(127 * abs(param_value - self._parameter_to_map_to.min), param_range))
        self.send_value(midi_value)

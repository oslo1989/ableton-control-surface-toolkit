# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/APC40_MkII/TransportComponent.py
# Compiled at: 2023-11-21 10:21:17
# Size of source mod 2**32: 1500 bytes
from _Framework.Control import ButtonControl
from _Framework.SubjectSlot import subject_slot
from _Framework.TransportComponent import TransportComponent as TransportComponentBase
from _Framework.Util import clamp


class TransportComponent(TransportComponentBase):
    shift_button = ButtonControl()

    def __init__(self, *a, **k):
        def play_toggle_model_transform(val):
            if self.shift_button.is_pressed:
                return False
            return val

        k["play_toggle_model_transform"] = play_toggle_model_transform
        (super().__init__)(*a, **k)
        self._tempo_encoder_control = None

    def set_tempo_encoder(self, control):
        if control != self._tempo_encoder_control:
            self._tempo_encoder_control = control
            self._tempo_encoder_value.subject = control
            self.update()

    @subject_slot("value")
    def _tempo_encoder_value(self, value):
        if self.is_enabled():
            step = 0.1 if self.shift_button.is_pressed else 1.0
            amount = value - 128 if value >= 64 else value
            self.song().tempo = clamp(self.song().tempo + amount * step, 20, 999)

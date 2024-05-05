# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/MiniLab_3/encoder.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 3169 bytes
from ableton.v3.control_surface.elements import EncoderElement as EncoderElementBase
from ableton.v3.live import liveobj_valid, parameter_value_to_midi_value

from .display_util import make_blank_parameter_message, make_parameter_message
from .midi import ENCODER_ID_TO_SYSEX_ID, ENCODER_VALUE_HEADER, SYSEX_END


class RealigningEncoderMixin:
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._sysex_header = self._get_sysex_header()
        self._last_mapped_value = None

    def realign_value(self):
        if self._sysex_header:
            value_to_send = self._last_mapped_value or self._last_received_value or 0
            self.send_midi((*self._sysex_header, value_to_send, SYSEX_END))

    def receive_value(self, value):
        super().receive_value(value)
        self._last_mapped_value = None

    def _parameter_value_changed(self):
        if liveobj_valid(self.mapped_object):
            self._last_mapped_value = parameter_value_to_midi_value(self.mapped_object)


class EncoderElement(EncoderElementBase):
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._last_sent_parameter_message = None

    def notify_parameter_name(self):
        super().notify_parameter_name()
        self._send_parameter_feedback()

    def notify_parameter_value(self):
        super().notify_parameter_value()
        self._send_parameter_feedback()

    def clear_send_cache(self):
        super().clear_send_cache()
        self._last_sent_parameter_message = None

    def _send_parameter_feedback(self):
        ident = self.message_identifier()
        if liveobj_valid(self.mapped_object):
            self._send_message(make_parameter_message(ident, self.parameter_name, self.parameter_value))
        else:
            self._send_message(make_blank_parameter_message(ident))

    def _send_message(self, message):
        if message != self._last_sent_parameter_message:
            self.send_midi(message)
        self._last_sent_parameter_message = message


class RealigningEncoderElement(RealigningEncoderMixin, EncoderElement):
    def _get_sysex_header(self):
        return (*ENCODER_VALUE_HEADER, ENCODER_ID_TO_SYSEX_ID[self.message_identifier()], 0)

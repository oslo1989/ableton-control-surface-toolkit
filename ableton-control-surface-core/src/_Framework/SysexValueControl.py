# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Framework/SysexValueControl.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1115 bytes
from .InputControlElement import MIDI_SYSEX_TYPE, InputControlElement


class SysexValueControl(InputControlElement):
    def __init__(self, message_prefix=None, value_enquiry=None, default_value=None, *a, **k):
        (super().__init__)(a, msg_type=MIDI_SYSEX_TYPE, sysex_identifier=message_prefix, **k)
        self._value_enquiry = value_enquiry
        self._default_value = default_value

    def send_value(self, value_bytes):
        self.send_midi(self.message_sysex_identifier() + value_bytes + (247,))

    def enquire_value(self):
        self.send_midi(self._value_enquiry)

    def reset(self):
        if self._default_value is not None:
            self.send_value(self._default_value)

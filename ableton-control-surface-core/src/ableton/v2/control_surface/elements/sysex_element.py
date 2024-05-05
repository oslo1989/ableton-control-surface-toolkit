# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/elements/sysex_element.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 3025 bytes
from base.dependency import depends

from ableton.v2.base import old_hasattr

from ..input_control_element import MIDI_SYSEX_TYPE, InputControlElement


class SysexElement(InputControlElement):
    def __init__(self, send_message_generator=None, enquire_message=None, default_value=None, optimized=False, *a, **k):
        (super().__init__)(a, msg_type=MIDI_SYSEX_TYPE, **k)
        self._send_message_generator = send_message_generator
        self._enquire_message = enquire_message
        self._default_value = default_value
        self._optimized = optimized

    def message_map_mode(self):
        raise AssertionError("SysexElement doesn't support mapping.")

    def send_value(self, *arguments):
        message = (self._send_message_generator)(*arguments)
        self._do_send_value(message)

    def enquire_value(self):
        self.send_midi(self._enquire_message)

    def reset(self):
        if self._default_value is not None:
            self.send_value(self._default_value)

    def _do_send_value(self, message):
        if self._optimized:
            if message == self._last_sent_message or self.send_midi(message):
                self._last_sent_message = message
        else:
            self.send_midi(message)

    @property
    def _last_sent_value(self):
        if self._last_sent_message:
            return self._last_sent_message
        return -1


class ColorSysexElement(SysexElement):
    @depends(skin=None)
    def __init__(self, skin=None, *a, **k):
        (super().__init__)(*a, **k)
        self._skin = skin

    def set_light(self, value):
        color = None
        color = value if old_hasattr(value, "draw") else self._skin[value]
        color.draw(self)

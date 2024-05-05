# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_MK3/simple_display.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 2615 bytes
from functools import partial

from ableton.v2.base import task
from ableton.v2.control_surface import NotifyingControlElement
from ableton.v3.base import as_ascii, get_default_ascii_translations

NON_ASCII_ENCODING = 17
TRANSLATED_DEGREE_SYMBOL = 48
ascii_translations = get_default_ascii_translations()
ascii_translations["°"] = (NON_ASCII_ENCODING, TRANSLATED_DEGREE_SYMBOL)
as_ascii = partial(as_ascii, ascii_translations=ascii_translations)


class SimpleDisplayElement(NotifyingControlElement):
    def __init__(self, command, tail, *a, **k):
        (super().__init__)(*a, **k)
        self._message_command = command
        self._message_header = None
        self._message_tail = tail
        self._message_to_send = None
        self._last_sent_message = None
        self._send_message_task = self._tasks.add(task.run(self._send_message))
        self._send_message_task.kill()
        self._initialized = False

    def initialize(self, header):
        self._message_header = header + self._message_command
        self._initialized = True
        self._request_send_message()

    def display_message(self, message):
        if message:
            self._message_to_send = tuple(as_ascii(message)) + self._message_tail
            self._request_send_message()

    def update(self):
        self._last_sent_message = None
        self._request_send_message()

    def clear_send_cache(self):
        self._last_sent_message = None
        self._request_send_message()

    def reset(self):
        self.display_message(" ")

    def send_midi(self, message):
        if message != self._last_sent_message:
            NotifyingControlElement.send_midi(self, message)
            self._last_sent_message = message

    def _request_send_message(self):
        if self._initialized:
            self._send_message_task.restart()

    def _send_message(self):
        if self._message_to_send:
            self.send_midi(self._message_header + self._message_to_send)

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/FANTOM/simple_display.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1658 bytes
from ableton.v3.base import as_ascii, task
from ableton.v3.control_surface import NotifyingControlElement
from ableton.v3.control_surface.elements import adjust_string


class SimpleDisplayElement(NotifyingControlElement):
    def __init__(self, header, tail, max_chars=6, *a, **k):
        (super().__init__)(*a, **k)
        self._max_chars = max_chars
        self._message_header = header
        self._message_tail = tail
        self._message_to_send = None
        self._last_sent_message = None
        self._send_message_task = self._tasks.add(task.run(self._send_message))
        self._send_message_task.kill()

    def display_data(self, data):
        self._message_to_send = (
            self._message_header + tuple(as_ascii(adjust_string(data, self._max_chars).strip())) + self._message_tail
        )
        self._request_send_message()

    def update(self):
        self._last_sent_message = None
        self._request_send_message()

    def clear_send_cache(self):
        self._last_sent_message = None
        self._request_send_message()

    def reset(self):
        self.display_data("")

    def send_midi(self, message):
        if message != self._last_sent_message:
            NotifyingControlElement.send_midi(self, message)
            self._last_sent_message = message

    def _request_send_message(self):
        self._send_message_task.restart()

    def _send_message(self):
        if self._message_to_send:
            self.send_midi(self._message_to_send)

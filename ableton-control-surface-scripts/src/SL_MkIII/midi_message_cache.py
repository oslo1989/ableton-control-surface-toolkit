# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/SL_MkIII/midi_message_cache.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 725 bytes
from .sysex import NUM_SET_PROPERTY_HEADER_BYTES


class MidiMessageCache:
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._messages = []

    def __call__(self, message):
        self._messages = list(
            filter(
                lambda m: m[:NUM_SET_PROPERTY_HEADER_BYTES] != message[:NUM_SET_PROPERTY_HEADER_BYTES],
                self._messages,
            ),
        )
        self._messages.append(message)

    @property
    def messages(self):
        return self._messages

    def clear(self):
        self._messages = []

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/SL_MkIII/message.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 533 bytes
from ableton.v2.control_surface import Component

from .control import TextDisplayControl

NUM_MESSAGE_SEGMENTS = 2


class MessageComponent(Component):
    display = TextDisplayControl(segments=(("",) * NUM_MESSAGE_SEGMENTS))

    def __call__(self, *messages):
        for index, message in zip(range(NUM_MESSAGE_SEGMENTS), messages):
            self.display[index] = message if message else ""

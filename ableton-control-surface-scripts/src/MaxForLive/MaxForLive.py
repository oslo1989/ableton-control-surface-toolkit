# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/MaxForLive/MaxForLive.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 2246 bytes
from ableton.v2.control_surface import SimpleControlSurface
from ableton.v2.control_surface.input_control_element import MIDI_CC_TYPE, MIDI_NOTE_TYPE, MIDI_PB_TYPE

STATUS_TO_TYPE = {144: MIDI_NOTE_TYPE, 176: MIDI_CC_TYPE, 224: MIDI_PB_TYPE}


class MaxForLive(SimpleControlSurface):
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._registered_control_names = []
        self._registered_messages = []

    def register_midi_control():
        pass

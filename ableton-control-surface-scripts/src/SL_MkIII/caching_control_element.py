# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/SL_MkIII/caching_control_element.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 628 bytes
from ableton.v2.base import depends
from ableton.v2.control_surface import ControlElement

from .sysex import SET_PROPERTY_MSG_HEADER


class CachingControlElement(ControlElement):
    @depends(message_cache=None)
    def __init__(self, message_cache=None, *a, **k):
        (super().__init__)(*a, **k)
        self._message_cache = message_cache

    def send_midi(self, message, **_):
        self._message_cache(message[len(SET_PROPERTY_MSG_HEADER) : -1])

    def reset(self):
        pass

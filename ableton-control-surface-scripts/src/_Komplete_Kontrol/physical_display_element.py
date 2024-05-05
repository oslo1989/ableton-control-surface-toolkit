# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Komplete_Kontrol/physical_display_element.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 647 bytes
from itertools import chain

from ableton.v2.control_surface.elements import PhysicalDisplayElement as PhysicalDisplayElementBase


class PhysicalDisplayElement(PhysicalDisplayElementBase):
    def _build_display_message(self, display):
        return chain(*(self._translate_string(str(x).strip()) for x in display._logical_segments))

    def _request_send_message(self):
        self._send_message()

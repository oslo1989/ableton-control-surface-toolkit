# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ATOM/drum_group.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 966 bytes
from ableton.v3.control_surface.components import DrumGroupComponent as DrumGroupComponentBase

from .note_pad import NotePadMixin

COMPLETE_QUADRANTS_RANGE = range(4, 116)
MAX_QUADRANT_INDEX = 7
NUM_PADS = 16
PADS_PER_ROW = 4


class DrumGroupComponent(NotePadMixin, DrumGroupComponentBase):
    @staticmethod
    def _filled_color(pad):
        pad_quadrant = MAX_QUADRANT_INDEX
        if pad.note in COMPLETE_QUADRANTS_RANGE:
            pad_quadrant = (pad.note - PADS_PER_ROW) // NUM_PADS
        return f"DrumGroup.PadQuadrant{pad_quadrant}"

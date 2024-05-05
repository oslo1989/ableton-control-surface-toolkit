# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Blackstar_Live_Logic/midi.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 455 bytes
from ableton.v2.control_surface.midi import SYSEX_START

SYSEX_HEADER = (SYSEX_START, 0, 32, 114)
NUMERIC_DISPLAY_COMMAND = (0,)
LIVE_INTEGRATION_MODE_ID = (SYSEX_START, 0, 0, 116, 1, 0, 77, 67, 1, 0, 7, 1, 0)

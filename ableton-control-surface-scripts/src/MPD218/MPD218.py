# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/MPD218/MPD218.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 417 bytes
from _MPDMkIIBase import MPDMkIIBase

PAD_CHANNEL = 9
PAD_IDS = [[48, 49, 50, 51], [44, 45, 46, 47], [40, 41, 42, 43], [36, 37, 38, 39]]


class MPD218(MPDMkIIBase):
    def __init__(self, *a, **k):
        (super().__init__)(PAD_IDS, PAD_CHANNEL, *a, **k)

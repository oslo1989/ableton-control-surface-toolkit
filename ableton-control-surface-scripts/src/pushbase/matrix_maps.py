# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/pushbase/matrix_maps.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1498 bytes
PAD_TRANSLATIONS = (
    (0, 0, 60, 13),
    (1, 0, 61, 13),
    (2, 0, 62, 13),
    (3, 0, 63, 13),
    (0, 1, 52, 13),
    (1, 1, 53, 13),
    (2, 1, 54, 13),
    (3, 1, 55, 13),
    (0, 2, 44, 13),
    (1, 2, 45, 13),
    (2, 2, 46, 13),
    (3, 2, 47, 13),
    (0, 3, 36, 13),
    (1, 3, 37, 13),
    (2, 3, 38, 13),
    (3, 3, 39, 13),
)
NON_FEEDBACK_CHANNEL = 0
FEEDBACK_CHANNELS = list(range(9, 16))
PAD_FEEDBACK_CHANNEL = FEEDBACK_CHANNELS[-1]
PLAYHEAD_FEEDBACK_CHANNELS = list(range(1, 9))

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Oxygen_5th_Gen/oxygen_5th_gen.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 754 bytes
from Oxygen_Pro.oxygen_pro import Oxygen_Pro

LIVE_MODE_BYTE = 0


class Oxygen_5th_Gen(Oxygen_Pro):
    live_mode_byte = LIVE_MODE_BYTE
    has_session_component = False

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self.set_pad_translations(
            tuple([(col, row, 36 + (3 - row) * 4 + col, 0) for row in range(3, -1, -1) for col in iter(range(4))]),
        )

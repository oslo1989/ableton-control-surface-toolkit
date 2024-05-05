# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/MiniLab_3/sysex.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1329 bytes
from ableton.v3.control_surface.elements import SysexElement as SysexElementBase

from .midi import COMMAND_ID_TO_DAW_PROGRAM_ID


class SysexElement(SysexElementBase):
    def receive_value(self, value):
        if len(value) == 2:
            if value[0] in COMMAND_ID_TO_DAW_PROGRAM_ID:
                super().receive_value(int(value[1] == COMMAND_ID_TO_DAW_PROGRAM_ID[value[0]]))

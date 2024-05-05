# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/simple_mode_switcher.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 753 bytes
from ableton.v2.base import const
from pushbase.note_layout_switcher import ModeSwitcherBase


class SimpleModeSwitcher(ModeSwitcherBase):
    def __init__(self, session_modes=None, *a, **k):
        (super().__init__)(*a, **k)
        self._session_modes = session_modes
        self._cycle_mode = session_modes.cycle_mode
        self._get_current_alternative_mode = const(session_modes)

    def _unlock_alternative_mode(self, locked_mode):
        super()._unlock_alternative_mode(locked_mode)
        self.locked_mode = None

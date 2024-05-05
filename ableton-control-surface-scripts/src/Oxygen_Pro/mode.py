# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Oxygen_Pro/mode.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 655 bytes
from ableton.v2.control_surface.mode import ImmediateBehaviour


class ReenterBehaviour(ImmediateBehaviour):
    def __init__(self, on_reenter=None, *a, **k):
        (super().__init__)(*a, **k)
        self.on_reenter = on_reenter

    def press_immediate(self, component, mode):
        was_active = component.selected_mode == mode
        super().press_immediate(component, mode)
        if was_active:
            self.on_reenter()

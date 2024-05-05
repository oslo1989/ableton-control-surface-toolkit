# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/elements/lockable_combo.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 610 bytes
from ableton.v2.control_surface.elements import ComboElement


class LockableComboElement(ComboElement):
    def _modifier_is_valid(self, mod):
        return self.owns_control_element(mod) and (mod.is_pressed) or ((hasattr(mod, "is_locked")) and (mod.is_locked))

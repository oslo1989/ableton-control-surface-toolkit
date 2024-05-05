# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/APC20/BackgroundComponent.py
# Compiled at: 2023-11-21 10:21:17
# Size of source mod 2**32: 595 bytes
from _Framework.BackgroundComponent import BackgroundComponent as BackgroundComponentBase
from _Framework.Util import nop


class BackgroundComponent(BackgroundComponentBase):
    def _clear_control(self, name, control):
        if control:
            control.add_value_listener(nop)
        else:
            if name in self._control_map:
                self._control_map[name].remove_value_listener(nop)
        super()._clear_control(name, control)

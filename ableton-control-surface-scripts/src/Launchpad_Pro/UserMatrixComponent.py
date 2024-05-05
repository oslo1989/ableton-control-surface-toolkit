# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_Pro/UserMatrixComponent.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 716 bytes
from _Framework import ControlSurfaceComponent


def _disable_control(control):
    for button in control:
        button.set_enabled(False)


class UserMatrixComponent(ControlSurfaceComponent):
    def __getattr__(self, name):
        if len(name) > 4:
            if name[:4] == "set_":
                return _disable_control
        raise AttributeError(name)

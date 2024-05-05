# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Akai_Force_MPC/background.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 455 bytes
from ableton.v2.control_surface.components import BackgroundComponent


class LightingBackgroundComponent(BackgroundComponent):
    def _clear_control(self, name, control):
        super()._clear_control(name, control)
        if control:
            control.set_light("Background.On")

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_Mini_MK3/notifying_background.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 812 bytes
from functools import partial

from ableton.v2.base import nop
from ableton.v2.control_surface.components import BackgroundComponent
from ableton.v2.control_surface.elements import ButtonMatrixElement


class NotifyingBackgroundComponent(BackgroundComponent):
    __events__ = ("value",)

    def register_slot(self, control, *a):
        listener = (
            nop
            if isinstance(control, ButtonMatrixElement)
            else partial(self._NotifyingBackgroundComponent__on_control_value, control)
        )
        return super(BackgroundComponent, self).register_slot(control, listener, "value")

    def __on_control_value(self, control, value):
        self.notify_value(control, value)

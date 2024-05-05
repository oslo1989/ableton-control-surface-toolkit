# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/drumcell.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 909 bytes
from enum import IntEnum

from ableton.v2.base import EventObject
from ableton.v2.control_surface import LiveObjectDecorator


class DrumCellDeviceDecorator(LiveObjectDecorator, EventObject):
    class select(IntEnum):
        env = 0
        flt = 1
        mod = 2
        sam = 3

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._add_enum_parameter(
            name="Select",
            values=["Env", "Filter", "Mod", "Sample"],
            default_value=(self.select.env),
        )
        self._add_switch_option(name="Env Mode", pname="Env Mode", labels=["Trigger", "Gate"])
        self._add_on_off_option(name="Filter", pname="Filter On")
        self.register_disconnectables(self.options)

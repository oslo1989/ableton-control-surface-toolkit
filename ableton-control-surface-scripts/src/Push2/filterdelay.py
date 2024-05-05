# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/filterdelay.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1389 bytes
from enum import IntEnum

from ableton.v2.base import EventObject
from ableton.v2.control_surface import LiveObjectDecorator


class FilterDelayDeviceDecorator(LiveObjectDecorator, EventObject):
    class ChanSelect(IntEnum):
        l = 0
        lr = 1
        r = 2
        dry = 3

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._add_enum_parameter(name="Chan Select", values=["L", "L+R", "R", "Dry"], default_value=(self.ChanSelect.l))
        self._add_on_off_option(name="L Sync", pname="1 Delay Mode")
        self._add_on_off_option(name="L+R Sync", pname="2 Delay Mode")
        self._add_on_off_option(name="R Sync", pname="3 Delay Mode")
        self._add_on_off_option(name="L Channel", pname="1 Input On")
        self._add_on_off_option(name="L+R Channel", pname="2 Input On")
        self._add_on_off_option(name="R Channel", pname="3 Input On")
        self._add_on_off_option(name="L Filter", pname="1 Filter On")
        self._add_on_off_option(name="L+R Filter", pname="2 Filter On")
        self._add_on_off_option(name="R Filter", pname="3 Filter On")
        self.register_disconnectables(self.options)

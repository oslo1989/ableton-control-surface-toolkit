# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/elements/velocity_levels_element.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 857 bytes
from ...base import EventObject, listenable_property
from .proxy_element import ProxyElement


class NullVelocityLevels(EventObject):
    enabled = False
    target_note = -1
    target_channel = -1
    source_channel = -1
    notes = []

    @property
    def levels(self):
        return []

    @listenable_property
    def last_played_level(self):
        return -1.0


class VelocityLevelsElement(ProxyElement):
    def __init__(self, velocity_levels=None, *a, **k):
        super().__init__(proxied_object=velocity_levels, proxied_interface=(NullVelocityLevels()))

    def reset(self):
        self.notes = []
        self.source_channel = -1

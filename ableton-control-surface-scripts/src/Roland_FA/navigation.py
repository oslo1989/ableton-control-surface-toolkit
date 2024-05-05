# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Roland_FA/navigation.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 591 bytes
from ableton.v2.control_surface.components import SessionNavigationComponent as SessionNavigationComponentBase

from .scroll import ScrollComponent


class SessionNavigationComponent(SessionNavigationComponentBase):
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._horizontal_paginator = ScrollComponent((self.track_pager_type(self._session_ring)), parent=self)

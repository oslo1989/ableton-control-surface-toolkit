# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Akai_Force_MPC/session_navigation.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 819 bytes
from ableton.v2.control_surface.components import SessionNavigationComponent as SessionNavigationComponentBase


class SessionNavigationComponent(SessionNavigationComponentBase):
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        for scroll_component in (
            self._vertical_banking,
            self._horizontal_banking,
            self._vertical_paginator,
            self._horizontal_paginator,
        ):
            for button in (scroll_component.scroll_up_button, scroll_component.scroll_down_button):
                button.color = "Navigation.Enabled"

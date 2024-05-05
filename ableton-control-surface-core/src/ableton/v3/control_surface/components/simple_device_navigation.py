# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/components/simple_device_navigation.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 2149 bytes
from typing import cast

import Live

from ...live import liveobj_changed, liveobj_valid
from ..display import Renderable
from . import Scrollable, ScrollComponent

NavDirection = Live.Application.Application.View.NavDirection


class SimpleDeviceNavigationComponent(ScrollComponent, Renderable, Scrollable):
    def __init__(self, name="Device_Navigation", *a, **k):
        (super().__init__)(a, name=name, scroll_skin_name="Device.Navigation", **k)
        self._previously_appointed_device = None

    def set_prev_button(self, button):
        self.scroll_up_button.set_control_element(button)

    def set_next_button(self, button):
        self.scroll_down_button.set_control_element(button)

    def can_scroll_up(self):
        return True

    def can_scroll_down(self):
        return True

    def scroll_up(self):
        self._scroll_device_chain(NavDirection.left)

    def scroll_down(self):
        self._scroll_device_chain(NavDirection.right)

    def _scroll_device_chain(self, direction):
        view = self.application.view
        if not (view.is_view_visible("Detail") and view.is_view_visible("Detail/DeviceChain")):
            view.show_view("Detail")
            view.show_view("Detail/DeviceChain")
        else:
            view.scroll_view(direction, "Detail/DeviceChain", False)
        self._tasks.add(self._notify_device_selection)

    def _notify_device_selection(self, _):
        device = self.song.appointed_device
        if liveobj_valid(device):
            if liveobj_changed(device, self._previously_appointed_device):
                self._previously_appointed_device = device
                self.notify(self.notifications.Device.select, cast(str, device.name))

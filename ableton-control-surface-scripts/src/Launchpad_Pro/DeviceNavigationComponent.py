# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_Pro/DeviceNavigationComponent.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1218 bytes
import Live
from _Framework import ControlSurfaceComponent
from _Framework.Control import ButtonControl

NavDirection = Live.Application.Application.View.NavDirection


class DeviceNavigationComponent(ControlSurfaceComponent):
    device_nav_left_button = ButtonControl(color="Device.Off", pressed_color="Device.On")
    device_nav_right_button = ButtonControl(color="Device.Off", pressed_color="Device.On")

    @device_nav_left_button.pressed
    def device_nav_left_button(self, value):
        self._scroll_device_chain(NavDirection.left)

    @device_nav_right_button.pressed
    def device_nav_right_button(self, value):
        self._scroll_device_chain(NavDirection.right)

    def _scroll_device_chain(self, direction):
        view = self.application().view
        if not (view.is_view_visible("Detail") and view.is_view_visible("Detail/DeviceChain")):
            view.show_view("Detail")
            view.show_view("Detail/DeviceChain")
        else:
            view.scroll_view(direction, "Detail/DeviceChain", False)

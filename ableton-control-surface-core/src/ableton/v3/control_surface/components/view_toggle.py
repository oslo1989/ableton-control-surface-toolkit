# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/components/view_toggle.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 2919 bytes
from ...base import MultiSlot
from .. import Component
from ..controls import ToggleButtonControl


class ViewToggleComponent(Component):
    main_view_toggle_button = ToggleButtonControl(color="ViewToggle.SessionOff", on_color="ViewToggle.SessionOn")
    detail_view_toggle_button = ToggleButtonControl(color="ViewToggle.DetailOff", on_color="ViewToggle.DetailOn")
    clip_view_toggle_button = ToggleButtonControl(color="ViewToggle.ClipOff", on_color="ViewToggle.ClipOn")
    browser_view_toggle_button = ToggleButtonControl(color="ViewToggle.BrowserOff", on_color="ViewToggle.BrowserOn")

    def __init__(self, name="View_Toggle", *a, **k):
        (super().__init__)(a, name=name, **k)
        for view_name in ("Session", "Detail", "Detail/Clip", "Browser"):
            self.register_slot(
                MultiSlot(
                    subject=(self.application.view),
                    listener=(self._ViewToggleComponent__update_view_toggle_buttons),
                    event_name_list=("is_view_visible",),
                    extra_args=(view_name,),
                ),
            )

        self._ViewToggleComponent__update_view_toggle_buttons()

    @main_view_toggle_button.toggled
    def main_view_toggle_button(self, is_toggled, _):
        self._show_or_hide_view(is_toggled, "Session")

    @detail_view_toggle_button.toggled
    def detail_view_toggle_button(self, is_toggled, _):
        self._show_or_hide_view(is_toggled, "Detail")

    @clip_view_toggle_button.toggled
    def clip_view_toggle_button(self, is_toggled, _):
        self._show_or_hide_view(is_toggled, "Detail/Clip")

    @browser_view_toggle_button.toggled
    def browser_view_toggle_button(self, is_toggled, _):
        self._show_or_hide_view(is_toggled, "Browser")

    def _show_or_hide_view(self, show_view, view_name):
        if show_view:
            self.application.view.show_view(view_name)
        else:
            self.application.view.hide_view(view_name)

    def __update_view_toggle_buttons(self):
        view = self.application.view
        self.main_view_toggle_button.is_on = view.is_view_visible("Session")
        self.detail_view_toggle_button.is_on = view.is_view_visible("Detail")
        self.clip_view_toggle_button.is_on = view.is_view_visible("Detail/Clip")
        self.browser_view_toggle_button.is_on = view.is_view_visible("Browser")

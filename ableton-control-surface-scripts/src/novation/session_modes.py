# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/novation/session_modes.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1879 bytes
from ableton.v2.base import lazy_attribute, task
from ableton.v2.control_surface.control import ButtonControl
from ableton.v2.control_surface.mode import ModesComponent


class QuickDoubleClickButton(ButtonControl):
    class State(ButtonControl.State):
        @lazy_attribute
        def _double_click_task(self):
            return self.tasks.add(task.wait(0.3))


class SessionModesComponent(ModesComponent):
    cycle_mode_button = QuickDoubleClickButton()
    mode_button_color_control = ButtonControl()

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._last_selected_main_mode = "launch"

    def revert_to_main_mode(self):
        self.selected_mode = self._last_selected_main_mode

    @cycle_mode_button.pressed
    def cycle_mode_button(self, _):
        if self._last_selected_main_mode and self.selected_mode == "overview":
            self.selected_mode = self._last_selected_main_mode
        else:
            if len(self._mode_list) > 2:
                self.selected_mode = "mixer" if self.selected_mode == "launch" else "launch"

    @cycle_mode_button.double_clicked
    def cycle_mode_button(self, _):
        self.selected_mode = "overview"

    def _do_enter_mode(self, name):
        super()._do_enter_mode(name)
        if self.selected_mode != "overview":
            self._last_selected_main_mode = self.selected_mode

    def _update_cycle_mode_button(self, selected):
        if selected == "overview":
            self.mode_button_color_control.color = "Mode.Session.Overview"
        else:
            self.mode_button_color_control.color = (
                "Mode.Session.Mixer" if selected == "mixer" else "Mode.Session.Launch"
            )

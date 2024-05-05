# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_MK3/device.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 3633 bytes
from _Generic.Devices import parameter_bank_names
from ableton.v2.base import listens_group, liveobj_valid, task
from ableton.v2.control_surface.control import control_list
from future.moves.itertools import zip_longest
from novation.simple_device import SimpleDeviceParameterComponent
from novation.simple_device_navigation import SimpleDeviceNavigationComponent
from past.builtins import unicode

from .control import DisplayControl


class DeviceComponent(SimpleDeviceNavigationComponent, SimpleDeviceParameterComponent):
    parameter_name_displays = control_list(DisplayControl, 8)
    parameter_value_displays = control_list(DisplayControl, 8)

    def __init__(self, show_notification=None, *a, **k):
        self._show_notification = show_notification
        (super().__init__)(*a, **k)
        self._show_on_scroll_task = self._tasks.add(
            task.sequence(task.wait(0.1), task.run(self.show_device_name_and_bank)),
        )

    def _on_bank_select_button_checked(self, button):
        super()._on_bank_select_button_checked(button)
        self.show_device_name_and_bank()

    def _on_bank_select_button_released(self):
        self.show_device_name_and_bank()

    def _scroll_device_chain(self, direction):
        super()._scroll_device_chain(direction)
        self._show_on_scroll_task.restart()

    def show_device_name_and_bank(self):
        device = self._device_provider.device
        if liveobj_valid(device):
            self._show_notification(
                device.name,
                parameter_bank_names(device)[self._bank_index] if self.num_banks else "Best of Parameters",
            )
        else:
            self._show_notification(None, None)

    def _on_device_lock_button_toggled(self):
        super()._on_device_lock_button_toggled()
        self._show_notification(
            "Device",
            "Lock {}".format("On" if self._device_provider.is_locked_to_device else "Off"),
        )

    def update(self):
        super().update()
        parameters = self.selected_bank if self._parameter_controls else []
        self._DeviceComponent__on_parameter_name_changed.replace_subjects(parameters)
        self._DeviceComponent__on_parameter_value_changed.replace_subjects(parameters)
        self._update_parameter_name_displays()
        self._update_parameter_value_displays()

    @listens_group("name")
    def __on_parameter_name_changed(self, _):
        self._update_parameter_name_displays()

    @listens_group("value")
    def __on_parameter_value_changed(self, parameter):
        if self.is_enabled():
            display = self.parameter_value_displays[self.selected_bank.index(parameter)]
            display.message = unicode(parameter)

    def _update_parameter_name_displays(self):
        if self.is_enabled():
            for parameter, display in zip_longest(self.selected_bank, self.parameter_name_displays):
                display.message = parameter.name if liveobj_valid(parameter) else "-"

    def _update_parameter_value_displays(self):
        if self.is_enabled():
            for parameter, display in zip_longest(self.selected_bank, self.parameter_value_displays):
                display.message = unicode(parameter) if liveobj_valid(parameter) else "-"

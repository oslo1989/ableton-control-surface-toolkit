# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/components/toggle.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 2802 bytes
from ...base import listens
from ..component import Component


class ToggleComponent(Component):
    is_private = True
    is_momentary = False
    read_only = False

    def __init__(
        self,
        property_name=None,
        subject=None,
        is_momentary=False,
        model_transform=None,
        view_transform=None,
        read_only=False,
        *a,
        **k,
    ):
        (super().__init__)(*a, **k)
        self._property_name = property_name
        self._property_slot = self.register_slot(subject, self._on_property_changed_in_model, property_name)
        self._property_button = None
        if is_momentary:
            self.is_momentary = is_momentary
        if model_transform:
            self.model_transform = model_transform
        if view_transform:
            self.view_transform = view_transform
        if read_only:
            self.read_only = read_only

    def model_transform(self, value):
        return value

    def view_transform(self, value):
        return value

    @property
    def subject(self):
        return self._property_slot.subject

    @subject.setter
    def subject(self, model):
        self._property_slot.subject = model
        self.update()

    @property
    def value(self):
        if self.subject:
            return getattr(self.subject, self._property_name)
        return False

    @value.setter
    def value(self, value):
        setattr(self.subject, self._property_name, value)

    def set_toggle_button(self, button):
        self._property_button = button
        self._ToggleComponent__on_button_value.subject = button
        self._update_button()

    def update(self):
        super().update()
        self._update_button()

    def _update_button(self):
        if self.is_enabled():
            button = self._property_button
            if button:
                button.set_light(self.view_transform(self.value))

    def _on_property_changed_in_model(self):
        self._update_button()

    @listens("value")
    def __on_button_value(self, value):
        if self.is_enabled() and not self.read_only:
            if self.is_momentary:
                if value:
                    self.value = self.model_transform(True)
                else:
                    self.value = self.model_transform(False)
        else:
            if not (value or self._property_button.is_momentary()):
                self.value = self.model_transform(not self.value)

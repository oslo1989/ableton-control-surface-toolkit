# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/pushbase/value_component.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 9563 bytes
from ableton.v2.base import listenable_property, listens
from ableton.v2.control_surface import Component, ParameterSlot
from ableton.v2.control_surface.control import ButtonControl, EncoderControl
from ableton.v2.control_surface.elements import DisplayDataSource
from past.utils import old_div

from . import consts
from .device_parameter_component import convert_parameter_value_to_graphic

NUM_SEGMENTS = 4


def convert_value_to_graphic(value):
    index = int(value * (len(consts.GRAPH_VOL) - 1))
    return consts.GRAPH_VOL[index] if index is not None and index < len(consts.GRAPH_VOL) else " "


class ValueDisplayComponentBase(Component):
    def __init__(self, display_label=" ", display_seg_start=0, *a, **k):
        (super().__init__)(*a, **k)
        self._label_data_source = DisplayDataSource(display_label)
        self._value_data_source = DisplayDataSource()
        self._graphic_data_source = DisplayDataSource()
        self._display_label = display_label
        self._display_seg_start = display_seg_start

    def get_value_string(self):
        raise NotImplementedError

    def get_graphic_string(self):
        raise NotImplementedError

    @listenable_property
    def value_string(self):
        return self.get_value_string()

    def set_label_display(self, display):
        self._set_display(display, self._label_data_source)

    def set_value_display(self, display):
        self._set_display(display, self._value_data_source)

    def set_graphic_display(self, display):
        self._set_display(display, self._graphic_data_source)

    def _set_display(self, display, source):
        if display:
            display.set_data_sources((None,) * NUM_SEGMENTS)
            display.segment(self._display_seg_start).set_data_source(source)

    def update(self):
        super().update()
        if self.is_enabled():
            self._value_data_source.set_display_string(self.get_value_string())
            self._graphic_data_source.set_display_string(self.get_graphic_string())


class ValueComponentBase(Component):
    def create_display_component(self, *a, **k):
        raise NotImplementedError

    def __init__(self, display_label=" ", display_seg_start=0, encoder_touch_delay=0, *a, **k):
        (super().__init__)(*a, **k)
        encoder = EncoderControl(touch_event_delay=encoder_touch_delay)
        encoder.touched = ValueComponentBase._ValueComponentBase__on_encoder_touched
        encoder.released = ValueComponentBase._ValueComponentBase__on_encoder_released
        encoder.value = ValueComponentBase._ValueComponentBase__on_encoder_value
        self.add_control("encoder", encoder)
        self._display = self.create_display_component(display_label=display_label, display_seg_start=display_seg_start)
        self._display.set_enabled(False)

    @property
    def display(self):
        return self._display

    def __on_encoder_touched(self, encoder):
        self._update_display_state()

    def __on_encoder_released(self, encoder):
        self._update_display_state()

    def __on_encoder_value(self, value, encoder):
        self._on_value(value)

    def _on_value(self, value):
        pass

    def _update_display_state(self):
        self._display.set_enabled(self.encoder.is_touched)


class ValueDisplayComponent(ValueDisplayComponentBase):
    def __init__(
        self,
        property_name=None,
        subject=None,
        display_format="%f",
        view_transform=None,
        graphic_transform=None,
        *a,
        **k,
    ):
        (super().__init__)(*a, **k)
        self._subject = subject
        self._property_name = property_name
        self._display_format = display_format
        if view_transform is not None:
            self.view_transform = view_transform
        if graphic_transform is not None:
            self.graphic_transform = graphic_transform
        self.register_slot(subject, self._on_value_changed, property_name)
        self._on_value_changed()

    def view_transform(self, x):
        return x

    def graphic_transform(self, x):
        return self.view_transform(x)

    def get_value_string(self):
        value = getattr(self._subject, self._property_name)
        return self._display_format % self.view_transform(value)

    def get_graphic_string(self):
        value = getattr(self._subject, self._property_name)
        graph = self.graphic_transform(value)
        return convert_value_to_graphic(graph)

    def _on_value_changed(self):
        self.update()
        self.notify_value_string()


class ValueComponent(ValueComponentBase):
    shift_button = ButtonControl()
    encoder_factor = 1.0

    def create_display_component(self, *a, **k):
        return ValueDisplayComponent(
            a,
            parent=self,
            property_name=self._property_name,
            subject=self._subject,
            display_format=self._display_format,
            view_transform=lambda x: self.view_transform(x),
            graphic_transform=lambda x: self.graphic_transform(x),
            **k,
        )

    def __init__(
        self,
        property_name=None,
        subject=None,
        display_format="%f",
        model_transform=None,
        view_transform=None,
        graphic_transform=None,
        encoder_factor=None,
        *a,
        **k,
    ):
        self._property_name = property_name
        self._subject = subject
        self._display_format = display_format
        (super().__init__)(*a, **k)
        if model_transform is not None:
            self.model_transform = model_transform
        if view_transform is not None:
            self.view_transform = view_transform
        if graphic_transform is not None:
            self.graphic_transform = graphic_transform
        if encoder_factor is not None:
            self.encoder_factor = encoder_factor
        self._original_encoder_factor = self.encoder_factor

    def model_transform(self, x):
        return x

    def view_transform(self, x):
        return x

    def graphic_transform(self, x):
        return old_div(self.view_transform(x), self.encoder_factor)

    @shift_button.pressed
    def shift_button(self, button):
        self.encoder_factor = old_div(self._original_encoder_factor, 10.0)

    @shift_button.released
    def shift_button(self, button):
        self.encoder_factor = self._original_encoder_factor

    def _on_value(self, value):
        super()._on_value(value)
        value = self.view_transform(getattr(self._subject, self._property_name)) + value * self.encoder_factor
        setattr(self._subject, self._property_name, self.model_transform(value))


class ParameterValueDisplayComponent(ValueDisplayComponentBase):
    def __init__(self, device_parameter=None, *a, **k):
        (super().__init__)(*a, **k)
        self._on_value_changed.subject = device_parameter
        self._on_value_changed()

    def get_value_string(self):
        return str(self._on_value_changed.subject)

    def get_graphic_string(self):
        return convert_parameter_value_to_graphic(self._on_value_changed.subject)

    @listens("value")
    def _on_value_changed(self):
        self.update()
        self.notify_value_string()


class ParameterValueComponent(ValueComponentBase):
    def create_display_component(self, *a, **k):
        return ParameterValueDisplayComponent(a, device_parameter=self._parameter_slot.parameter, **k)

    def __init__(self, device_parameter=None, *a, **k):
        self._parameter_slot = ParameterSlot(device_parameter)
        (super().__init__)(*a, **k)
        self.register_disconnectable(self._parameter_slot)

    def set_encoder(self, encoder):
        self.encoder.set_control_element(encoder)
        self._parameter_slot.control = encoder

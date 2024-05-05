# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/transmute.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 3747 bytes
from ableton.v2.base import EventObject
from ableton.v2.control_surface import EnumWrappingParameter, IntegerParameter, LiveObjectDecorator
from past.builtins import unicode

from .device_decoration import DeviceSwitchOption


class TransmuteDeviceDecorator(LiveObjectDecorator, EventObject):
    MIN_PITCH_BEND_RANGE = 0
    MAX_PITCH_BEND_RANGE = 24
    polyphony_values = ("2", "4", "8", "16")

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self.frequency_dial_mode_parameter = EnumWrappingParameter(
            name="Frequency Dial Mode",
            parent=self,
            values_host=(self._live_object),
            index_property_host=(self._live_object),
            values_property="frequency_dial_mode_list",
            index_property="frequency_dial_mode",
        )
        self.midi_gate_parameter = EnumWrappingParameter(
            name="Midi Gate",
            parent=self,
            values_host=(self._live_object),
            index_property_host=self,
            values_property="midi_gate_list",
            index_property="midi_gate",
        )
        self.mod_mode_parameter = EnumWrappingParameter(
            name="Mod Mode",
            parent=self,
            values_host=(self._live_object),
            index_property_host=self,
            values_property="mod_mode_list",
            index_property="mod_mode",
        )
        self.mono_poly_parameter = EnumWrappingParameter(
            name="Mono Poly",
            parent=self,
            values_host=(self._live_object),
            index_property_host=self,
            values_property="mono_poly_list",
            index_property="mono_poly",
        )
        self.pitch_mode_parameter = EnumWrappingParameter(
            name="Pitch Mode",
            parent=self,
            values_host=(self._live_object),
            index_property_host=self,
            values_property="pitch_mode_list",
            index_property="pitch_mode",
        )
        self.pitch_bend_range_parameter = IntegerParameter(
            name="Pitch Bend Range",
            parent=self,
            integer_value_host=(self._live_object),
            integer_value_property_name="pitch_bend_range",
            min_value=(self.MIN_PITCH_BEND_RANGE),
            max_value=(self.MAX_PITCH_BEND_RANGE),
            show_as_quantized=False,
            display_value_conversion=(lambda x: unicode(x) + " st"),
        )
        self.polyphony_parameter = EnumWrappingParameter(
            name="Polyphony",
            parent=self,
            values_host=self,
            index_property_host=self,
            values_property="polyphony_values",
            index_property="polyphony",
        )
        self._additional_parameters = (
            self.frequency_dial_mode_parameter,
            self.midi_gate_parameter,
            self.mod_mode_parameter,
            self.mono_poly_parameter,
            self.pitch_mode_parameter,
            self.pitch_bend_range_parameter,
            self.polyphony_parameter,
        )
        self.freq_dial_mode_option = DeviceSwitchOption(
            name="frequency_dial_mode_opt",
            parameter=(self.frequency_dial_mode_parameter),
            labels=["Hz", "Note"],
        )
        self.register_disconnectables(self._additional_parameters)
        self.register_disconnectables(self.options)

    @property
    def options(self):
        return (self.freq_dial_mode_option,)

    @property
    def parameters(self):
        return tuple(self._live_object.parameters) + self._additional_parameters

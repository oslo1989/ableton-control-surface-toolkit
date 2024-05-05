# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Akai_Force_MPC/control.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 2819 bytes
from ableton.v2.base import clamp, listens, liveobj_valid
from ableton.v2.control_surface.control import (
    InputControl,
    MappedControl,
    MappedSensitivitySettingControl,
    SendValueMixin,
    is_internal_parameter,
)
from past.utils import old_div


class SendReceiveValueControl(InputControl):
    class State(SendValueMixin, InputControl.State):
        pass


class MappedAbsoluteControl(MappedControl):
    class State(MappedControl.State):
        def _update_direct_connection(self):
            if self._control_element is None:
                self._control_value.subject = None
            if is_internal_parameter(self.mapped_parameter):
                self._connect_to_internal_parameter()
            else:
                self._connect_to_parameter()

        def _connect_to_internal_parameter(self):
            if self._control_element:
                self._control_element.release_parameter()
                self._control_value.subject = self._control_element

        def _connect_to_parameter(self):
            self._control_value.subject = None
            if self._control_element is not None:
                parameter = self.mapped_parameter
                if liveobj_valid(parameter):
                    self._control_element.connect_to(parameter)
                else:
                    self._control_element.release_parameter()

        @listens("value")
        def _control_value(self, value):
            mapped_parameter = self.mapped_parameter
            if mapped_parameter.is_quantized:
                num_items = len(mapped_parameter.value_items)
                if num_items > 0:
                    mapped_parameter.value = value * num_items // 128
            else:
                mapped_parameter.linear_value = self._midi_value_to_parameter_value(value)

        def _midi_value_to_parameter_value(self, value):
            parameter = self.mapped_parameter
            parameter_min = parameter.min
            parameter_max = parameter.max
            normalized_value = clamp(old_div(value, 127.0), 0.0, 1.0)
            return clamp((parameter_min + parameter_max) * normalized_value, parameter_min, parameter_max)


class SendingMappedAbsoluteControl(MappedAbsoluteControl):
    class State(SendValueMixin, MappedAbsoluteControl.State):
        pass


class SendingMappedSensitivitySettingControl(MappedSensitivitySettingControl):
    class State(SendValueMixin, MappedSensitivitySettingControl.State):
        pass

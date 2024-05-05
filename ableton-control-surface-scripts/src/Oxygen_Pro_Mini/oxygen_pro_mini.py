# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Oxygen_Pro_Mini/oxygen_pro_mini.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 673 bytes
from Oxygen_Pro.mode import ReenterBehaviour
from Oxygen_Pro.oxygen_pro import Oxygen_Pro

from .simple_device import SimpleDeviceParameterComponent


class Oxygen_Pro_Mini(Oxygen_Pro):
    session_width = 4
    pad_ids = ((40, 41, 42, 43), (48, 49, 50, 51))
    device_parameter_component = SimpleDeviceParameterComponent

    def _get_device_mode_behaviour(self):
        return ReenterBehaviour(on_reenter=(self._on_reenter_device_mode))

    def _on_reenter_device_mode(self):
        self._device_parameters.toggle_parameter_offset()

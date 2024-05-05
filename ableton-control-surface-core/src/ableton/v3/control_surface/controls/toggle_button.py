# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/controls/toggle_button.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1317 bytes
from . import ButtonControl, Connectable, control_event


class ToggleButtonControl(ButtonControl):
    toggled = control_event("toggled")

    class State(ButtonControl.State, Connectable):
        requires_listenable_connected_property = True

        def connect_property(self, *a):
            (super().connect_property)(*a)
            self.is_on = self.connected_property_value

        def on_connected_property_changed(self, value):
            self.is_on = value

        def _on_pressed(self):
            super()._on_pressed()
            self.is_on = not self._is_on
            self._call_listener("toggled", self.is_on)
            self.connected_property_value = self.is_on

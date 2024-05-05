# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/FANTOM/control.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 941 bytes
from ableton.v3.control_surface.controls import Control


class DisplayControl(Control):
    class State(Control.State):
        def __init__(self, *a, **k):
            (super().__init__)(*a, **k)
            self._data = ""

        @property
        def data(self):
            return self._data

        @data.setter
        def data(self, data):
            self._data = data
            self._send_current_data()

        def set_control_element(self, control_element):
            super().set_control_element(control_element)
            self._send_current_data()

        def update(self):
            super().update()
            self._send_current_data()

        def _send_current_data(self):
            if self._control_element:
                self._control_element.display_data(self._data)

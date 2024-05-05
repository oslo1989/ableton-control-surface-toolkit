# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/control/text_display.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1485 bytes
from ..elements import DisplayDataSource
from .control import Control


class TextDisplayControl(Control):
    class State(Control.State):
        def __init__(self, segments=("",), *a, **k):
            (super(TextDisplayControl.State, self).__init__)(*a, **k)
            self._data_sources = [DisplayDataSource(segment) for segment in segments]

        def set_control_element(self, control_element):
            if not control_element:
                if self._control_element:
                    self._control_element.set_data_sources(None)
            super(TextDisplayControl.State, self).set_control_element(control_element)
            if control_element:
                control_element.set_data_sources(self._data_sources)

        def __getitem__(self, index):
            return self._data_sources[index].display_string()

        def __setitem__(self, index, value):
            return self._data_sources[index].set_display_string(value)

    def __init__(self, *a, **k):
        super().__init__(extra_args=a, extra_kws=k)


class ConfigurableTextDisplayControl(TextDisplayControl):
    class State(TextDisplayControl.State):
        def set_data_sources(self, data_sources):
            self._data_sources = data_sources
            if self._control_element:
                self._control_element.set_data_sources(data_sources)

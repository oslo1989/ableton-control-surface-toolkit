# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push/global_pad_parameters.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1348 bytes
from ableton.v2.control_surface import Component

from . import sysex


class GlobalPadParameters(Component):
    def __init__(self, aftertouch_threshold=0, *a, **k):
        (super().__init__)(*a, **k)
        self._pad_parameter_element = None
        self._aftertouch_threshold = aftertouch_threshold

    def _get_aftertouch_threshold(self):
        return self._aftertouch_threshold

    def _set_aftertouch_threshold(self, value):
        self._aftertouch_threshold = value
        self._update_pad_parameter_element()

    aftertouch_threshold = property(_get_aftertouch_threshold, _set_aftertouch_threshold)

    def set_pad_parameter(self, element):
        self._pad_parameter_element = element
        self._update_pad_parameter_element()

    def _update_pad_parameter_element(self):
        if self._pad_parameter_element:
            self._pad_parameter_element.send_value(
                sysex.make_pad_parameter_message(aftertouch_threshold=(self._aftertouch_threshold)),
            )

    def update(self):
        super().update()
        if self.is_enabled():
            self._update_pad_parameter_element()

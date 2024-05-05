# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/elements/discrete_values.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 2385 bytes
from ...base import nop
from .. import MIDI_CC_TYPE, InputControlElement, NotifyingControlElement


class ValueElement(NotifyingControlElement):
    def __init__(self, *a, **k):
        (super().__init__)(a, is_private=True, **k)
        self.send_value = nop
        self.set_light = nop
        self.is_momentary = lambda: False

    def reset(self):
        pass


class DiscreteValuesElement(InputControlElement):
    def __init__(self, identifier, channel=0, msg_type=MIDI_CC_TYPE, values=None, *a, **k):
        (super().__init__)(a, **k)
        self._sub_elements = {v: ValueElement() for v in values}

    def script_wants_forwarding(self):
        return True

    def message_map_mode(self):
        raise AssertionError("DiscreteValuesElement doesn't support mapping.")

    def receive_value(self, value):
        super().receive_value(value)
        if value in self._sub_elements:
            self._sub_elements[value].notify_value(127)

    def __iter__(self):
        yield from self._sub_elements.values()

    def __getitem__(self, value):
        return self._sub_elements[value]

    def __len__(self):
        return len(self._sub_elements)

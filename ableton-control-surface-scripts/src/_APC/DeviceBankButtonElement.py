# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_APC/DeviceBankButtonElement.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 797 bytes
from _Framework import ComboElement


class DeviceBankButtonElement(ComboElement):
    def on_nested_control_element_received(self, control):
        super().on_nested_control_element_received(control)
        if control == self.wrapped_control:
            self.wrapped_control.set_channel(1)

    def on_nested_control_element_lost(self, control):
        super().on_nested_control_element_lost(control)
        if control == self.wrapped_control:
            self.wrapped_control.set_channel(0)

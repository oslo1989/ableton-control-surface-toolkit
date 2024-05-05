# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/APC40_MkII/BankToggleComponent.py
# Compiled at: 2023-11-21 10:21:17
# Size of source mod 2**32: 914 bytes
from _Framework import ControlSurfaceComponent
from _Framework.ComboElement import ToggleElement
from _Framework.Control import ToggleButtonControl


class BankToggleComponent(ControlSurfaceComponent):
    bank_toggle_button = ToggleButtonControl()

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._toggle_elements = []

    @bank_toggle_button.toggled
    def bank_toggle_button(self, toggled, button):
        for e in self._toggle_elements:
            e.set_toggled(toggled)

    def create_toggle_element(self, *a, **k):
        element = ToggleElement(*a, **k)
        element.toggled = self.bank_toggle_button.is_toggled
        self._toggle_elements.append(element)
        return element

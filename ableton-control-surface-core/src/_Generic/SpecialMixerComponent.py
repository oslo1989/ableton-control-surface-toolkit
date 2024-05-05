# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Generic/SpecialMixerComponent.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 661 bytes
from _Framework import MixerComponent

from .SelectChanStripComponent import SelectChanStripComponent


class SpecialMixerComponent(MixerComponent):
    def _create_strip(self):
        return SelectChanStripComponent()

    def set_bank_up_button(self, button):
        self.set_bank_buttons(button, self._bank_down_button)

    def set_bank_down_button(self, button):
        self.set_bank_buttons(self._bank_up_button, button)

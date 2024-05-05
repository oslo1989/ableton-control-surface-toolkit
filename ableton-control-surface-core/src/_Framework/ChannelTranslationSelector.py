# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Framework/ChannelTranslationSelector.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 2426 bytes
from .ModeSelectorComponent import ModeSelectorComponent


class ChannelTranslationSelector(ModeSelectorComponent):
    def __init__(self, num_modes=0, *a, **k):
        (super().__init__)(*a, **k)
        self._controls_to_translate = None
        self._initial_num_modes = num_modes

    def disconnect(self):
        ModeSelectorComponent.disconnect(self)
        self._controls_to_translate = None

    def set_controls_to_translate(self, controls):
        for control in controls:
            pass

        self._controls_to_translate = controls

    def number_of_modes(self):
        result = self._initial_num_modes
        if result == 0:
            if self._modes_buttons is not None:
                result = len(self._modes_buttons)
        return result

    def update(self):
        super().update()
        if self._controls_to_translate is not None:
            for control in self._controls_to_translate:
                control.use_default_message()
                if self.is_enabled():
                    control.set_channel((control.message_channel() + self._mode_index) % 16)

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_Pro/TranslationComponent.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1491 bytes
from functools import partial

from _Framework import ControlSurfaceComponent


class TranslationComponent(ControlSurfaceComponent):
    def __init__(self, translated_channel, should_enable=True, should_reset=True, *a, **k):
        self._translated_channel = translated_channel
        self._should_enable = bool(should_enable)
        self._should_reset = should_reset
        (super().__init__)(*a, **k)

    def __getattr__(self, name):
        if len(name) > 4:
            if name[:4] == "set_":
                return partial(self._set_control_elements, name[4:])
        raise AttributeError(name)

    def _set_control_elements(self, name, control_elements):
        if bool(control_elements):
            buttons = control_elements
            for button in buttons:
                if button:
                    if self._should_reset:
                        button.reset()
                    else:
                        button.reset_state()
                    button.set_enabled(self._should_enable)
                    button.set_channel(self._translated_channel)

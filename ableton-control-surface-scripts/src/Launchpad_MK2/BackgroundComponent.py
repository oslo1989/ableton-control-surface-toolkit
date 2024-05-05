# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_MK2/BackgroundComponent.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 989 bytes
from _Framework.BackgroundComponent import BackgroundComponent as BackgroundComponentBase


class BackgroundComponent(BackgroundComponentBase):
    def _clear_control(self, name, control):
        if control:
            control.add_value_listener(self._on_value_listener)
        super()._clear_control(name, control)

    def _on_value_listener(self, *a, **k):
        pass


class TranslatingBackgroundComponent(BackgroundComponent):
    def __init__(self, translation_channel=0, *a, **k):
        (super().__init__)(*a, **k)
        self._translation_channel = translation_channel

    def _clear_control(self, name, control):
        if control:
            control.set_channel(self._translation_channel)
        super()._clear_control(name, control)

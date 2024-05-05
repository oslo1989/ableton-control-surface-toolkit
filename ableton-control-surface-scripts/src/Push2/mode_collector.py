# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/mode_collector.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1782 bytes
from ableton.v2.base import EventObject, listenable_property, listens


class ModeCollector(EventObject):
    def __init__(self, main_modes=None, mix_modes=None, global_mix_modes=None, device_modes=None, *a, **k):
        (super().__init__)(*a, **k)
        self._main_modes = main_modes
        self._mix_modes = mix_modes
        self._global_mix_modes = global_mix_modes
        self._device_modes = device_modes
        self._on_selected_main_mode_changed.subject = main_modes
        self._on_selected_mix_mode_changed.subject = mix_modes
        self._on_selected_global_mix_mode_changed.subject = global_mix_modes
        self._on_selected_device_mode_changed.subject = device_modes

    @listenable_property
    def main_mode(self):
        return self._main_modes.selected_mode

    @listens("selected_mode")
    def _on_selected_main_mode_changed(self, mode):
        self.notify_main_mode()

    @listenable_property
    def mix_mode(self):
        return self._mix_modes.selected_mode

    @listens("selected_mode")
    def _on_selected_mix_mode_changed(self, mode):
        self.notify_mix_mode()

    @listenable_property
    def global_mix_mode(self):
        return self._global_mix_modes.selected_mode

    @listens("selected_mode")
    def _on_selected_global_mix_mode_changed(self, mode):
        self.notify_global_mix_mode()

    @listenable_property
    def device_mode(self):
        return self._device_modes.selected_mode

    @listens("selected_mode")
    def _on_selected_device_mode_changed(self, mode):
        self.notify_device_mode()

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/APC64/mixer.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 2116 bytes
from ableton.v3.control_surface.components import ChannelStripComponent, SendIndexManager
from ableton.v3.control_surface.components import MixerComponent as MixerComponentBase


class TargetStripComponent(ChannelStripComponent):
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._send_controls = []
        self._send_index_manager = self.register_disconnectable(SendIndexManager(cycle_size=6))
        self.register_slot(self._send_index_manager, self._update_send_controls, "send_index")

    def set_send_controls(self, controls):
        self._send_controls = controls or []
        self._update_send_controls()

    def cycle_send_index(self):
        self._send_index_manager.cycle_send_index(range_name="CH Strip")

    def _update_send_controls(self):
        if self._send_index_manager.send_index is None:
            self.send_controls.set_control_element(self._send_controls)
        else:
            self.send_controls.set_control_element(
                [None] * self._send_index_manager.send_index + list(self._send_controls),
            )
            self.update()


class MixerComponent(MixerComponentBase):
    def __getattr__(self, name):
        if name == "set_target_track_send_controls":
            return self._target_strip.set_send_controls
        return super().__getattr__(name)

    def _create_channel_strip(self, is_master=False, is_target=False):
        if is_target:
            return TargetStripComponent(parent=self)
        return super()._create_channel_strip(is_master=is_master)

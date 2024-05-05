# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/APC_mini/APC_mini.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1468 bytes
from _APC.ControlElementUtils import make_slider
from _Framework.Layer import Layer, SimpleLayerOwner
from APC_Key_25 import APC_Key_25


class APC_mini(APC_Key_25):
    SESSION_HEIGHT = 8
    HAS_TRANSPORT = False

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        with self.component_guard():
            self.register_disconnectable(
                SimpleLayerOwner(layer=Layer(_unused_buttons=(self.wrap_matrix(self._unused_buttons)))),
            )

    def _make_stop_all_button(self):
        return self.make_shifted_button(self._scene_launch_buttons[7])

    def _create_controls(self):
        super()._create_controls()
        self._unused_buttons = list(map(self.make_shifted_button, self._scene_launch_buttons[5:7]))
        self._master_volume_control = make_slider(0, 56, name="Master_Volume")

    def _create_mixer(self):
        mixer = super()._create_mixer()
        mixer.master_strip().layer = Layer(volume_control=(self._master_volume_control))
        return mixer

    def _product_model_id_byte(self):
        return 40

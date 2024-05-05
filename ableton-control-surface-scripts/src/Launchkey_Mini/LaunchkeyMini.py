# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_Mini/LaunchkeyMini.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1573 bytes
from Launchkey.Launchkey import Launchkey, LaunchkeyControlFactory, make_button


class LaunchkeyMiniControlFactory(LaunchkeyControlFactory):
    def create_next_track_button(self):
        return make_button(107, "Next_Track_Button")

    def create_prev_track_button(self):
        return make_button(106, "Prev_Track_Button")


class LaunchkeyMini(Launchkey):
    def __init__(self, c_instance):
        super().__init__(
            c_instance,
            control_factory=(LaunchkeyMiniControlFactory()),
            identity_response=(240, 126, 127, 6, 2, 0, 32, 41, 53, 0, 0),
        )
        self._suggested_input_port = "LK Mini InControl"
        self._suggested_output_port = "LK Mini InControl"

    def _setup_navigation(self):
        super()._setup_navigation()
        self._next_scene_button = make_button(105, "Next_Scene_Button")
        self._prev_scene_button = make_button(104, "Prev_Scene_Button")
        self._session_navigation.set_next_scene_button(self._next_scene_button)
        self._session_navigation.set_prev_scene_button(self._prev_scene_button)

    def _setup_transport(self):
        pass

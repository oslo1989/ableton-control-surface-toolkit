# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_Mini_MK3/elements.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 662 bytes
from novation.launchkey_elements import LaunchkeyElements


class Elements(LaunchkeyElements):
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self.record_button_with_shift = self.with_shift(self.record_button)
        self.scene_launch_button_with_shift = self.with_shift(self.scene_launch_buttons_raw[0])
        self.stop_solo_mute_button_with_shift = self.with_shift(self.scene_launch_buttons_raw[1])

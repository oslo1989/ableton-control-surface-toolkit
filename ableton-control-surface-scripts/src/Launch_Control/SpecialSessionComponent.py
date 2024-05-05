# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launch_Control/SpecialSessionComponent.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 567 bytes
from future.moves.itertools import zip_longest

from _Framework import SessionComponent


class SpecialSessionComponent(SessionComponent):
    def set_clip_launch_buttons(self, buttons):
        for i, button in zip_longest(range(self._num_tracks), buttons or []):
            scene = self.selected_scene()
            slot = scene.clip_slot(i)
            slot.set_launch_button(button)

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_mkII/mixer.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 599 bytes
from ableton.v2.base import liveobj_valid
from novation.mixer import MixerComponent as MixerComponentBase


class MixerComponent(MixerComponentBase):
    def set_selected_track_name_display(self, display):
        self._selected_strip.set_track_name_display(display)

    def _update_selected_strip(self):
        selected_strip = self._selected_strip
        if liveobj_valid(selected_strip):
            selected_strip.set_track(self.song.view.selected_track)

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/novation/drum_group.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 726 bytes
from ableton.v2.control_surface.components import DrumGroupComponent as DrumGroupComponentBase

from .util import skin_scroll_buttons


class DrumGroupComponent(DrumGroupComponentBase):
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        skin_scroll_buttons(self._position_scroll, "DrumGroup.Navigation", "DrumGroup.NavigationPressed")
        skin_scroll_buttons(self._page_scroll, "DrumGroup.Navigation", "DrumGroup.NavigationPressed")

    def set_parent_track(self, track):
        pass

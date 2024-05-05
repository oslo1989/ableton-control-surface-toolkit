# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_Essential/view_control.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 902 bytes
from ableton.v2.control_surface.components import BasicSceneScroller, ScrollComponent
from ableton.v2.control_surface.components import ViewControlComponent as ViewControlComponentBase
from ableton.v2.control_surface.control import StepEncoderControl


class ViewControlComponent(ViewControlComponentBase):
    scene_scroll_encoder = StepEncoderControl(num_steps=64)

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._scroll_scenes = ScrollComponent((BasicSceneScroller()), parent=self)

    @scene_scroll_encoder.value
    def scene_scroll_encoder(self, value, _):
        if value > 0:
            self._scroll_scenes.scroll_down()
        else:
            if value < 0:
                self._scroll_scenes.scroll_up()

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/elements/playhead_element.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 681 bytes
from ...base import nop
from .proxy_element import ProxyElement


class NullPlayhead:
    notes = []
    start_time = 0.0
    step_length = 1.0
    velocity = 0.0
    wrap_around = False
    track = None
    clip = None
    set_feedback_channels = nop


class PlayheadElement(ProxyElement):
    def __init__(self, playhead=None, *a, **k):
        super().__init__(proxied_object=playhead, proxied_interface=(NullPlayhead()))

    def reset(self):
        self.track = None

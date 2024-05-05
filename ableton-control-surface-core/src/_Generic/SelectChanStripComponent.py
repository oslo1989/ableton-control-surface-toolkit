# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Generic/SelectChanStripComponent.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1046 bytes
from _Framework import ChannelStripComponent


class SelectChanStripComponent(ChannelStripComponent):
    def __init__(self):
        ChannelStripComponent.__init__(self)

    def _arm_value(self, value):
        if self.is_enabled():
            track_was_armed = False
            if self._track is not None:
                if self._track.can_be_armed:
                    track_was_armed = self._track.arm
            ChannelStripComponent._arm_value(self, value)
            if self._track is None and self._track.can_be_armed or self._track.arm:
                if not track_was_armed:
                    if self._track.view.select_instrument():
                        self.song().view.selected_track = self._track

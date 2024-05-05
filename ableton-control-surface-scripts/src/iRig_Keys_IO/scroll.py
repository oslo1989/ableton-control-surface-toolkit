# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/iRig_Keys_IO/scroll.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 710 bytes
from ableton.v2.base import nop
from ableton.v2.control_surface.components import ScrollComponent as ScrollComponentBase
from ableton.v2.control_surface.control import EncoderControl


class ScrollComponent(ScrollComponentBase):
    scroll_encoder = EncoderControl()

    @scroll_encoder.value
    def scroll_encoder(self, value, _):
        scroll_step = nop
        if value > 0 and self.can_scroll_down():
            scroll_step = self._do_scroll_down
        else:
            if value < 0:
                if self.can_scroll_up():
                    scroll_step = self._do_scroll_up
        scroll_step()

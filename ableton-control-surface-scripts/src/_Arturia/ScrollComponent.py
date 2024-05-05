# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Arturia/ScrollComponent.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 821 bytes
from _Framework.Control import EncoderControl
from _Framework.ScrollComponent import ScrollComponent as ScrollComponentBase


class ScrollComponent(ScrollComponentBase):
    scroll_encoder = EncoderControl()

    def set_scroll_encoder(self, encoder):
        self.scroll_encoder.set_control_element(encoder)
        self.update()

    @scroll_encoder.value
    def scroll_encoder(self, value, encoder):
        scroll_step = None
        if value > 0 and self.can_scroll_down():
            scroll_step = self._do_scroll_down
        else:
            if value < 0:
                if self.can_scroll_up():
                    scroll_step = self._do_scroll_up
        if scroll_step is not None:
            scroll_step()

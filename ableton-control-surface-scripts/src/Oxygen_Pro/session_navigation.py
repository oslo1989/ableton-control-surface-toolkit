# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Oxygen_Pro/session_navigation.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 740 bytes
from ableton.v2.control_surface.components import SessionNavigationComponent as SessionNavigationComponentBase
from ableton.v2.control_surface.control import EncoderControl


class SessionNavigationComponent(SessionNavigationComponentBase):
    scene_encoder = EncoderControl()

    @scene_encoder.value
    def scene_encoder(self, value, _):
        if value > 0:
            if self._vertical_banking.can_scroll_up():
                self._vertical_banking.scroll_up()
        else:
            if self._vertical_banking.can_scroll_down():
                self._vertical_banking.scroll_down()

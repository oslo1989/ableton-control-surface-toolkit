# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Roland_FA/transport.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 512 bytes
from ableton.v2.control_surface.components import TransportComponent as TransportComponentBase
from ableton.v2.control_surface.control import ButtonControl


class TransportComponent(TransportComponentBase):
    jump_to_start_button = ButtonControl()

    @jump_to_start_button.pressed
    def jump_to_start_button(self, _):
        self.song.current_song_time = 0.0

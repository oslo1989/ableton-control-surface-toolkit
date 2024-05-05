# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_MK3/rgb_button.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1017 bytes
from ableton.v2.control_surface.elements import ButtonElement


class RgbButtonElement(ButtonElement):
    def __init__(self, *a, **k):
        self._led_channel = k.pop("led_channel", 0)
        (super().__init__)(*a, **k)

    def _do_send_value(self, value, channel=None):
        super()._do_send_value(value, channel=(self._led_channel))

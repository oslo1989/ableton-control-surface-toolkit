# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/MIDI_Mix/MixerComponent.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1306 bytes
from _APC.MixerComponent import MixerComponent as MixerComponentBase
from _Framework.Control import ButtonControl


class MixerComponent(MixerComponentBase):
    bank_up_button = ButtonControl(color="DefaultButton.Off", pressed_color="DefaultButton.On")
    bank_down_button = ButtonControl(color="DefaultButton.Off", pressed_color="DefaultButton.On")

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)

    def set_send_controls(self, controls):
        self._send_controls = controls
        if controls:
            for index, strip in enumerate(self._channel_strips):
                strip.set_send_controls((controls.get_button(index, 0), controls.get_button(index, 1)))

    @bank_up_button.pressed
    def bank_up_button(self, button):
        new_offset = self._track_offset + len(self._channel_strips)
        if len(self.tracks_to_use()) > new_offset:
            self.set_track_offset(new_offset)

    @bank_down_button.pressed
    def bank_down_button(self, button):
        self.set_track_offset(max(0, self._track_offset - len(self._channel_strips)))

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_Pro_MK3/transport.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 783 bytes
from novation.blinking_button import BlinkingButtonControl
from novation.transport import TransportComponent as TransportComponentBase


class TransportComponent(TransportComponentBase):
    capture_midi_button = BlinkingButtonControl(
        color="Transport.CaptureOff",
        blink_on_color="Transport.CaptureOn",
        blink_off_color="Transport.CaptureOff",
    )

    @capture_midi_button.pressed
    def capture_midi_button(self, _):
        try:
            if self.song.can_capture_midi:
                self.song.capture_midi()
                self.capture_midi_button.start_blinking()
        except RuntimeError:
            pass

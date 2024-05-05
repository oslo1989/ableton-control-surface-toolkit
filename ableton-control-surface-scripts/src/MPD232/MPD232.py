# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/MPD232/MPD232.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1798 bytes
from _Framework import ButtonMatrixElement
from _MPDMkIIBase import MPDMkIIBase
from _MPDMkIIBase.ControlElementUtils import make_button, make_encoder, make_slider

PAD_CHANNEL = 1
PAD_IDS = [[81, 83, 84, 86], [74, 76, 77, 79], [67, 69, 71, 72], [60, 62, 64, 65]]


class MPD232(MPDMkIIBase):
    def __init__(self, *a, **k):
        (super().__init__)(PAD_IDS, PAD_CHANNEL, *a, **k)
        with self.component_guard():
            self._create_device()
            self._create_transport()
            self._create_mixer()

    def _create_controls(self):
        self._create_pads()
        self._encoders = ButtonMatrixElement(
            rows=[
                [make_encoder(identifier, 0, "Encoder_%d" % index) for index, identifier in enumerate(range(22, 30))],
            ],
        )
        self._sliders = ButtonMatrixElement(
            rows=[[make_slider(identifier, 0, "Slider_%d" % index) for index, identifier in enumerate(range(12, 20))]],
        )
        self._control_buttons = ButtonMatrixElement(
            rows=[
                [
                    make_button(identifier, 0, "Control_Button_%d" % index)
                    for index, identifier in enumerate(range(32, 40))
                ],
            ],
        )
        self._play_button = make_button(118, 0, "Play_Button")
        self._stop_button = make_button(117, 0, "Stop_Button")
        self._record_button = make_button(119, 0, "Record_Button")

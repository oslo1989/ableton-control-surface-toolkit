# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/APC40_MkII/QuantizationComponent.py
# Compiled at: 2023-11-21 10:21:17
# Size of source mod 2**32: 1975 bytes
import Live
from _Framework import ControlSurfaceComponent
from _Framework.Control import RadioButtonControl, control_list
from _Framework.SubjectSlot import subject_slot

AVAILABLE_QUANTIZATION = [
    Live.Song.Quantization.q_no_q,
    Live.Song.Quantization.q_8_bars,
    Live.Song.Quantization.q_4_bars,
    Live.Song.Quantization.q_2_bars,
    Live.Song.Quantization.q_bar,
    Live.Song.Quantization.q_quarter,
    Live.Song.Quantization.q_eight,
    Live.Song.Quantization.q_sixtenth,
]


class QuantizationComponent(ControlSurfaceComponent):
    quantization_buttons = control_list(RadioButtonControl)

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self.quantization_buttons.control_count = len(AVAILABLE_QUANTIZATION) + 1
        self._on_clip_trigger_quantization_changed.subject = self.song()
        self._on_clip_trigger_quantization_changed()

    @quantization_buttons.checked
    def quantization_buttons(self, button):
        if 0 <= button.index < len(AVAILABLE_QUANTIZATION):
            quantization = AVAILABLE_QUANTIZATION[button.index]
            if quantization != self.song().clip_trigger_quantization:
                self.song().clip_trigger_quantization = quantization

    @subject_slot("clip_trigger_quantization")
    def _on_clip_trigger_quantization_changed(self):
        self._get_button(self.song().clip_trigger_quantization).is_checked = True

    def _get_button(self, quantization):
        if quantization in AVAILABLE_QUANTIZATION:
            return self.quantization_buttons[AVAILABLE_QUANTIZATION.index(quantization)]
        return self.quantization_buttons[-1]

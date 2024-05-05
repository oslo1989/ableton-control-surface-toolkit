# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push/quantization_settings.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 2949 bytes
from ableton.v2.base import listens
from ableton.v2.control_surface.control import TextDisplayControl
from pushbase.quantization_component import QUANTIZATION_NAMES, quantize_amount_to_string
from pushbase.quantization_component import QuantizationSettingsComponent as QuantizationSettingsComponentBase


class QuantizationSettingsComponent(QuantizationSettingsComponentBase):
    display_line1 = TextDisplayControl(segments=("", "", "", "", "", "", "", ""))
    display_line2 = TextDisplayControl(segments=("Swing", "Quantize", "Quantize", "", "", "", "", "Record"))
    display_line3 = TextDisplayControl(segments=("Amount", "To", "Amount", "", "", "", "", "Quantize"))
    display_line4 = TextDisplayControl(segments=("", "", "", "", "", "", "", ""))

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._update_swing_amount_display()
        self._update_quantize_to_display()
        self._update_quantize_amount_display()
        self._update_record_quantization_display()
        self._QuantizationSettingsComponent__on_swing_amount_changed.subject = self.song
        self._QuantizationSettingsComponent__on_record_quantization_index_changed.subject = self
        self._QuantizationSettingsComponent__on_record_quantization_enabled_changed.subject = self
        self._QuantizationSettingsComponent__on_quantize_to_index_changed.subject = self
        self._QuantizationSettingsComponent__on_quantize_amount_changed.subject = self

    def _update_swing_amount_display(self):
        self.display_line1[0] = str(int(self.song.swing_amount * 200.0)) + "%"

    def _update_record_quantization_display(self):
        record_quantization_on = self.record_quantization_toggle_button.is_toggled
        self.display_line1[-1] = QUANTIZATION_NAMES[self.record_quantization_index]
        self.display_line4[-1] = "[  On  ]" if record_quantization_on else "[  Off ]"

    def _update_quantize_to_display(self):
        self.display_line1[1] = QUANTIZATION_NAMES[self.quantize_to_index]

    def _update_quantize_amount_display(self):
        self.display_line1[2] = quantize_amount_to_string(self.quantize_amount)

    @listens("quantize_to_index")
    def __on_quantize_to_index_changed(self, _):
        self._update_quantize_to_display()

    @listens("quantize_amount")
    def __on_quantize_amount_changed(self, _):
        self._update_quantize_amount_display()

    @listens("swing_amount")
    def __on_swing_amount_changed(self):
        self._update_swing_amount_display()

    @listens("record_quantization_index")
    def __on_record_quantization_index_changed(self, _):
        self._update_record_quantization_display()

    @listens("record_quantization_enabled")
    def __on_record_quantization_enabled_changed(self, _):
        self._update_record_quantization_display()

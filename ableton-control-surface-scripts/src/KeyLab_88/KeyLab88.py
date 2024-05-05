# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_88/KeyLab88.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 862 bytes
from KeyLab import KeyLab


class KeyLab88(KeyLab):
    def _setup_hardware_encoder(self, hardware_id, identifier, channel=0):
        self._set_encoder_cc_msg_type(hardware_id)
        self._set_identifier(hardware_id, identifier)
        self._set_channel(hardware_id, channel)
        self._set_binary_offset_mode(hardware_id)

    def _setup_hardware_button(self, hardware_id, identifier, channel=0, **k):
        self._set_button_msg_type(hardware_id, "cc")
        self._set_channel(hardware_id, channel)
        self._set_identifier(hardware_id, identifier)
        self._set_value_minimum(hardware_id)
        self._set_value_maximum(hardware_id)
        self._set_momentary_mode(hardware_id, is_momentary=True)

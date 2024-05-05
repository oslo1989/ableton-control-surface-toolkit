# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Axiom_DirectLink/PeekableEncoderElement.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 2064 bytes
from _Framework import EncoderElement
from _Framework.InputControlElement import *


class PeekableEncoderElement(EncoderElement):
    def __init__(self, msg_type, channel, identifier, map_mode):
        EncoderElement.__init__(self, msg_type, channel, identifier, map_mode)
        self._peek_mode = False

    def set_peek_mode(self, peek_mode):
        if self._peek_mode != peek_mode:
            self._peek_mode = peek_mode
            self._request_rebuild()

    def get_peek_mode(self):
        return self._peek_mode

    def install_connections(self, install_translation_callback, install_mapping_callback, install_forwarding_callback):
        current_parameter = self._parameter_to_map_to
        if self._peek_mode:
            self._parameter_to_map_to = None
        InputControlElement.install_connections(
            self,
            install_translation_callback,
            install_mapping_callback,
            install_forwarding_callback,
        )
        self._parameter_to_map_to = current_parameter

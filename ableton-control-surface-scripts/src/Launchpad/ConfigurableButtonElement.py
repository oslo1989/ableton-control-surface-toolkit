# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad/ConfigurableButtonElement.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 4215 bytes
from _Framework.ButtonElement import *


class ConfigurableButtonElement(ButtonElement):
    def __init__(self, is_momentary, msg_type, channel, identifier):
        ButtonElement.__init__(self, is_momentary, msg_type, channel, identifier)
        self._on_value = 127
        self._off_value = 4
        self._is_enabled = True
        self._is_notifying = False
        self._force_next_value = False
        self._pending_listeners = []

    def set_on_off_values(self, on_value, off_value):
        self.clear_send_cache()
        self._on_value = on_value
        self._off_value = off_value

    def set_force_next_value(self):
        self._force_next_value = True

    def set_enabled(self, enabled):
        self._is_enabled = enabled

    def turn_on(self):
        self.send_value(self._on_value)

    def turn_off(self):
        self.send_value(self._off_value)

    def reset(self):
        self.send_value(4)

    def add_value_listener(self, callback, identify_sender=False):
        if not self._is_notifying:
            ButtonElement.add_value_listener(self, callback, identify_sender)
        else:
            self._pending_listeners.append((callback, identify_sender))

    def receive_value(self, value):
        self._is_notifying = True
        ButtonElement.receive_value(self, value)
        self._is_notifying = False
        for listener in self._pending_listeners:
            self.add_value_listener(listener[0], listener[1])

        self._pending_listeners = []

    def send_value(self, value, force=False):
        ButtonElement.send_value(self, value, force or self._force_next_value)
        self._force_next_value = False

    def install_connections(self, install_translation_callback, install_mapping_callback, install_forwarding_callback):
        if self._is_enabled:
            ButtonElement.install_connections(
                self,
                install_translation_callback,
                install_mapping_callback,
                install_forwarding_callback,
            )
        else:
            if self._msg_channel != self._original_channel or self._msg_identifier != self._original_identifier:
                install_translation_callback(
                    self._msg_type,
                    self._original_identifier,
                    self._original_channel,
                    self._msg_identifier,
                    self._msg_channel,
                )

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/MackieControl_Classic/MainDisplay.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 3343 bytes
from ableton.v3.base import as_ascii

from .MackieControlComponent import *


class MainDisplay(MackieControlComponent):
    def __init__(self, main_script):
        MackieControlComponent.__init__(self, main_script)
        self._MainDisplay__stack_offset = 0
        self._MainDisplay__last_send_messages = [[], []]

    def destroy(self):
        NUM_CHARS_PER_DISPLAY_LINE = 54
        upper_message = "Ableton Live".center(NUM_CHARS_PER_DISPLAY_LINE)
        self.send_display_string(upper_message, 0, 0)
        lower_message = "Device is offline".center(NUM_CHARS_PER_DISPLAY_LINE)
        self.send_display_string(lower_message, 1, 0)
        MackieControlComponent.destroy(self)

    def stack_offset(self):
        return self._MainDisplay__stack_offset

    def set_stack_offset(self, offset):
        self._MainDisplay__stack_offset = offset

    def send_display_string(self, display_string, display_row, cursor_offset):
        if display_row == 0:
            offset = cursor_offset
        else:
            if display_row == 1:
                offset = NUM_CHARS_PER_DISPLAY_LINE + 2 + cursor_offset
            else:
                pass
        message_string = as_ascii(display_string)
        if self._MainDisplay__last_send_messages[display_row] != message_string:
            self._MainDisplay__last_send_messages[display_row] = message_string
            device_type = SYSEX_DEVICE_TYPE_XT if self.main_script().is_extension() else SYSEX_DEVICE_TYPE
            display_sysex = (240, 0, 0, 102, device_type, 18, offset, *tuple(message_string), 247)
            self.send_midi(display_sysex)

    def refresh_state(self):
        self._MainDisplay__last_send_messages = [[], []]

    def on_update_display_timer(self):
        pass

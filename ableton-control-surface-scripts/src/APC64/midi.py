# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/APC64/midi.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1197 bytes
from ableton.v3.control_surface.midi import SYSEX_END, SYSEX_START

HALF_BRIGHTNESS_LED_CHANNEL = 0
FULL_BRIGHTNESS_LED_CHANNEL = 6
PULSE_LED_CHANNEL = 10
BLINK_LED_CHANNEL = 14
SYSEX_HEADER = (SYSEX_START, 71, 0, 83)
DISPLAY_MESSAGE_ID = 16
SET_DISPLAY_OWNER_ID = 28
MODE_MESSAGE_ID = 25
TRACK_TYPE_MESSAGE_ID = 27
RTC_START_MESSAGE_ID = 32
RTC_DATA_MESSAGE_ID = 33
RTC_END_MESSAGE_ID = 34


def make_message(message_id, *payload):
    msg_size = len(payload)
    return (*SYSEX_HEADER, message_id, msg_size >> 7 & 127, msg_size & 127, *payload, SYSEX_END)

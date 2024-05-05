# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Akai_Force_MPC/sysex.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 600 bytes
SYSEX_MSG_HEADER = (240, 71, 0)
SYSEX_END_BYTE = 247
MPC_X_PRODUCT_ID = 58
MPC_LIVE_PRODUCT_ID = 59
FORCE_PRODUCT_ID = 64
SUPPORTED_PRODUCT_IDS = (MPC_LIVE_PRODUCT_ID, MPC_X_PRODUCT_ID, FORCE_PRODUCT_ID)
BROADCAST_ID = 127
PING_MSG_TYPE = 0
PONG_MSG_TYPE = 1
TEXT_MSG_TYPE = 16
COLOR_MSG_TYPE = 17
PING_MSG = (*SYSEX_MSG_HEADER, BROADCAST_ID, PING_MSG_TYPE, SYSEX_END_BYTE)
INNER_MESSAGE_MAX_LENGTH = 251
NUM_MSG_IDENTIFYING_BYTES = 3

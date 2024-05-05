# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Framework/Defaults.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 432 bytes
from past.utils import old_div

TIMER_DELAY = 0.1
MOMENTARY_DELAY = 0.3
MOMENTARY_DELAY_TICKS = int(old_div(MOMENTARY_DELAY, TIMER_DELAY))

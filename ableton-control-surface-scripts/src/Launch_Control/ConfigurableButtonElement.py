# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launch_Control/ConfigurableButtonElement.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 588 bytes
from Launchpad.ConfigurableButtonElement import ConfigurableButtonElement as LaunchpadButtonElement

from . import Colors


class ConfigurableButtonElement(LaunchpadButtonElement):
    def set_light(self, value):
        if value is Colors.LED_OFF:
            self.send_value(value)
        else:
            super().set_light(value)

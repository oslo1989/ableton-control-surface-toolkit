# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/elements/full_velocity_element.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 466 bytes
from .proxy_element import ProxyElement


class NullFullVelocity:
    enabled = False


class FullVelocityElement(ProxyElement):
    def __init__(self, full_velocity=None, *a, **k):
        super().__init__(proxied_object=full_velocity, proxied_interface=(NullFullVelocity()))

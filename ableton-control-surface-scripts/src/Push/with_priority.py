# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push/with_priority.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 622 bytes
from ableton.v2.control_surface import DEFAULT_PRIORITY
from ableton.v2.control_surface.elements import WrapperElement


class WithPriority(WrapperElement):
    def __init__(self, wrapped_priority=DEFAULT_PRIORITY, *a, **k):
        (super().__init__)(*a, **k)
        self.wrapped_priority = wrapped_priority
        self.register_control_element(self.wrapped_control)

    def get_control_element_priority(self, element, priority):
        return self.wrapped_priority

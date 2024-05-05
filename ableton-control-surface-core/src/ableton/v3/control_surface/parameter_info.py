# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/parameter_info.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 950 bytes
from ableton.v2.control_surface import ParameterInfo as ParameterInfoBase

from ..live import liveobj_valid


class ParameterInfo(ParameterInfoBase):
    def __init__(self, parameter=None, name=None, *a, **k):
        (super().__init__)(a, parameter=parameter, name=name, **k)
        if liveobj_valid(parameter):
            if name is not None:
                parameter.display_name = name

    @property
    def original_name(self):
        if liveobj_valid(self.parameter):
            return self.parameter.original_name
        return ""

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/clip_creator.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1178 bytes
import Live

_Q = Live.Song.Quantization


class ClipCreator:
    grid_quantization = None
    is_grid_triplet = False
    fixed_length = 8
    legato_launch = True

    def create(self, slot, length=None, launch_quantization=None, legato_launch=None):
        if length is None:
            length = self.fixed_length
        slot.create_clip(length)
        should_legato_launch = self.legato_launch if legato_launch is None else legato_launch
        if self.grid_quantization is not None:
            slot.clip.view.grid_quantization = self.grid_quantization
            slot.clip.view.grid_is_triplet = self.is_grid_triplet
        if launch_quantization is None or should_legato_launch:
            launch_quantization = _Q.q_no_q
        slot.fire(force_legato=should_legato_launch, launch_quantization=launch_quantization)

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/pushbase/mixer_utils.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 431 bytes
import Live
from ableton.v2.base import old_hasattr


def is_set_to_split_stereo(mixer):
    modes = Live.MixerDevice.MixerDevice.panning_modes
    return modes.stereo_split == getattr(mixer, "panning_mode", modes.stereo)


def has_pan_mode(mixer):
    return old_hasattr(mixer, "panning_mode")

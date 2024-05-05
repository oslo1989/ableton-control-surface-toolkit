# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/pushbase/device_chain_utils.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 740 bytes
import Live
from ableton.v2.base import find_if


def is_empty_drum_pad(drum_pad):
    return isinstance(drum_pad, Live.DrumPad.DrumPad) and (not drum_pad.chains or not drum_pad.chains[0].devices)


def is_first_device_on_pad(device, drum_pad):
    return find_if(
        lambda pad: pad.chains and pad.chains[0].devices and pad.chains[0].devices[0] == device,
        drum_pad.canonical_parent.drum_pads,
    )


def is_simpler(device):
    return device and device.class_name == "OriginalSimpler"

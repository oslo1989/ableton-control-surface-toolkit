# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Blackstar_Live_Logic/clip_util.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1885 bytes
from ableton.v2.base import liveobj_valid
from past.utils import old_div


def has_clip(slot):
    if liveobj_valid(slot):
        return slot.has_clip
    return None


def clip_of_slot(slot):
    if liveobj_valid(slot):
        if liveobj_valid(slot.clip):
            return slot.clip
        return None
    return None


def fire(clip_or_slot, **k):
    if liveobj_valid(clip_or_slot):
        (clip_or_slot.fire)(**k)
        return True
    return False


def delete_clip(slot):
    if liveobj_valid(slot):
        if has_clip(slot):
            slot.delete_clip()
            return True
    return False


def is_looping(clip):
    if liveobj_valid(clip):
        return clip.looping
    return None


def get_clip_time(clip):
    sig_num, sig_denom = clip.signature_numerator, clip.signature_denominator
    loop_position = (clip.playing_position - clip.loop_start) * old_div(sig_denom, 4.0)
    beats = int(loop_position) % sig_num + 1
    bars = int(old_div(loop_position, sig_num)) + 1
    return (bars, beats)

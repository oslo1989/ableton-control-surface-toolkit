# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Blackstar_Live_Logic/track_util.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 6710 bytes
from itertools import chain

import Live
from ableton.v2.base import compose, const, depends, find_if, liveobj_valid

from .clip_util import clip_of_slot, has_clip


def playing_slot_index(track):
    if liveobj_valid(track):
        return track.playing_slot_index
    return None


def playing_or_recording_clip_slot(track):
    index = playing_slot_index(track)
    if index is not None:
        if index >= 0:
            slot = track.clip_slots[index]
            if liveobj_valid(slot):
                return slot
            return None
        return None
    return None


def fired_clip_slot(track):
    if liveobj_valid(track):
        if track.fired_slot_index >= 0:
            slot = track.clip_slots[track.fired_slot_index]
            if liveobj_valid(slot):
                return slot
            return None
        return None
    return None


def is_fired(track):
    if liveobj_valid(track):
        return track.fired_slot_index != -1
    return None


def playing_clip_slot(track):
    slot = playing_or_recording_clip_slot(track)
    if liveobj_valid(slot):
        if not slot.is_recording:
            return slot
        return None
    return None


def recording_clip_slot(track):
    slot = playing_or_recording_clip_slot(track)
    if liveobj_valid(slot):
        if slot.is_recording:
            return slot
        return None
    return None


playing_or_recording_clip = compose(clip_of_slot, playing_or_recording_clip_slot)
playing_clip = compose(clip_of_slot, playing_clip_slot)
recording_clip = compose(clip_of_slot, recording_clip_slot)


@depends(song=(const(None)))
def get_or_create_first_empty_clip_slot(track, song=None):
    if liveobj_valid(track):
        first_empty_slot = find_if(lambda s: not s.has_clip, track.clip_slots)
        if first_empty_slot:
            if liveobj_valid(first_empty_slot):
                return first_empty_slot
        try:
            song.create_scene(-1)
            slot = track.clip_slots[-1]
            if liveobj_valid(slot):
                return slot
        except Live.Base.LimitationError:
            pass
    return None


def last_slot_with_clip(track):
    return find_if(has_clip, reversed(clip_slots(track)))


def clip_slots(track):
    if liveobj_valid(track):
        return track.clip_slots
    return []


def is_playing(track):
    if liveobj_valid(track):
        return track.playing_slot_index >= 0
    return None


def is_group_track(track):
    if liveobj_valid(track):
        return track.is_foldable
    return None


def is_grouped(track):
    if liveobj_valid(track):
        return track.is_grouped
    return None


def group_track(track):
    if is_grouped(track):
        return track.group_track
    return None


def flatten_tracks(tracks):
    return chain(*(grouped_tracks(t) if is_group_track(t) else [t] for t in tracks))


@depends(song=(const(None)))
def grouped_tracks(track, song=None):
    if not is_group_track(track):
        return []
    return flatten_tracks(filter(lambda t: group_track(t) == track, song.tracks))


def toggle_fold(track):
    if is_group_track(track):
        track.fold_state = not track.fold_state
        return True
    return False


def is_folded(track):
    if is_group_track(track):
        return track.fold_state
    return None


def has_clips(track):
    if is_group_track(track):
        return any(map(has_clips, grouped_tracks(track)))
    return any(map(has_clip, clip_slots(track)))


def can_be_armed(track):
    if liveobj_valid(track):
        return track.can_be_armed
    return None


def arm(track):
    if can_be_armed(track):
        track.arm = True
        return True
    return False


def unarm(track):
    if can_be_armed(track):
        track.arm = False
        return True
    return False


def stop_all_clips(track, quantized=True):
    if liveobj_valid(track):
        track.stop_all_clips(quantized)
        return True
    return False


def unarm_tracks(tracks):
    for track in tracks:
        unarm(track)


def tracks(song):
    return filter(liveobj_valid, song.tracks)


def visible_tracks(song):
    return filter(liveobj_valid, song.visible_tracks)

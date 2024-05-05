# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/mixable_utilities.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 981 bytes
import Live
from ableton.v2.base import old_hasattr
from ableton.v2.control_surface import find_instrument_meeting_requirement


def is_chain(track_or_chain):
    return isinstance(getattr(track_or_chain, "proxied_object", track_or_chain), Live.Chain.Chain)


def is_midi_track(track):
    return getattr(track, "has_midi_input", False) and not is_chain(track)


def is_audio_track(track):
    return getattr(track, "has_audio_input", False) and not is_chain(track)


def can_play_clips(mixable):
    return old_hasattr(mixable, "fired_slot_index")


def find_drum_rack_instrument(track):
    return find_instrument_meeting_requirement(lambda i: i.can_have_drum_pads, track)


def find_simpler(track_or_chain):
    return find_instrument_meeting_requirement(lambda i: old_hasattr(i, "playback_mode"), track_or_chain)
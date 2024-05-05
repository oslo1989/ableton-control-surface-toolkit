# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/pushbase/song_utils.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 937 bytes
import Live
from ableton.v2.base import liveobj_valid


def is_return_track(song, track):
    return track in list(song.return_tracks)


def delete_track_or_return_track(song, track):
    tracks = list(song.tracks)
    if track in tracks:
        track_index = tracks.index(track)
        song.delete_track(track_index)
    else:
        track_index = list(song.return_tracks).index(track)
        song.delete_return_track(track_index)


def find_parent_track(live_object):
    track = live_object
    while liveobj_valid(track):
        if not isinstance(track, Live.Track.Track):
            track = getattr(track, "canonical_parent", None)

    return track

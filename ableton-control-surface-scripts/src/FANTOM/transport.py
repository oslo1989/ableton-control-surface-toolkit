# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/FANTOM/transport.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1432 bytes
from ableton.v3.base import listens
from ableton.v3.control_surface.components import TransportComponent as TransportComponentBase

from .control import DisplayControl

MAX_NUM_BARS_WITH_BEATS = 9999


class TransportComponent(TransportComponentBase):
    beat_time_display = DisplayControl()
    tempo_display = DisplayControl()

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._TransportComponent__on_song_time_changed.subject = self.song
        self._TransportComponent__on_tempo_changed.subject = self.song

    def update(self):
        super().update()
        self._TransportComponent__on_song_time_changed()
        self._TransportComponent__on_tempo_changed()

    @listens("current_song_time")
    def __on_song_time_changed(self):
        beat_time = self.song.get_current_beats_song_time()
        bars = beat_time.bars
        if bars <= MAX_NUM_BARS_WITH_BEATS:
            self.beat_time_display.data = f"{bars}.{beat_time.beats}"
        else:
            self.beat_time_display.data = str(bars)

    @listens("tempo")
    def __on_tempo_changed(self):
        tempo = f"{self.song.tempo:.2f}"
        self.tempo_display.data = tempo

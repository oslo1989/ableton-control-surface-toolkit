# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/components/playhead.py
# Compiled at: 2023-12-18 13:26:15
# Size of source mod 2**32: 3810 bytes
from ...base import depends, listens
from ...live import liveobj_valid
from .. import Component
from . import DEFAULT_STEP_TRANSLATION_CHANNEL


class PlayheadComponent(Component):
    @depends(playhead=None, sequencer_clip=None, grid_resolution=None)
    def __init__(
        self,
        name="Playhead",
        playhead=None,
        sequencer_clip=None,
        grid_resolution=None,
        paginator=None,
        notes=None,
        triplet_notes=None,
        channels=None,
        *a,
        **k,
    ):
        (super().__init__)(a, name=name, **k)
        self._notes = notes or tuple(range(8))
        self._triplet_notes = triplet_notes or tuple(range(6))
        self._channels = channels or [DEFAULT_STEP_TRANSLATION_CHANNEL]
        self._playhead = playhead
        self._sequencer_clip = sequencer_clip
        self._grid_resolution = grid_resolution
        self._paginator = paginator
        self.register_slot(self._grid_resolution, self.update, "index")
        self.register_slot(self._paginator, self.update, "page")
        self.register_slot(self.song, self.update, "is_playing")
        self._PlayheadComponent__on_sequencer_clip_playing_status_changed.subject = sequencer_clip
        self._PlayheadComponent__on_sequencer_clip_changed()

    def update(self):
        super().update()
        playhead_clip = None
        sequencer_clip = self._sequencer_clip.clip
        if self.is_enabled():
            if not liveobj_valid(sequencer_clip) or self.song.is_playing:
                if sequencer_clip.is_arrangement_clip or sequencer_clip.is_playing:
                    playhead_clip = sequencer_clip
                self._playhead.clip = playhead_clip
                self._playhead.set_feedback_channels(self._channels)
                if playhead_clip:
                    self._update_playhead_notes()
                    self._playhead.start_time = self._paginator.page_time
                    self._playhead.step_length = self._grid_resolution.step_length

    def _update_playhead_notes(self):
        self._playhead.notes = list(self._triplet_notes if self._grid_resolution.is_triplet else self._notes)

    @listens("clip")
    def __on_sequencer_clip_changed(self):
        self.update()

    @listens("clip.playing_status")
    def __on_sequencer_clip_playing_status_changed(self):
        self.update()

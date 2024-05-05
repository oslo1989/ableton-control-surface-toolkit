# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_Pro/TargetTrackComponent.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 2732 bytes
from _Framework import ControlSurfaceComponent
from _Framework.SubjectSlot import Subject, subject_slot, subject_slot_group


class TargetTrackComponent(ControlSurfaceComponent, Subject):
    __subject_events__ = ("target_track",)

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._target_track = None
        self._armed_track_stack = []
        self._on_tracks_changed.subject = self.song()
        self._on_tracks_changed()

    @property
    def target_track(self):
        return self._target_track

    def on_selected_track_changed(self):
        if not self._armed_track_stack:
            self._set_target_track()

    @subject_slot("tracks")
    def _on_tracks_changed(self):
        tracks = [t for t in self.song().tracks if t.can_be_armed if t.has_midi_input]
        self._on_arm_changed.replace_subjects(tracks)
        self._on_frozen_state_changed.replace_subjects(tracks)
        self._refresh_armed_track_stack(tracks)

    @subject_slot_group("arm")
    def _on_arm_changed(self, track):
        if track in self._armed_track_stack:
            self._armed_track_stack.remove(track)
        if track.arm:
            self._armed_track_stack.append(track)
            self._set_target_track(track)
        else:
            self._set_target_track()

    @subject_slot_group("is_frozen")
    def _on_frozen_state_changed(self, track):
        if track in self._armed_track_stack:
            self._armed_track_stack.remove(track)
        if track == self._target_track:
            self._set_target_track()

    def _set_target_track(self, target=None):
        new_target = self._target_track
        if target is None:
            new_target = self._armed_track_stack[-1] if self._armed_track_stack else self.song().view.selected_track
        else:
            new_target = target
        if self._target_track != new_target:
            self._target_track = new_target
        self.notify_target_track()

    def _refresh_armed_track_stack(self, all_tracks):
        for track in self._armed_track_stack:
            if track not in all_tracks:
                self._armed_track_stack.remove(track)

        for track in all_tracks:
            if track.arm:
                if track not in self._armed_track_stack:
                    self._armed_track_stack.append(track)

        self._set_target_track()

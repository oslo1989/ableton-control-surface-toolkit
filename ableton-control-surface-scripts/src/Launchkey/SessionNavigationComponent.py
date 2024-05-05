# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey/SessionNavigationComponent.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 4362 bytes
from _Framework import CompoundComponent, ScrollComponent, Task
from _Framework.ViewControlComponent import BasicSceneScroller, TrackScroller


def is_recording_clip(tracks, check_arrangement):
    found_recording_clip = False
    for track in tracks:
        if track.can_be_armed:
            if track.arm:
                if check_arrangement:
                    found_recording_clip = True
                    break
                else:
                    playing_slot_index = track.playing_slot_index
                if playing_slot_index in range(len(track.clip_slots)):
                    slot = track.clip_slots[playing_slot_index]
                    if slot.has_clip:
                        if slot.clip.is_recording:
                            found_recording_clip = True
                            break

    return found_recording_clip


class ArmingTrackScrollComponent(ScrollComponent):
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._arming_task = self._tasks.add(Task.sequence(Task.delay(1), self._arm_task))
        self._arming_task.kill()

    def scroll_up(self):
        super().scroll_up()
        self._start_arming_task()

    def scroll_down(self):
        super().scroll_down()
        self._start_arming_task()

    def _start_arming_task(self):
        if self._arming_task.is_killed:
            self._arming_task.restart()

    @property
    def is_scrolling(self):
        return not self._scroll_task_up.is_killed or not self._scroll_task_down.is_killed

    def _track_to_arm(self):
        track = self.song().view.selected_track
        can_arm_track = track is not None and track.has_midi_input and track.can_be_armed and not track.arm
        if can_arm_track:
            return track
        return None

    def _try_arm(self):
        track_to_arm = self._track_to_arm()
        if track_to_arm is not None:
            song = self.song()
            tracks = song.tracks
            check_arrangement = song.is_playing and song.record_mode
            if not is_recording_clip(tracks, check_arrangement):
                if song.exclusive_arm:
                    for track in tracks:
                        if track.can_be_armed:
                            if track != track_to_arm:
                                track.arm = False

                track_to_arm.arm = True
                track_to_arm.view.select_instrument()

    def _arm_task(self, delta):
        result_state = Task.KILLED
        if self.is_enabled():
            if self.is_scrolling:
                result_state = Task.RUNNING
            else:
                self._try_arm()
        return result_state


class SessionNavigationComponent(CompoundComponent):
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._scroll_tracks, self._scroll_scenes = self.register_components(
            ArmingTrackScrollComponent(TrackScroller()),
            ScrollComponent(BasicSceneScroller()),
        )
        song = self.song()
        view = song.view
        self.register_slot(song, self._scroll_tracks.update, "visible_tracks")
        self.register_slot(song, self._scroll_tracks.update, "return_tracks")
        self.register_slot(song, self._scroll_scenes.update, "scenes")
        self.register_slot(view, self._scroll_tracks.update, "selected_track")
        self.register_slot(view, self._scroll_scenes.update, "selected_scene")

    def set_next_track_button(self, button):
        self._scroll_tracks.set_scroll_down_button(button)

    def set_prev_track_button(self, button):
        self._scroll_tracks.set_scroll_up_button(button)

    def set_next_scene_button(self, button):
        self._scroll_scenes.set_scroll_down_button(button)

    def set_prev_scene_button(self, button):
        self._scroll_scenes.set_scroll_up_button(button)

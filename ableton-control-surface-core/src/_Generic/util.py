# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Generic/util.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1644 bytes
from _Framework.SubjectSlot import SlotManager, subject_slot
from _Framework.Util import nop


class DeviceAppointer(SlotManager):
    def __init__(self, song=None, appointed_device_setter=nop, *a, **k):
        (super().__init__)(*a, **k)
        self._set_appointed_device = appointed_device_setter
        self._appointed_device = None
        self._song = song
        self._DeviceAppointer__on_appointed_device_changed.subject = self._song
        self._DeviceAppointer__on_selected_track_changed.subject = self._song.view
        self._DeviceAppointer__on_selected_track_changed()

    @subject_slot("appointed_device")
    def __on_appointed_device_changed(self):
        if self._appointed_device != self._song.appointed_device:
            self._update_appointed_device(self._song.appointed_device)

    @subject_slot("selected_device")
    def __on_selected_device_changed(self):
        song = self._song
        device = song.view.selected_track.view.selected_device
        if device is not None:
            self._update_appointed_device(device)

    @subject_slot("selected_track")
    def __on_selected_track_changed(self):
        track_view = self._song.view.selected_track.view
        self._DeviceAppointer__on_selected_device_changed.subject = track_view
        self._update_appointed_device(track_view.selected_device)

    def _update_appointed_device(self, device):
        if device is not None:
            self._appointed_device = device
            self._set_appointed_device(device)
            self._song.appointed_device = device

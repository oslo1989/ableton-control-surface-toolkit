# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_Essential_mk3/mixer.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1893 bytes
from ableton.v3.base import listens, nop
from ableton.v3.control_surface.components import MixerComponent as MixerComponentBase
from ableton.v3.control_surface.components import SessionRingComponent
from ableton.v3.control_surface.controls import ButtonControl


class MixerComponent(MixerComponentBase):
    bank_toggle_button = ButtonControl()

    def __init__(self, *a, **k):
        self._session_ring = SessionRingComponent(
            name="Mixer_Session_Ring",
            num_tracks=8,
            set_session_highlight=nop,
            snap_track_offset=True,
            is_private=True,
        )
        (super().__init__)(a, session_ring=self._session_ring, **k)
        self.add_children(self._session_ring)
        self._MixerComponent__on_tracks_changed.subject = self._session_ring
        self._MixerComponent__on_tracks_changed()

    def set_bank_toggle_button(self, button):
        self.bank_toggle_button.set_control_element(button)

    @bank_toggle_button.pressed
    def bank_toggle_button(self, _):
        self._session_ring.track_offset = 8 if self._session_ring.track_offset == 0 else 0

    @listens("tracks")
    def __on_tracks_changed(self):
        self.bank_toggle_button.enabled = len(self._session_ring.tracks_to_use()) > 8
        self.bank_toggle_button.color = "Banking.PageOne" if self._session_ring.track_offset == 0 else "Banking.PageTwo"

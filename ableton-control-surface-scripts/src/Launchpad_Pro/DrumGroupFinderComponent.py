# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchpad_Pro/DrumGroupFinderComponent.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 3300 bytes
from itertools import chain

import Live
from _Framework import ControlSurfaceComponent
from _Framework.SubjectSlot import Subject, subject_slot, subject_slot_group
from _Framework.Util import find_if


class DrumGroupFinderComponent(ControlSurfaceComponent, Subject):
    __subject_events__ = ("drum_group",)
    _drum_group = None

    def __init__(self, target_track_component, layer=None, is_enabled=True, *a, **k):
        (super().__init__)(*a, **k)
        self._target_track_component = target_track_component
        self._on_track_changed.subject = self._target_track_component
        self.update()

    @property
    def drum_group(self):
        return self._drum_group

    @property
    def root(self):
        return self._target_track_component.target_track

    @subject_slot_group("devices")
    def _on_devices_changed(self, chain):
        self.update()

    @subject_slot_group("chains")
    def _on_chains_changed(self, chain):
        self.update()

    @subject_slot("target_track")
    def _on_track_changed(self):
        self.update()

    def update(self):
        super().update()
        if self.is_enabled():
            self._update_listeners()
            self._update_drum_group()

    def _update_listeners(self):
        root = self.root
        devices = list(find_instrument_devices(root))
        chains = list(chain([root], *[d.chains for d in devices]))
        self._on_chains_changed.replace_subjects(devices)
        self._on_devices_changed.replace_subjects(chains)

    def _update_drum_group(self):
        drum_group = find_drum_group_device(self.root)
        if type(drum_group) != type(self._drum_group) or drum_group != self._drum_group:
            self._drum_group = drum_group
        self.notify_drum_group()


def find_instrument_devices(track_or_chain):
    instrument = find_if(lambda d: d.type == Live.Device.DeviceType.instrument, track_or_chain.devices)
    if instrument:
        if not instrument.can_have_drum_pads:
            if instrument.can_have_chains:
                return chain([instrument], *map(find_instrument_devices, instrument.chains))
        return []
    return None


def find_drum_group_device(track_or_chain):
    instrument = find_if(lambda d: d.type == Live.Device.DeviceType.instrument, track_or_chain.devices)
    if instrument:
        if instrument.can_have_drum_pads:
            return instrument
        if instrument.can_have_chains:
            return find_if(bool, map(find_drum_group_device, instrument.chains))
        return None
    return None

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/base/disconnectable.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 2483 bytes
from .util import find_if


class Disconnectable:
    def disconnect(self):
        pass


class CompoundDisconnectable(Disconnectable):
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._registered_disconnectables = []

    def register_disconnectables(self, disconnectables):
        for disconnectable in disconnectables:
            self.register_disconnectable(disconnectable)

        return disconnectables

    def register_disconnectable(self, slot):
        if slot not in self._registered_disconnectables:
            self._registered_disconnectables.append(slot)
        return slot

    def unregister_disconnectable(self, slot):
        if slot in self._registered_disconnectables:
            self._registered_disconnectables.remove(slot)

    def disconnect_disconnectable(self, slot):
        if slot in self._registered_disconnectables:
            self._registered_disconnectables.remove(slot)
            slot.disconnect()

    def find_disconnectable(self, predicate):
        return find_if(predicate, self._registered_disconnectables)

    def has_disconnectable(self, slot):
        return slot in self._registered_disconnectables

    def disconnect(self):
        for slot in self._registered_disconnectables:
            slot.disconnect()

        self._registered_disconnectables = []
        super().disconnect()


class disconnectable:
    def __init__(self, managed=None, *a, **k):
        (super().__init__)(*a, **k)
        self._managed = managed

    def __enter__(self):
        return self._managed

    def __exit__(self, *a, **k):
        if self._managed is not None:
            self._managed.disconnect()

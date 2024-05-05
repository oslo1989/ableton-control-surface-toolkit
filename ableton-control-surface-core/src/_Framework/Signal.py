# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Framework/Signal.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 3054 bytes
from functools import partial

from .Util import find_if, nop


def default_combiner(results):
    for _ in results:
        pass


class Slot:
    def __init__(self, callback=None, *a, **k):
        (super().__init__)(*a, **k)
        self.callback = callback

    def __call__(self, *a, **k):
        return (self.callback)(*a, **k)

    def __eq__(self, other):
        return id(self) == id(other) or self.callback == other


class IdentifyingSlot(Slot):
    def __init__(self, sender=None, *a, **k):
        (super().__init__)(*a, **k)
        self.sender = sender

    def __call__(self, *a, **k):
        (self.callback)(*(*a, self.sender), **k)


class Signal:
    def __init__(self, combiner=default_combiner, sender=None, *a, **k):
        (super().__init__)(*a, **k)
        self._slots = []
        self._combiner = combiner

    def connect(self, slot, in_front=False, sender=None):
        if slot not in self._slots:
            slot = IdentifyingSlot(sender, slot) if sender is not None else Slot(slot)
            if in_front:
                self._slots.insert(0, slot)
            else:
                self._slots.append(slot)
        else:
            slot = find_if(lambda x: x == slot, self._slots)
        return slot

    def disconnect(self, slot):
        if slot in self._slots:
            self._slots.remove(slot)

    def disconnect_all(self):
        self._slots = []

    @property
    def count(self):
        return len(self._slots)

    def is_connected(self, slot):
        return slot in self._slots

    def __call__(self, *a, **k):
        return self._combiner(_slot_notification_generator(self._slots, a, k))


def _slot_notification_generator(slots, args, kws):
    for slot in slots:
        yield slot(*args, **kws)


def short_circuit_combiner(slot_results):
    return find_if(nop, slot_results)


short_circuit_signal = partial(Signal, short_circuit_combiner)

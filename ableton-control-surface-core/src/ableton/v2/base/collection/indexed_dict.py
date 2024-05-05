# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/base/collection/indexed_dict.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1562 bytes
from collections import OrderedDict


class IndexedDict(OrderedDict):
    def __init__(self, *args, **kwds):
        self._IndexedDict__keys = []
        (super().__init__)(*args, **kwds)

    def __setitem__(self, key, value, *args, **kwds):
        (super().__setitem__)(key, value, *args, **kwds)
        if key not in self._IndexedDict__keys:
            self._IndexedDict__keys.append(key)

    def __delitem__(self, key, *args, **kwds):
        (super().__delitem__)(key, *args, **kwds)
        self._IndexedDict__keys.remove(key)

    def clear(self):
        super().clear()
        self._IndexedDict__keys = []

    def popitem(self, last=True):
        item = super().popitem(last)
        self._IndexedDict__keys.pop(-1 if last else 0)
        return item

    def keys(self):
        return self._IndexedDict__keys

    def item_by_index(self, ix):
        key = self._IndexedDict__keys[ix]
        return (key, self[key])

    def key_by_index(self, ix):
        return self._IndexedDict__keys[ix]

    def value_by_index(self, ix):
        return self[self._IndexedDict__keys[ix]]

    def index_by_key(self, key):
        return self._IndexedDict__keys.index(key)

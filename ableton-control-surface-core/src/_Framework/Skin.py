# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Framework/Skin.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1389 bytes
from itertools import chain

from future.utils import raise_


class SkinColorMissingError(Exception):
    pass


class Skin:
    def __init__(self, colors=None, *a, **k):
        (super().__init__)(*a, **k)
        self._colors = {}
        if colors is not None:
            self._fill_colors(colors)

    def _fill_colors(self, colors, pathname=""):
        if getattr(colors, "__bases__", None):
            for base in colors.__bases__:
                self._fill_colors(base)

        for k, v in colors.__dict__.items():
            if k[:1] != "_":
                if callable(v):
                    self._fill_colors(v, pathname + k + ".")
                else:
                    self._colors[pathname + k] = v

    def __getitem__(self, key):
        try:
            return self._colors[key]
        except KeyError:
            raise_(SkinColorMissingError, "Skin color missing: %s" % str(key))

    def iteritems(self):
        return iter(self._colors.items())


def merge_skins(*skins):
    skin = Skin()
    skin._colors = dict(chain(*[list(s._colors.items()) for s in skins]))
    return skin

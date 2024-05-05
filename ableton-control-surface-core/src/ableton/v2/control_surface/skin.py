# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/skin.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 2497 bytes
from itertools import chain

from future.utils import iteritems

from ableton.v2.base import EventObject, const, depends, liveobj_valid
from ableton.v2.control_surface.elements.color import is_dynamic_color_factory


class SkinColorMissingError(Exception):
    pass


class DynamicColorNotAvailableError(Exception):
    msg = "In order to use dynamic colors, you need to inject the song while creating         the skin"


class Skin(EventObject):
    @depends(song=(const(None)))
    def __init__(self, colors=None, song=None, *a, **k):
        (super().__init__)(*a, **k)
        self._colors = {}
        self._factory_to_instance_map = {}
        if colors is not None:
            self._fill_colors(colors, song=song)

    def _fill_colors(self, colors, pathname="", song=None):
        if getattr(colors, "__bases__", None):
            for base in colors.__bases__:
                self._fill_colors(base, song=song, pathname=pathname)

        for k, v in iteritems(colors.__dict__):
            if k[:1] != "_":
                if callable(v):
                    self._fill_colors(v, (pathname + k + "."), song=song)
                else:
                    if is_dynamic_color_factory(v):
                        v = self._get_dynamic_color(v, song)
                    self._colors[pathname + k] = v

    def __getitem__(self, key):
        try:
            return self._colors[key]
        except KeyError:
            raise SkinColorMissingError("Skin color missing: %s" % str(key))

    def iteritems(self):
        return iteritems(self._colors)

    def _get_dynamic_color(self, color_factory, song):
        if not liveobj_valid(song):
            raise DynamicColorNotAvailableError
        else:
            if color_factory not in self._factory_to_instance_map:
                self._factory_to_instance_map[color_factory] = self._create_dynamic_color(color_factory, song)
            return self._factory_to_instance_map[color_factory]

    def _create_dynamic_color(self, color_factory, song):
        return self.register_disconnectable(color_factory.instantiate(song))


def merge_skins(*skins):
    skin = Skin()
    skin._colors = dict(chain(*(s._colors.items() for s in skins)))
    return skin

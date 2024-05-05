# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/base/gcutil.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1837 bytes
import contextlib
import gc
from collections import defaultdict

from future.builtins import range

from .util import old_hasattr


def typename(obj):
    if old_hasattr(obj, "__class__"):
        return obj.__class__.__name__
    if old_hasattr(obj, "__name__"):
        return obj.__name__
    return "<unknown>"


def histogram(name_filter=None, objs=None):
    all_ = gc.get_objects() if objs is None else objs

    def _name_filter(name):
        return name_filter is None or name_filter in name

    hist = defaultdict(
        lambda: 0,
    )
    for o in all_:
        n = typename(o)
        if _name_filter(n):
            hist[n] += 1

    return hist


def instances_by_name(name_filter):
    return [o for o in gc.get_objects() if name_filter == typename(o)]


def refget(objs, level=1):
    for _ in range(level):
        refs = (gc.get_referrers)(*objs)
        with contextlib.suppress(ValueError):
            refs.remove(objs)

        objs = refs

    return refs

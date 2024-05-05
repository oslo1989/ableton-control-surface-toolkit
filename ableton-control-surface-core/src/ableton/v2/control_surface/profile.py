# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/profile.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1775 bytes
from functools import partial, wraps

ENABLE_PROFILING = False
if ENABLE_PROFILING:
    import cProfile

    PROFILER = cProfile.Profile()


def profile(fn):
    if ENABLE_PROFILING:

        @wraps(fn)
        def wrapper(self, *a, **k):
            if PROFILER:
                return PROFILER.runcall(partial(fn, self, *a, **k))
            print(f"Can not profile ({fn.__name__}), it is probably reloaded")
            return fn(*a, **k)

        return wrapper
    return fn


def dump(name="default"):
    import pstats

    fname = name + ".profile"
    PROFILER.dump_stats(fname)

    def save_human_data(sort):
        s = pstats.Stats(fname, stream=(open(f"{fname}.{sort}.txt", "w")))
        s.sort_stats(sort)
        s.print_stats()

    save_human_data("time")
    save_human_data("cumulative")

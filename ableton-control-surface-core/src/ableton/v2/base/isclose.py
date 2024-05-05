# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/base/isclose.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 2204 bytes
import math


def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    if a == b:
        return True
    if rel_tol < 0.0 or abs_tol < 0.0:
        raise ValueError("error tolerances must be non-negative")
    if math.isinf(abs(a)) or math.isinf(abs(b)):
        return False
    diff = abs(b - a)
    return diff <= abs(rel_tol * b) or diff <= abs(rel_tol * a) or diff <= abs_tol

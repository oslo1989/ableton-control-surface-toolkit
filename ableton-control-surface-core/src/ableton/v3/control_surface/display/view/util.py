# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/display/view/util.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 542 bytes
from typing import List, Optional

from ..state import State


def suppress_notifications(state: State, exclude: Optional[List[str]] = None):
    if exclude is None:
        exclude = []
    for notification in getattr(state, "_notifications", set()) - set(exclude):
        setattr(state, notification, None)

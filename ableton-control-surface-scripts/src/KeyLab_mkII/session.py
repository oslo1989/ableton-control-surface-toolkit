# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_mkII/session.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 514 bytes
from KeyLab_Essential.session import SceneComponent as SceneComponentBase
from KeyLab_Essential.session import SessionComponent as SessionComponentBase

from .clip_slot import ClipSlotComponent


class SceneComponent(SceneComponentBase):
    clip_slot_component_type = ClipSlotComponent


class SessionComponent(SessionComponentBase):
    scene_component_type = SceneComponent

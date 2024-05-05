# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_MK2/ControlElementUtils.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1372 bytes
import Live
from _Framework import ButtonElement, EncoderElement, SliderElement
from _Framework.Dependency import depends
from _Framework.InputControlElement import MIDI_CC_TYPE, MIDI_NOTE_TYPE
from _Framework.Resource import PrioritizedResource

from .consts import STANDARD_CHANNEL


@depends(skin=None)
def make_button(identifier, msg_type=MIDI_NOTE_TYPE, is_momentary=True, skin=None, is_modifier=False, name=""):
    return ButtonElement(
        is_momentary,
        msg_type,
        STANDARD_CHANNEL,
        identifier,
        skin=skin,
        name=name,
        resource_type=(PrioritizedResource if is_modifier else None),
    )


def make_encoder(identifier, name=""):
    return EncoderElement(MIDI_CC_TYPE, STANDARD_CHANNEL, identifier, (Live.MidiMap.MapMode.absolute), name=name)


def make_slider(identifier, name="", channel=STANDARD_CHANNEL):
    return SliderElement(MIDI_CC_TYPE, channel, identifier, name=name)

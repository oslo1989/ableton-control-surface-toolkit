# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/AIRA_MX_1/ControlElementUtils.py
# Compiled at: 2023-12-21 15:36:02
# Size of source mod 2**32: 1170 bytes
import Live
from _Framework import ButtonElement, ComboElement, EncoderElement
from _Framework.Dependency import depends
from _Framework.InputControlElement import MIDI_CC_TYPE, MIDI_NOTE_TYPE
from _Framework.Resource import PrioritizedResource


@depends(skin=None)
def make_button(name, identifier, channel=0, msg_type=MIDI_NOTE_TYPE, is_momentary=True, is_modifier=False, skin=None):
    return ButtonElement(
        is_momentary,
        msg_type,
        channel,
        identifier,
        name=name,
        resource_type=(PrioritizedResource if is_modifier else None),
        skin=skin,
    )


def make_encoder(name, identifier, channel=0):
    return EncoderElement(MIDI_CC_TYPE, channel, identifier, (Live.MidiMap.MapMode.absolute), name=name)


def with_modifier(control, modifier):
    return ComboElement(control, modifiers=[modifier], name=(control.name + "_With_Modifier"))

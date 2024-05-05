# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_MPDMkIIBase/ControlElementUtils.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 763 bytes
import Live
from _Framework import ButtonElement, EncoderElement, SliderElement
from _Framework.InputControlElement import MIDI_CC_TYPE


def make_encoder(identifier, channel, name):
    return EncoderElement(MIDI_CC_TYPE, channel, identifier, (Live.MidiMap.MapMode.absolute), name=name)


def make_slider(identifier, channel, name):
    return SliderElement(MIDI_CC_TYPE, channel, identifier, name=name)


def make_button(identifier, channel, name):
    return ButtonElement(True, MIDI_CC_TYPE, channel, identifier, name=name)

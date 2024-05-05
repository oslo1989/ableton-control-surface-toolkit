# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/MIDI_Mix/ControlElementUtils.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1154 bytes
import Live
from _Framework import ButtonElement, ButtonMatrixElement, EncoderElement, SliderElement
from _Framework.Dependency import depends
from _Framework.InputControlElement import MIDI_CC_TYPE, MIDI_NOTE_TYPE


@depends(skin=None)
def make_button(identifier, name, skin=None):
    return ButtonElement(True, MIDI_NOTE_TYPE, 0, identifier, name=name, skin=skin)


def make_slider(identifier, name):
    return SliderElement(MIDI_CC_TYPE, 0, identifier, name=name)


def make_encoder(identifier, name):
    return EncoderElement(MIDI_CC_TYPE, 0, identifier, map_mode=(Live.MidiMap.MapMode.absolute), name=name)


def make_button_row(identifier_sequence, element_factory, name):
    return ButtonMatrixElement(
        rows=[
            [element_factory(identifier, name + "_%d" % index)] for index, identifier in enumerate(identifier_sequence)
        ],
    )

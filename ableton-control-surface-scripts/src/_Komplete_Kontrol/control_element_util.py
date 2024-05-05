# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Komplete_Kontrol/control_element_util.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1521 bytes
import Live
from ableton.v2.control_surface import MIDI_CC_TYPE, midi
from ableton.v2.control_surface.elements import ButtonElement, EncoderElement, SliderElement, SysexElement

from .physical_display_element import PhysicalDisplayElement
from .skin import skin

MIDI_CHANNEL = 15


def create_button(identifier, name):
    return ButtonElement(False, MIDI_CC_TYPE, MIDI_CHANNEL, identifier, name=name, skin=skin)


def create_encoder(identifier, name, is_s_mk2=False):
    encoder = EncoderElement(
        MIDI_CC_TYPE,
        MIDI_CHANNEL,
        identifier,
        (Live.MidiMap.MapMode.relative_smooth_two_compliment),
        name=name,
        encoder_sensitivity=1.0,
    )
    if is_s_mk2:
        encoder.set_feedback_delay(-1)
        encoder.mapping_sensitivity = 0.1
    return encoder


def create_slider_element(identifier, name):
    return SliderElement(MIDI_CC_TYPE, MIDI_CHANNEL, identifier, name=name)


def create_display_line(header, line_index, name, width=0):
    line = PhysicalDisplayElement(width_in_chars=width, name=name)
    line.set_message_parts((*header, line_index), (midi.SYSEX_END,))
    return line


def create_sysex_element(header, index, name):
    return SysexElement(
        (lambda value: (*header, value, index, midi.SYSEX_END)),
        default_value=0,
        optimized=True,
        name=name,
    )

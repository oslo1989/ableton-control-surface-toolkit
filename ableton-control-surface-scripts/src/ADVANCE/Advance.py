# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ADVANCE/Advance.py
# Compiled at: 2023-11-21 10:21:17
# Size of source mod 2**32: 2844 bytes
import Live
from _Framework import (
    ButtonElement,
    ButtonMatrixElement,
    ControlSurface,
    DeviceComponent,
    DrumRackComponent,
    EncoderElement,
    Layer,
    TransportComponent,
)
from _Framework.InputControlElement import MIDI_CC_TYPE, MIDI_NOTE_TYPE

PAD_CHANNEL = 1
PAD_IDS = ((81, 83, 84, 86), (74, 76, 77, 79), (67, 69, 71, 72), (60, 62, 64, 65))


def make_encoder(identifier, name):
    return EncoderElement(MIDI_CC_TYPE, 0, identifier, (Live.MidiMap.MapMode.absolute), name=name)


def make_button(identifier, name, msg_type=MIDI_NOTE_TYPE, channel=PAD_CHANNEL):
    return ButtonElement(True, msg_type, channel, identifier, name=name)


class Advance(ControlSurface):
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        with self.component_guard():
            encoders = ButtonMatrixElement(
                rows=[[make_encoder(index + 22, "Encoder_%d" % index) for index in range(8)]],
            )
            pads = ButtonMatrixElement(
                rows=[
                    [make_button(identifier, "Pad_%d_%d" % (col, row)) for col, identifier in enumerate(row_ids)]
                    for row, row_ids in enumerate(PAD_IDS)
                ],
            )
            device = DeviceComponent(
                is_enabled=False,
                layer=Layer(parameter_controls=encoders),
                device_selection_follows_track_selection=True,
            )
            device.set_enabled(True)
            self.set_device_component(device)
            drums = DrumRackComponent(is_enabled=False, layer=Layer(pads=pads))
            drums.set_enabled(True)
            play_button = make_button(118, "Play_Button", MIDI_CC_TYPE, 0)
            stop_button = make_button(117, "Stop_Button", MIDI_CC_TYPE, 0)
            record_button = make_button(119, "Record_Button", MIDI_CC_TYPE, 0)
            loop_button = make_button(114, "Loop_Button", MIDI_CC_TYPE, 0)
            transport = TransportComponent(
                is_enabled=False,
                layer=Layer(
                    play_button=play_button,
                    stop_button=stop_button,
                    record_button=record_button,
                    loop_button=loop_button,
                ),
            )
            transport.set_enabled(True)

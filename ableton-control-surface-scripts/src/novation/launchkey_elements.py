# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/novation/launchkey_elements.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 3761 bytes
import Live
from ableton.v2.base import depends
from ableton.v2.control_surface import MIDI_CC_TYPE, MIDI_NOTE_TYPE, PrioritizedResource
from ableton.v2.control_surface.elements import ButtonElement, ButtonMatrixElement, ComboElement, EncoderElement

SESSION_WIDTH = 8
SESSION_HEIGHT = 2
DRUM_CHANNEL = 9


@depends(skin=None)
def create_button(identifier, name, msg_type=MIDI_CC_TYPE, channel=15, **k):
    return ButtonElement(True, msg_type, channel, identifier, name=name, **k)


def create_encoder(identifier, name, **k):
    return EncoderElement(MIDI_CC_TYPE, 15, identifier, Live.MidiMap.MapMode.absolute, name=name, **k)


class LaunchkeyElements:
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self.right_button = create_button(102, "Right_Button")
        self.left_button = create_button(103, "Left_Button")
        self.shift_button = create_button(108, "Shift_Button", resource_type=PrioritizedResource, channel=0)
        self.play_button = create_button(115, "Play_Button")
        self.record_button = create_button(117, "Record_Button")
        self.play_button_with_shift = self.with_shift(self.play_button)
        self.scene_launch_buttons_raw = [
            create_button(104, "Scene_Launch_Button", channel=0),
            create_button(105, "Stop_Solo_Mute_Button", channel=0),
        ]
        self.scene_launch_buttons = ButtonMatrixElement(
            rows=[self.scene_launch_buttons_raw],
            name="Scene_Launch_Buttons",
        )
        self.clip_launch_matrix = ButtonMatrixElement(
            rows=[
                [
                    create_button(
                        (offset + col_index),
                        (f"{col_index}_Clip_Launch_Button_{row_index}"),
                        msg_type=MIDI_NOTE_TYPE,
                        channel=0,
                    )
                    for col_index in range(SESSION_WIDTH)
                ]
                for row_index, offset in enumerate(range(96, 119, 16))
            ],
            name="Clip_Launch_Matrix",
        )
        drum_pad_rows = ((48, 49, 50, 51), (44, 45, 46, 47), (40, 41, 42, 43), (36, 37, 38, 39))
        self.drum_pads = ButtonMatrixElement(
            rows=[
                [
                    create_button(
                        (row_identifiers[col_index]),
                        (f"Drum_Pad_{col_index}_{row_index}"),
                        msg_type=MIDI_NOTE_TYPE,
                        channel=DRUM_CHANNEL,
                    )
                    for col_index in range(4)
                ]
                for row_index, row_identifiers in enumerate(drum_pad_rows)
            ],
            name="Drum_Pads",
        )
        self.pots = ButtonMatrixElement(
            rows=[[create_encoder(index + 21, f"Pot_{index}") for index in range(SESSION_WIDTH)]],
            name="Pots",
        )
        self.incontrol_mode_switch = create_button(12, "InControl_Mode_Switch", msg_type=MIDI_NOTE_TYPE)
        self.pad_layout_switch = create_button(3, "Pad_Layout_Switch")
        self.pot_layout_switch = create_button(9, "Pot_Layout_Switch")

    def with_shift(self, button):
        return ComboElement(control=button, modifier=(self.shift_button), name=(f"{button.name}_With_Shift"))

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ATOM/mappings.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 4794 bytes
from ableton.v3.control_surface import LOW_PRIORITY
from ableton.v3.control_surface.mode import LatchingBehaviour, MomentaryBehaviour


def create_mappings(control_surface):
    mappings = {}
    mappings["Modifier_Background"] = {"shift": "shift_button"}
    mappings["Undo_Redo"] = {"undo_button": "stop_button_with_shift"}
    mappings["View_Toggle"] = {
        "detail_view_toggle_button": "show_hide_button",
        "main_view_toggle_button": "preset_button",
    }
    mappings["View_Based_Recording"] = {"record_button": "record_button"}
    mappings["Transport"] = {
        "play_button": "play_button",
        "loop_button": "play_button_with_shift",
        "stop_button": "stop_button",
        "metronome_button": "click_button",
    }
    mappings["Session_Navigation_Modes"] = {
        "cycle_mode_button": "bank_button",
        "default": {
            "component": "Session_Navigation",
            "up_button": "up_button",
            "down_button": "down_button",
            "left_button": "left_button",
            "right_button": "right_button",
            "priority": LOW_PRIORITY,
        },
        "paged": {
            "component": "Session_Navigation",
            "page_up_button": "up_button",
            "page_down_button": "down_button",
            "page_left_button": "left_button",
            "page_right_button": "right_button",
            "priority": LOW_PRIORITY,
        },
    }
    mappings["Encoder_Modes"] = {
        "volume": {"component": "Mixer", "volume_controls": "encoders"},
        "pan": {"component": "Mixer", "pan_controls": "encoders"},
        "send_a": {"component": "Mixer", "send_a_controls": "encoders"},
        "send_b": {"component": "Mixer", "send_b_controls": "encoders"},
    }
    mappings["Note_Modes"] = {
        "enable": False,
        "drum": {
            "component": "Drum_Group",
            "matrix": "pads",
            "scroll_page_up_button": "up_button",
            "scroll_page_down_button": "down_button",
        },
        "keyboard": {
            "component": "Keyboard",
            "matrix": "pads",
            "scroll_up_button": "up_button",
            "scroll_down_button": "down_button",
        },
    }
    mappings["Pad_Modes"] = {
        "default_behaviour": (LatchingBehaviour()),
        "session_button": "full_level_button",
        "note_button": "note_repeat_button",
        "channel_button": "select_button",
        "encoder_modes_button": "setup_button",
        "session": {
            "modes": [
                {"component": "Background", "unused_pads": "pads_with_shift"},
                {
                    "component": "Session",
                    "clip_launch_buttons": "pads",
                    "scene_launch_buttons": "pads_column_3_with_shift",
                },
                {"component": "Session_Overview", "matrix": "pads_with_zoom"},
                {"component": "Modifier_Background", "zoom": "zoom_button"},
            ],
        },
        "note": {"component": "Note_Modes"},
        "channel": {
            "modes": [
                {
                    "component": "Mixer",
                    "arm_buttons": "pads_row_0",
                    "solo_buttons": "pads_row_1",
                    "track_select_buttons": "pads_row_2",
                },
                {"component": "Session", "stop_track_clip_buttons": "pads_row_3"},
            ],
        },
        "encoder_modes": {
            "component": "Encoder_Modes",
            "volume_button": "pads_raw[0]",
            "pan_button": "pads_raw[1]",
            "send_a_button": "pads_raw[2]",
            "send_b_button": "pads_raw[3]",
            "behaviour": (MomentaryBehaviour()),
        },
    }
    mappings["Top_Level_Modes"] = {
        "support_momentary_mode_cycling": False,
        "cycle_mode_button": "editor_button",
        "default": (control_surface.refresh_state),
        "user": {
            "component": "Translating_Background",
            "note_repeat_button": "note_repeat_button",
            "full_level_button": "full_level_button",
            "bank_button": "bank_button",
            "preset_button": "preset_button",
            "show_hide_button": "show_hide_button",
            "nudge_button": "nudge_button",
            "set_loop_button": "set_loop_button",
            "setup_button": "setup_button",
            "up_button": "up_button",
            "down_button": "down_button",
            "left_button": "left_button",
            "right_button": "right_button",
            "select_button": "select_button",
            "click_button": "click_button",
            "record_button": "record_button",
            "play_button": "play_button",
            "stop_button": "stop_button",
            "pads": "pads",
            "encoders": "encoders",
        },
    }
    return mappings

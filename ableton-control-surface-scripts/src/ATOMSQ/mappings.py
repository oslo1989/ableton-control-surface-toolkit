# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ATOMSQ/mappings.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 4200 bytes
from ableton.v3.control_surface.mode import LatchingBehaviour


def create_mappings(_):
    mappings = {}
    mappings["Modifier_Background"] = {"shift": "shift_button"}
    mappings["Undo_Redo"] = {"undo_button": "stop_button_with_shift"}
    mappings["Session_Navigation"] = {"up_button": "up_button_with_shift", "down_button": "down_button_with_shift"}
    mappings["View_Control"] = {
        "next_track_button": "right_button",
        "prev_track_button": "left_button",
        "next_scene_button": "down_button",
        "prev_scene_button": "up_button",
    }
    mappings["View_Based_Recording"] = {"record_button": "record_button"}
    mappings["Transport"] = {
        "arrangement_position_encoder": "display_encoder",
        "tempo_coarse_encoder": "display_encoder_with_shift",
        "play_button": "play_button",
        "loop_button": "play_button_with_shift",
        "stop_button": "stop_button",
        "metronome_button": "click_button",
        "capture_midi_button": "record_button_with_shift",
        "prev_cue_button": "display_left_button",
        "next_cue_button": "display_right_button",
    }
    mappings["Lower_Pad_Modes"] = {
        "enable": False,
        "cycle_mode_button": "minus_button",
        "select": {"component": "Mixer", "track_select_buttons": "lower_pads"},
        "stop": {"component": "Session", "stop_track_clip_buttons": "lower_pads"},
    }
    mappings["Main_Modes"] = {
        "default_behaviour": (LatchingBehaviour()),
        "song_button": "song_mode_button",
        "instrument_button": "instrument_mode_button",
        "editor_button": "editor_mode_button",
        "user_button": "user_mode_button",
        "instrument": {"component": "Device", "parameter_controls": "encoders"},
        "song": {
            "modes": [
                {"component": "Lower_Pad_Modes"},
                {
                    "component": "View_Toggle",
                    "main_view_toggle_button": "bank_a_button",
                    "browser_view_toggle_button": "bank_b_button",
                    "detail_view_toggle_button": "bank_d_button",
                    "clip_view_toggle_button": "bank_h_button",
                },
                {
                    "component": "Launch_And_Stop",
                    "clip_launch_button": "display_buttons_raw[3]",
                    "scene_launch_button": "display_buttons_raw[4]",
                    "track_stop_button": "display_buttons_raw[5]",
                },
                {"component": "Session", "clip_launch_buttons": "upper_pads", "scene_0_launch_button": "plus_button"},
                {
                    "component": "Mixer",
                    "target_track_volume_control": "encoders_raw[0]",
                    "target_track_pan_control": "encoders_raw[1]",
                    "target_track_send_controls": "encoders_2_thru_7",
                    "target_track_solo_button": "display_buttons_raw[0]",
                    "target_track_mute_button": "display_buttons_raw[1]",
                    "target_track_arm_button": "display_buttons_raw[2]",
                    "crossfader_control": "touch_strip",
                },
            ],
        },
        "editor": {
            "modes": [
                {"component": "Device", "parameter_controls": "encoders"},
                {
                    "component": "Device_Navigation",
                    "prev_button": "display_buttons_raw[1]",
                    "next_button": "display_buttons_raw[2]",
                },
                {
                    "component": "Device",
                    "device_lock_button": "display_buttons_raw[0]",
                    "device_on_off_button": "display_buttons_raw[3]",
                    "prev_bank_button": "display_buttons_raw[4]",
                    "next_bank_button": "display_buttons_raw[5]",
                },
            ],
        },
        "user": {
            "component": "Translating_Background",
            "encoders": "encoders",
            "channel_selection_buttons": "display_buttons",
        },
    }
    return mappings

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/APC64/mappings.py
# Compiled at: 2023-12-18 13:26:15
# Size of source mod 2**32: 8722 bytes
from ableton.v3.control_surface import ACTIVE_PARAMETER_TIMEOUT, LOW_PRIORITY
from ableton.v3.control_surface.mode import LatchingBehaviour, MomentaryBehaviour, make_reenter_behaviour


def create_mappings(control_surface):
    mappings = {}
    mappings["Modifier_Background"] = {"clear_button": "clear_button", "duplicate_button": "duplicate_button"}
    mappings["Settings"] = {"fixed_length_button": "fixed_length_button"}
    mappings["Active_Parameter"] = {"touch_controls": "touch_elements"}
    mappings["Transport"] = {
        "stop_button": "stop_button",
        "tap_tempo_button": "tempo_button",
        "record_quantize_button": "quantize_button",
        "shift_button": "shift_button",
    }
    mappings["Mixer"] = {"shift_button": "shift_button"}
    mappings["Session"] = {
        "select_button": "shift_button",
        "delete_button": "clear_button",
        "duplicate_button": "duplicate_button",
        "scene_launch_buttons": "scene_launch_buttons",
    }
    mappings["View_Control"] = {
        "prev_track_button": "left_button",
        "next_track_button": "right_button",
        "prev_track_page_button": "left_button_with_shift",
        "next_track_page_button": "right_button_with_shift",
    }
    mappings["Render_To_Clip"] = {
        "start_control": "render_to_clip_start_element",
        "data_control": "render_to_clip_data_element",
        "end_control": "render_to_clip_end_element",
    }
    mappings["Touch_Strip_Modes"] = {
        "default_behaviour": (LatchingBehaviour()),
        "device_button": "device_button",
        "volume_button": "volume_button",
        "pan_button": "pan_button",
        "send_button": "send_button",
        "channel_strip_button": "channel_strip_button",
        "off_button": "off_button",
        "device": {
            "modes": [
                {
                    "component": "Device",
                    "parameter_controls": "touch_strips",
                    "prev_bank_button": "up_button_with_device",
                    "next_bank_button": "down_button_with_device",
                    "device_lock_button": "device_button_with_shift",
                },
                {
                    "component": "Device_Navigation",
                    "prev_button": "left_button_with_device",
                    "next_button": "right_button_with_device",
                },
            ],
        },
        "volume": {"component": "Mixer", "volume_controls": "touch_strips"},
        "pan": {"component": "Mixer", "pan_controls": "touch_strips"},
        "send": {
            "component": "Mixer",
            "send_controls": "touch_strips",
            "behaviour": make_reenter_behaviour(
                LatchingBehaviour,
                on_reenter=(control_surface.component_map["Mixer"].cycle_send_index),
            ),
        },
        "channel_strip": {
            "component": "Mixer",
            "target_track_volume_control": "touch_strips_raw[0]",
            "target_track_pan_control": "touch_strips_raw[1]",
            "target_track_send_controls": "touch_strips_2_thru_7",
            "behaviour": make_reenter_behaviour(
                LatchingBehaviour,
                on_reenter=(control_surface.component_map["Mixer"].target_strip.cycle_send_index),
            ),
        },
        "off": None,
    }
    mappings["Encoder_Modes"] = {
        "default_behaviour": MomentaryBehaviour(entry_delay=0.1),
        "tempo_button": "tempo_button",
        "fixed_length_button": "fixed_length_button",
        "swing_button": "tempo_button_with_shift",
        "default": {
            "modes": [
                {"component": "View_Control", "track_encoder": "encoder", "priority": LOW_PRIORITY},
                {"component": "View_Control", "track_page_encoder": "encoder_with_shift"},
                {"component": "Transport", "metronome_button": "encoder_button"},
            ],
        },
        "tempo": {
            "component": "Transport",
            "tempo_coarse_encoder": "encoder",
            "behaviour": MomentaryBehaviour(entry_delay=0, immediate_exit_delay=ACTIVE_PARAMETER_TIMEOUT),
        },
        "fixed_length": {"component": "Settings", "fixed_length_encoder": "encoder"},
        "quantize": {"component": "Settings", "quantization_encoder": "encoder"},
        "swing": {"modes": [], "behaviour": (MomentaryBehaviour())},
    }
    mappings["Track_State_Modes"] = {
        "default_behaviour": (LatchingBehaviour()),
        "mute_button": "mute_button",
        "arm_button": "record_arm_button",
        "solo_button": "solo_button",
        "clip_stop_button": "clip_stop_button",
        "mute": {"component": "Mixer", "mute_buttons": "track_state_buttons"},
        "arm": {"component": "Mixer", "arm_buttons": "track_state_buttons"},
        "solo": {"component": "Mixer", "solo_buttons": "track_state_buttons"},
        "clip_stop": {"component": "Session", "stop_track_clip_buttons": "track_state_buttons"},
    }
    session_navigation = {
        "component": "Session_Navigation",
        "up_button": "up_button",
        "down_button": "down_button",
        "left_button": "left_button",
        "right_button": "right_button",
        "page_up_button": "up_button_with_shift",
        "page_down_button": "down_button_with_shift",
        "page_left_button": "left_button_with_shift",
        "page_right_button": "right_button_with_shift",
    }
    encoder_background = {
        "component": "Background",
        "bg_encoder": "encoder",
        "encoder_with_shift": "encoder_with_shift",
    }
    mappings["Pad_Modes"] = {
        "mode_selection_control": "firmware_mode_element",
        "session": {"modes": [{"component": "Session", "clip_launch_buttons": "pads"}, session_navigation]},
        "session_overview": {"modes": [{"component": "Session_Overview", "matrix": "pads"}, session_navigation.copy()]},
        "note": None,
        "chord": None,
        "note_config": None,
        "drum": {
            "component": "Drum_Group",
            "matrix": "pads",
            "scroll_up_button": "up_button",
            "scroll_down_button": "down_button",
            "scroll_page_up_button": "up_button_with_shift",
            "scroll_page_down_button": "down_button_with_shift",
            "select_button": "shift_button",
            "delete_button": "clear_button",
        },
        "step_seq": encoder_background,
        "step_seq_config": (encoder_background.copy()),
        "project": None,
        "custom": {"component": "Background", "bg_touch_elements": "touch_elements"},
        "globals": None,
    }
    mappings["Global_Modes"] = {
        "shift_button": "shift_button",
        "default": {
            "modes": [
                {"component": "View_Based_Recording", "record_button": "record_button"},
                {"component": "Transport", "play_button": "play_button"},
                {"component": "Undo_Redo", "undo_button": "undo_button"},
                {"component": "Session", "quantize_button": "quantize_button"},
                {"component": "Encoder_Modes", "quantize_button": "quantize_button"},
                {"component": "Mixer", "track_select_buttons": "track_select_buttons"},
            ],
        },
        "shift": {
            "modes": [
                {"component": "View_Based_Recording", "overdub_button": "record_button"},
                {"component": "Transport", "play_pause_button": "play_button"},
                {"component": "Undo_Redo", "redo_button": "undo_button"},
                {"component": "Session", "stop_all_clips_button": "scene_launch_buttons_raw[7]"},
                {"component": "Global_Quantization", "rate_buttons": "track_select_buttons"},
            ],
            "behaviour": (MomentaryBehaviour()),
        },
    }
    return mappings

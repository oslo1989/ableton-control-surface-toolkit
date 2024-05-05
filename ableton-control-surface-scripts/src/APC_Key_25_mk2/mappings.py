# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/APC_Key_25_mk2/mappings.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 3251 bytes
from ableton.v3.control_surface import HIGH_PRIORITY
from ableton.v3.control_surface.mode import ImmediateBehaviour, MomentaryBehaviour, make_reenter_behaviour


def create_mappings(control_surface):
    mappings = {}
    mappings["Transport"] = {"play_toggle_button": "play_button"}
    mappings["Session"] = {
        "clip_launch_buttons": "clip_launch_buttons",
        "stop_all_clips_button": "stop_all_clips_button",
        "clip_slot_select_button": "shift_button",
    }
    mappings["Track_Button_Modes"] = {
        "clip_stop": {"component": "Session", "stop_track_clip_buttons": "track_buttons"},
        "solo": {"component": "Mixer", "solo_buttons": "track_buttons"},
        "mute": {"component": "Mixer", "mute_buttons": "track_buttons"},
        "arm": {"component": "Mixer", "arm_buttons": "track_buttons"},
        "track_select": {"component": "Mixer", "track_select_buttons": "track_buttons"},
    }
    mappings["Encoder_Modes"] = {
        "volume": {"component": "Mixer", "volume_controls": "encoders"},
        "pan": {"component": "Mixer", "pan_controls": "encoders"},
        "send": {
            "component": "Mixer",
            "send_controls": "encoders",
            "behaviour": make_reenter_behaviour(
                ImmediateBehaviour,
                on_reenter=(control_surface.component_map["Mixer"].cycle_send_index),
            ),
        },
        "device": {"component": "Device", "parameter_controls": "encoders"},
    }
    mappings["Main_Modes"] = {
        "shift_button": "shift_button",
        "default": {
            "modes": [
                {"component": "View_Based_Recording", "record_button": "record_button"},
                {"component": "Session", "scene_launch_buttons": "scene_launch_buttons"},
            ],
        },
        "shift": {
            "modes": [
                {"component": "Transport", "capture_midi_button": "record_button"},
                {
                    "component": "Track_Button_Modes",
                    "clip_stop_button": "scene_launch_buttons_raw[0]",
                    "solo_button": "scene_launch_buttons_raw[1]",
                    "mute_button": "scene_launch_buttons_raw[2]",
                    "arm_button": "scene_launch_buttons_raw[3]",
                    "track_select_button": "scene_launch_buttons_raw[4]",
                },
                {
                    "component": "Session_Navigation",
                    "up_button": "track_buttons_raw[0]",
                    "down_button": "track_buttons_raw[1]",
                    "left_button": "track_buttons_raw[2]",
                    "right_button": "track_buttons_raw[3]",
                    "priority": HIGH_PRIORITY,
                },
                {
                    "component": "Encoder_Modes",
                    "volume_button": "track_buttons_raw[4]",
                    "pan_button": "track_buttons_raw[5]",
                    "send_button": "track_buttons_raw[6]",
                    "device_button": "track_buttons_raw[7]",
                    "priority": HIGH_PRIORITY,
                },
            ],
            "behaviour": (MomentaryBehaviour()),
        },
    }
    return mappings

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_Essential_mk3/mappings.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1837 bytes


def create_mappings(_):
    mappings = {}
    mappings["Transport"] = {
        "play_button": "play_button",
        "stop_button": "stop_button",
        "metronome_button": "metronome_button",
        "loop_button": "loop_button",
        "tap_tempo_button": "tap_button",
        "capture_midi_button": "save_button",
        "rewind_button": "rewind_button",
        "fastforward_button": "fastforward_button",
    }
    mappings["View_Based_Recording"] = {"record_button": "record_button"}
    mappings["Undo_Redo"] = {"undo_button": "undo_button", "redo_button": "redo_button"}
    mappings["Clip_Actions"] = {"quantize_button": "punch_button"}
    mappings["View_Control"] = {
        "prev_track_button": "context_button_2",
        "next_track_button": "context_button_3",
        "scene_encoder": "display_encoder",
    }
    mappings["Mixer"] = {
        "target_track_arm_button": "context_button_1",
        "target_track_volume_control": "fader_9",
        "target_track_pan_control": "encoder_9",
    }
    mappings["Session"] = {
        "selected_scene_launch_button": "display_encoder_button",
        "clip_launch_buttons": "pad_bank_a",
    }
    mappings["Drum_Group"] = {"matrix": "pad_bank_b"}
    mappings["Continuous_Control_Modes"] = {
        "support_momentary_mode_cycling": False,
        "cycle_mode_button": "context_button_0",
        "device": {
            "component": "Device",
            "parameter_controls": "continuous_controls",
            "bank_toggle_button": "part_button",
        },
        "mixer": {
            "component": "Mixer",
            "volume_controls": "faders",
            "pan_controls": "encoders",
            "bank_toggle_button": "part_button",
        },
    }
    return mappings

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Keystage/mappings.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 824 bytes


def create_mappings(_):
    mappings = {}
    mappings["Transport"] = {
        "play_button": "play_button",
        "stop_button": "stop_button",
        "loop_button": "loop_button",
        "tap_tempo_button": "tempo_button",
        "metronome_button": "metronome_button",
        "rewind_button": "rewind_button",
        "fastforward_button": "fastforward_button",
    }
    mappings["View_Based_Recording"] = {"record_button": "record_button"}
    mappings["Undo_Redo"] = {"undo_button": "undo_button"}
    mappings["View_Control"] = {"prev_track_button": "up_button", "next_track_button": "down_button"}
    mappings["Device"] = {"parameter_controls": "knobs"}
    return mappings

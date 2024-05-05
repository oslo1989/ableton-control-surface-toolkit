# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/settings.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 689 bytes
from pushbase.setting import OnOffSetting


def create_settings(preferences=None):
    preferences = preferences if preferences is not None else {}
    return {
        "workflow": OnOffSetting(
            name="Workflow",
            value_labels=["Scene", "Clip"],
            default_value=True,
            preferences=preferences,
        ),
        "aftertouch_mode": OnOffSetting(
            name="Pressure",
            value_labels=["Mono", "Polyphonic"],
            default_value=True,
            preferences=preferences,
        ),
    }

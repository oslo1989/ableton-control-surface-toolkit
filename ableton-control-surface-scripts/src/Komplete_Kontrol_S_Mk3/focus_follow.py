# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Komplete_Kontrol_S_Mk3/focus_follow.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1789 bytes
from ableton.v3.control_surface import InstrumentFinderComponent, find_instrument_meeting_requirement
from ableton.v3.control_surface.controls import SendValueControl
from ableton.v3.live import liveobj_valid
from Live import PluginDevice

PLUGIN_NAME_PREFIXES = ("Komplete Kontrol", "Kontakt")
KONTAKT_PARAMETER_NAME_PREFIX = "NIKT"


def get_parameter_name_for_instance(instance):
    param_names = instance.get_parameter_names()
    if param_names:
        if instance.name.startswith("Komplete Kontrol"):
            return param_names[0]
        for index in (2048, 4096):
            if index < len(param_names):
                if param_names[index].startswith(KONTAKT_PARAMETER_NAME_PREFIX):
                    return param_names[index]

    return ""


class FocusFollowComponent(InstrumentFinderComponent):
    focus_follow_control = SendValueControl()

    def _update_instruments(self):
        instance = find_instrument_meeting_requirement(
            lambda d: isinstance(d, PluginDevice) and d.name.startswith(PLUGIN_NAME_PREFIXES),
            self._target_track.target_track,
        )
        param_name = ""
        if liveobj_valid(instance):
            param_name = get_parameter_name_for_instance(instance)
        self.focus_follow_control.value = tuple(ord(n) for n in param_name)

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_MK3/mixer.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 3084 bytes
from ableton.v2.base import liveobj_valid, nop
from ableton.v2.control_surface.control import control_list
from novation.mixer import MixerComponent as MixerComponentBase

from .control import DisplayControl

ASCII_A = 65


class MixerComponent(MixerComponentBase):
    pot_parameter_name_displays = control_list(DisplayControl, 8)
    fader_parameter_name_displays = control_list(DisplayControl, 8)

    def __init__(self, *a, **k):
        self._pot_parameter_name = None
        self._fader_parameter_name = None
        self.set_send_controls = nop
        (super().__init__)(*a, **k)

    def set_pot_parameter_name(self, name):
        self._pot_parameter_name = name
        self._update_parameter_name_displays()

    def set_fader_parameter_name(self, name):
        self._fader_parameter_name = name
        self._update_parameter_name_displays()

    def _set_send_controls(self, controls, send_index):
        if controls:
            for index, control in enumerate(controls):
                if control:
                    self.channel_strip(index).set_send_control(control, send_index)

        else:
            for strip in self._channel_strips:
                strip.set_send_control(None, send_index)

    def on_num_sends_changed(self):
        super().on_num_sends_changed()
        self._update_parameter_name_displays()

    def _reassign_tracks(self):
        super()._reassign_tracks()
        self._update_parameter_name_displays()

    def _update_parameter_name_displays(self):
        tracks = self._track_assigner.tracks(self._provider)
        pot_param_name = self._get_parameter_name_to_display(self._pot_parameter_name)
        fader_param_name = self._get_parameter_name_to_display(self._fader_parameter_name)
        for track, pot_dsp, fader_dsp in zip(
            tracks,
            self.pot_parameter_name_displays,
            self.fader_parameter_name_displays,
        ):
            track_is_valid = liveobj_valid(track)
            pot_dsp.message = pot_param_name if track_is_valid else None
            fader_dsp.message = fader_param_name if track_is_valid else None

    def _get_parameter_name_to_display(self, desired_parameter_name):
        if desired_parameter_name:
            if "Send" in desired_parameter_name:
                send_index = ord(desired_parameter_name[-1]) - ASCII_A
                if send_index >= self.num_sends:
                    return None
        return desired_parameter_name

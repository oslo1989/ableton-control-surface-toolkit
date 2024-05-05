# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/selected_track_parameter_provider.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 921 bytes
from ableton.v2.control_surface import ParameterInfo
from pushbase.selected_track_parameter_provider import (
    SelectedTrackParameterProvider as SelectedTrackParameterProviderBase,
)

from .parameter_mapping_sensitivities import fine_grain_parameter_mapping_sensitivity, parameter_mapping_sensitivity


class SelectedTrackParameterProvider(SelectedTrackParameterProviderBase):
    def _create_parameter_info(self, parameter, name):
        return ParameterInfo(
            name=name,
            parameter=parameter,
            default_encoder_sensitivity=(parameter_mapping_sensitivity(parameter)),
            fine_grain_encoder_sensitivity=(fine_grain_parameter_mapping_sensitivity(parameter)),
        )

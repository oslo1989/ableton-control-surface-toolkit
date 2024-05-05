# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/drift_decoration.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1958 bytes
from .decoration import LiveObjectDecorator
from .internal_parameter import EnumWrappingParameter


class DriftDeviceDecorator(LiveObjectDecorator):
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._additional_parameters = self._create_parameters()
        self.register_disconnectables(self._additional_parameters)

    @property
    def parameters(self):
        return tuple(self._live_object.parameters) + self._additional_parameters

    def _create_parameters(self):
        return (
            EnumWrappingParameter(
                name="Voice Mode",
                parent=self,
                values_host=(self._live_object),
                index_property_host=self,
                values_property="voice_mode_list",
                index_property="voice_mode_index",
            ),
            EnumWrappingParameter(
                name="Voice Count",
                parent=self,
                values_host=(self._live_object),
                index_property_host=self,
                values_property="voice_count_list",
                index_property="voice_count_index",
            ),
            EnumWrappingParameter(
                name="LP Mod Src 1",
                parent=self,
                values_host=(self._live_object),
                index_property_host=self,
                values_property="mod_matrix_filter_source_1_list",
                index_property="mod_matrix_filter_source_1_index",
            ),
            EnumWrappingParameter(
                name="LP Mod Src 2",
                parent=self,
                values_host=(self._live_object),
                index_property_host=self,
                values_property="mod_matrix_filter_source_2_list",
                index_property="mod_matrix_filter_source_2_index",
            ),
        )

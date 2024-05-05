from __future__ import annotations

from typing import Any, Callable

from Live import *
from Live.Application import *
from Live.Base import *
from Live.Browser import *
from Live.CcControlDevice import *
from Live.Chain import *
from Live.ChainMixerDevice import *
from Live.Clip import *
from Live.ClipSlot import *
from Live.CompressorDevice import *
from Live.Conversions import *
from Live.Device import *
from Live.DeviceIO import *
from Live.DeviceParameter import *
from Live.DriftDevice import *
from Live.DrumChain import *
from Live.DrumPad import *
from Live.Eq8Device import *
from Live.Groove import *
from Live.GroovePool import *
from Live.HybridReverbDevice import *
from Live.Listener import *
from Live.LomObject import *
from Live.MaxDevice import *
from Live.MeldDevice import *
from Live.MidiMap import *
from Live.MixerDevice import *
from Live.PluginDevice import *
from Live.RackDevice import *
from Live.RoarDevice import *
from Live.Scene import *
from Live.ShifterDevice import *
from Live.SimplerDevice import *
from Live.Song import *
from Live.SpectralResonatorDevice import *
from Live.Track import *
from Live.WavetableDevice import *


class Sample:
    """
    This class represents a sample file loaded into a Simpler instance.
    """

    def add_beats_granulation_resolution_listener(self, listener: Callable) -> None:
        """
        add_beats_granulation_resolution_listener( (Sample)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "beats_granulation_resolution" has changed.

            C++ signature :
                void add_beats_granulation_resolution_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def add_beats_transient_envelope_listener(self, listener: Callable) -> None:
        """
        add_beats_transient_envelope_listener( (Sample)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "beats_transient_envelope" has changed.

            C++ signature :
                void add_beats_transient_envelope_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def add_beats_transient_loop_mode_listener(self, listener: Callable) -> None:
        """
        add_beats_transient_loop_mode_listener( (Sample)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "beats_transient_loop_mode" has changed.

            C++ signature :
                void add_beats_transient_loop_mode_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def add_complex_pro_envelope_listener(self, listener: Callable) -> None:
        """
        add_complex_pro_envelope_listener( (Sample)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "complex_pro_envelope" has changed.

            C++ signature :
                void add_complex_pro_envelope_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def add_complex_pro_formants_listener(self, listener: Callable) -> None:
        """
        add_complex_pro_formants_listener( (Sample)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "complex_pro_formants" has changed.

            C++ signature :
                void add_complex_pro_formants_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def add_end_marker_listener(self, listener: Callable) -> None:
        """
        add_end_marker_listener( (Sample)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "end_marker" has changed.

            C++ signature :
                void add_end_marker_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def add_file_path_listener(self, listener: Callable) -> None:
        """
        add_file_path_listener( (Sample)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "file_path" has changed.

            C++ signature :
                void add_file_path_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def add_gain_listener(self, listener: Callable) -> None:
        """
        add_gain_listener( (Sample)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "gain" has changed.

            C++ signature :
                void add_gain_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def add_slices_listener(self, listener: Callable) -> None:
        """
        add_slices_listener( (Sample)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "slices" has changed.

            C++ signature :
                void add_slices_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def add_slicing_beat_division_listener(self, listener: Callable) -> None:
        """
        add_slicing_beat_division_listener( (Sample)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "slicing_beat_division" has changed.

            C++ signature :
                void add_slicing_beat_division_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def add_slicing_region_count_listener(self, listener: Callable) -> None:
        """
        add_slicing_region_count_listener( (Sample)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "slicing_region_count" has changed.

            C++ signature :
                void add_slicing_region_count_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def add_slicing_sensitivity_listener(self, listener: Callable) -> None:
        """
        add_slicing_sensitivity_listener( (Sample)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "slicing_sensitivity" has changed.

            C++ signature :
                void add_slicing_sensitivity_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def add_slicing_style_listener(self, listener: Callable) -> None:
        """
        add_slicing_style_listener( (Sample)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "slicing_style" has changed.

            C++ signature :
                void add_slicing_style_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def add_start_marker_listener(self, listener: Callable) -> None:
        """
        add_start_marker_listener( (Sample)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "start_marker" has changed.

            C++ signature :
                void add_start_marker_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def add_texture_flux_listener(self, listener: Callable) -> None:
        """
        add_texture_flux_listener( (Sample)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "texture_flux" has changed.

            C++ signature :
                void add_texture_flux_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def add_texture_grain_size_listener(self, listener: Callable) -> None:
        """
        add_texture_grain_size_listener( (Sample)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "texture_grain_size" has changed.

            C++ signature :
                void add_texture_grain_size_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def add_tones_grain_size_listener(self, listener: Callable) -> None:
        """
        add_tones_grain_size_listener( (Sample)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "tones_grain_size" has changed.

            C++ signature :
                void add_tones_grain_size_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def add_warp_markers_listener(self, listener: Callable) -> None:
        """
        add_warp_markers_listener( (Sample)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "warp_markers" has changed.

            C++ signature :
                void add_warp_markers_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def add_warp_mode_listener(self, listener: Callable) -> None:
        """
        add_warp_mode_listener( (Sample)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "warp_mode" has changed.

            C++ signature :
                void add_warp_mode_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def add_warping_listener(self, listener: Callable) -> None:
        """
        add_warping_listener( (Sample)arg1, (object)arg2) -> None :
            Add a listener function or method, which will be called as soon as the
            property "warping" has changed.

            C++ signature :
                void add_warping_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def beat_to_sample_time(self, beat_time: float) -> float:
        """
        beat_to_sample_time( (Sample)self, (float)beat_time) -> float :
            Converts the given beat time to sample time. Raises an error if the sample is not warped.

            C++ signature :
                double beat_to_sample_time(TPyHandle<AMultiSamplePart>,double)
        """

    def beats_granulation_resolution_has_listener(self, listener: Callable) -> bool:
        """
        beats_granulation_resolution_has_listener( (Sample)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "beats_granulation_resolution".

            C++ signature :
                bool beats_granulation_resolution_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def beats_transient_envelope_has_listener(self, listener: Callable) -> bool:
        """
        beats_transient_envelope_has_listener( (Sample)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "beats_transient_envelope".

            C++ signature :
                bool beats_transient_envelope_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def beats_transient_loop_mode_has_listener(self, listener: Callable) -> bool:
        """
        beats_transient_loop_mode_has_listener( (Sample)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "beats_transient_loop_mode".

            C++ signature :
                bool beats_transient_loop_mode_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def clear_slices(self) -> None:
        """
        clear_slices( (Sample)self) -> None :
            Clears all slices created in Simpler's manual mode.

            C++ signature :
                void clear_slices(TPyHandle<AMultiSamplePart>)
        """

    def complex_pro_envelope_has_listener(self, listener: Callable) -> bool:
        """
        complex_pro_envelope_has_listener( (Sample)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "complex_pro_envelope".

            C++ signature :
                bool complex_pro_envelope_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def complex_pro_formants_has_listener(self, listener: Callable) -> bool:
        """
        complex_pro_formants_has_listener( (Sample)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "complex_pro_formants".

            C++ signature :
                bool complex_pro_formants_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def end_marker_has_listener(self, listener: Callable) -> bool:
        """
        end_marker_has_listener( (Sample)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "end_marker".

            C++ signature :
                bool end_marker_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def file_path_has_listener(self, listener: Callable) -> bool:
        """
        file_path_has_listener( (Sample)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "file_path".

            C++ signature :
                bool file_path_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def gain_display_string(self) -> str:
        """
        gain_display_string( (Sample)self) -> str :
            Get the gain's display value as a string.

            C++ signature :
                TString gain_display_string(TPyHandle<AMultiSamplePart>)
        """

    def gain_has_listener(self, listener: Callable) -> bool:
        """
        gain_has_listener( (Sample)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "gain".

            C++ signature :
                bool gain_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def insert_slice(self, slice_time: int) -> None:
        """
        insert_slice( (Sample)self, (int)slice_time) -> None :
            Add a slice point at the provided time if there is none.

            C++ signature :
                void insert_slice(TPyHandle<AMultiSamplePart>,int)
        """

    def move_slice(self, old_time: int, new_time: int) -> int:
        """
        move_slice( (Sample)self, (int)old_time, (int)new_time) -> int :
            Move the slice point at the provided time.

            C++ signature :
                int move_slice(TPyHandle<AMultiSamplePart>,int,int)
        """

    def remove_beats_granulation_resolution_listener(self, listener: Callable) -> None:
        """
        remove_beats_granulation_resolution_listener( (Sample)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "beats_granulation_resolution".

            C++ signature :
                void remove_beats_granulation_resolution_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def remove_beats_transient_envelope_listener(self, listener: Callable) -> None:
        """
        remove_beats_transient_envelope_listener( (Sample)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "beats_transient_envelope".

            C++ signature :
                void remove_beats_transient_envelope_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def remove_beats_transient_loop_mode_listener(self, listener: Callable) -> None:
        """
        remove_beats_transient_loop_mode_listener( (Sample)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "beats_transient_loop_mode".

            C++ signature :
                void remove_beats_transient_loop_mode_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def remove_complex_pro_envelope_listener(self, listener: Callable) -> None:
        """
        remove_complex_pro_envelope_listener( (Sample)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "complex_pro_envelope".

            C++ signature :
                void remove_complex_pro_envelope_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def remove_complex_pro_formants_listener(self, listener: Callable) -> None:
        """
        remove_complex_pro_formants_listener( (Sample)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "complex_pro_formants".

            C++ signature :
                void remove_complex_pro_formants_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def remove_end_marker_listener(self, listener: Callable) -> None:
        """
        remove_end_marker_listener( (Sample)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "end_marker".

            C++ signature :
                void remove_end_marker_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def remove_file_path_listener(self, listener: Callable) -> None:
        """
        remove_file_path_listener( (Sample)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "file_path".

            C++ signature :
                void remove_file_path_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def remove_gain_listener(self, listener: Callable) -> None:
        """
        remove_gain_listener( (Sample)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "gain".

            C++ signature :
                void remove_gain_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def remove_slice(self, slice_time: int) -> None:
        """
        remove_slice( (Sample)self, (int)slice_time) -> None :
            Remove the slice point at the provided time if there is one.

            C++ signature :
                void remove_slice(TPyHandle<AMultiSamplePart>,int)
        """

    def remove_slices_listener(self, listener: Callable) -> None:
        """
        remove_slices_listener( (Sample)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "slices".

            C++ signature :
                void remove_slices_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def remove_slicing_beat_division_listener(self, listener: Callable) -> None:
        """
        remove_slicing_beat_division_listener( (Sample)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "slicing_beat_division".

            C++ signature :
                void remove_slicing_beat_division_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def remove_slicing_region_count_listener(self, listener: Callable) -> None:
        """
        remove_slicing_region_count_listener( (Sample)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "slicing_region_count".

            C++ signature :
                void remove_slicing_region_count_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def remove_slicing_sensitivity_listener(self, listener: Callable) -> None:
        """
        remove_slicing_sensitivity_listener( (Sample)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "slicing_sensitivity".

            C++ signature :
                void remove_slicing_sensitivity_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def remove_slicing_style_listener(self, listener: Callable) -> None:
        """
        remove_slicing_style_listener( (Sample)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "slicing_style".

            C++ signature :
                void remove_slicing_style_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def remove_start_marker_listener(self, listener: Callable) -> None:
        """
        remove_start_marker_listener( (Sample)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "start_marker".

            C++ signature :
                void remove_start_marker_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def remove_texture_flux_listener(self, listener: Callable) -> None:
        """
        remove_texture_flux_listener( (Sample)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "texture_flux".

            C++ signature :
                void remove_texture_flux_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def remove_texture_grain_size_listener(self, listener: Callable) -> None:
        """
        remove_texture_grain_size_listener( (Sample)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "texture_grain_size".

            C++ signature :
                void remove_texture_grain_size_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def remove_tones_grain_size_listener(self, listener: Callable) -> None:
        """
        remove_tones_grain_size_listener( (Sample)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "tones_grain_size".

            C++ signature :
                void remove_tones_grain_size_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def remove_warp_markers_listener(self, listener: Callable) -> None:
        """
        remove_warp_markers_listener( (Sample)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "warp_markers".

            C++ signature :
                void remove_warp_markers_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def remove_warp_mode_listener(self, listener: Callable) -> None:
        """
        remove_warp_mode_listener( (Sample)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "warp_mode".

            C++ signature :
                void remove_warp_mode_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def remove_warping_listener(self, listener: Callable) -> None:
        """
        remove_warping_listener( (Sample)arg1, (object)arg2) -> None :
            Remove a previously set listener function or method from
            property "warping".

            C++ signature :
                void remove_warping_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def reset_slices(self) -> None:
        """
        reset_slices( (Sample)self) -> None :
            Resets all edited slices to their original positions.

            C++ signature :
                void reset_slices(TPyHandle<AMultiSamplePart>)
        """

    def sample_to_beat_time(self, sample_time: float) -> float:
        """
        sample_to_beat_time( (Sample)self, (float)sample_time) -> float :
            Converts the given sample time to beat time. Raises an error if the sample is not warped.

            C++ signature :
                double sample_to_beat_time(TPyHandle<AMultiSamplePart>,double)
        """

    def slices_has_listener(self, listener: Callable) -> bool:
        """
        slices_has_listener( (Sample)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "slices".

            C++ signature :
                bool slices_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def slicing_beat_division_has_listener(self, listener: Callable) -> bool:
        """
        slicing_beat_division_has_listener( (Sample)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "slicing_beat_division".

            C++ signature :
                bool slicing_beat_division_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def slicing_region_count_has_listener(self, listener: Callable) -> bool:
        """
        slicing_region_count_has_listener( (Sample)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "slicing_region_count".

            C++ signature :
                bool slicing_region_count_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def slicing_sensitivity_has_listener(self, listener: Callable) -> bool:
        """
        slicing_sensitivity_has_listener( (Sample)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "slicing_sensitivity".

            C++ signature :
                bool slicing_sensitivity_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def slicing_style_has_listener(self, listener: Callable) -> bool:
        """
        slicing_style_has_listener( (Sample)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "slicing_style".

            C++ signature :
                bool slicing_style_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def start_marker_has_listener(self, listener: Callable) -> bool:
        """
        start_marker_has_listener( (Sample)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "start_marker".

            C++ signature :
                bool start_marker_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def texture_flux_has_listener(self, listener: Callable) -> bool:
        """
        texture_flux_has_listener( (Sample)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "texture_flux".

            C++ signature :
                bool texture_flux_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def texture_grain_size_has_listener(self, listener: Callable) -> bool:
        """
        texture_grain_size_has_listener( (Sample)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "texture_grain_size".

            C++ signature :
                bool texture_grain_size_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def tones_grain_size_has_listener(self, listener: Callable) -> bool:
        """
        tones_grain_size_has_listener( (Sample)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "tones_grain_size".

            C++ signature :
                bool tones_grain_size_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def warp_markers_has_listener(self, listener: Callable) -> bool:
        """
        warp_markers_has_listener( (Sample)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "warp_markers".

            C++ signature :
                bool warp_markers_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def warp_mode_has_listener(self, listener: Callable) -> bool:
        """
        warp_mode_has_listener( (Sample)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "warp_mode".

            C++ signature :
                bool warp_mode_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    def warping_has_listener(self, listener: Callable) -> bool:
        """
        warping_has_listener( (Sample)arg1, (object)arg2) -> bool :
            Returns true, if the given listener function or method is connected
            to the property "warping".

            C++ signature :
                bool warping_has_listener(TPyHandle<AMultiSamplePart>,boost::python::api::object)
        """

    @property
    def beats_granulation_resolution(self) -> Any:
        """
        Access to the Granulation Resolution parameter in Beats Warp Mode.
        """

    @property
    def beats_transient_envelope(self) -> Any:
        """
        Access to the Transient Envelope parameter in Beats Warp Mode.
        """

    @property
    def beats_transient_loop_mode(self) -> Any:
        """
        Access to the Transient Loop Mode parameter in Beats Warp Mode.
        """

    @property
    def canonical_parent(self) -> Any:
        """
        Access to the sample's canonical parent.
        """

    @property
    def complex_pro_envelope(self) -> Any:
        """
        Access to the Envelope parameter in Complex Pro Mode.
        """

    @property
    def complex_pro_formants(self) -> Any:
        """
        Access to the Formants parameter in Complex Pro Warp Mode.
        """

    @property
    def end_marker(self) -> Any:
        """
        Access to the position of the sample's end marker.
        """

    @property
    def file_path(self) -> Any:
        """
        Get the path of the sample file.
        """

    @property
    def gain(self) -> Any:
        """
        Access to the sample gain.
        """

    @property
    def length(self) -> Any:
        """
        Get the length of the sample file in sample frames.
        """

    @property
    def sample_rate(self) -> Any:
        """
        Access to the audio sample rate of the sample.
        """

    @property
    def slices(self) -> Any:
        """
        Access to the list of slice points in sample time in the sample.
        """

    @property
    def slicing_beat_division(self) -> Any:
        """
        Access to sample's slicing step size.
        """

    @property
    def slicing_region_count(self) -> Any:
        """
        Access to sample's slicing split count.
        """

    @property
    def slicing_sensitivity(self) -> Any:
        """
        Access to sample's slicing sensitivity whose sensitivity is in between 0.0 and 1.0.
        The higher the sensitivity, the more slices will be available.
        """

    @property
    def slicing_style(self) -> Any:
        """
        Access to sample's slicing style.
        """

    @property
    def start_marker(self) -> Any:
        """
        Access to the position of the sample's start marker.
        """

    @property
    def texture_flux(self) -> Any:
        """
        Access to the Flux parameter in Texture Warp Mode.
        """

    @property
    def texture_grain_size(self) -> Any:
        """
        Access to the Grain Size parameter in Texture Warp Mode.
        """

    @property
    def tones_grain_size(self) -> Any:
        """
        Access to the Grain Size parameter in Tones Warp Mode.
        """

    @property
    def warp_markers(self) -> Any:
        """
        Get the warp markers for this sample.
        """

    @property
    def warp_mode(self) -> Any:
        """
        Access to the sample's warp mode.
        """

    @property
    def warping(self) -> Any:
        """
        Access to the sample's warping property.
        """


class SlicingBeatDivision:
    """
    Class that represent an enumeration of values for SlicingBeatDivision
    int([x]) -> integer
    int(x, base=10) -> integer

    Convert a number or string to an integer, or return 0 if no arguments
    are given.  If x is a number, return x.__int__().  For floating point
    numbers, this truncates towards zero.

    If x is not a number or if base is given, then x must be a string,
    bytes, or bytearray instance representing an integer literal in the
    given base.  The literal can be preceded by '+' or '-' and be surrounded
    by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
    Base 0 means to interpret the base from the string as an integer literal.
    >>> int('0b100', base=0)
    4
    """

    sixteenth = 0
    sixteenth_triplett = 1
    eighth = 2
    eighth_triplett = 3
    quarter = 4
    quarter_triplett = 5
    half = 6
    half_triplett = 7
    one_bar = 8
    two_bars = 9
    four_bars = 10


class SlicingStyle:
    """
    Class that represent an enumeration of values for SlicingStyle
    int([x]) -> integer
    int(x, base=10) -> integer

    Convert a number or string to an integer, or return 0 if no arguments
    are given.  If x is a number, return x.__int__().  For floating point
    numbers, this truncates towards zero.

    If x is not a number or if base is given, then x must be a string,
    bytes, or bytearray instance representing an integer literal in the
    given base.  The literal can be preceded by '+' or '-' and be surrounded
    by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
    Base 0 means to interpret the base from the string as an integer literal.
    >>> int('0b100', base=0)
    4
    """

    transient = 0
    beat = 1
    region = 2
    manual = 3


class TransientLoopMode:
    """
    Class that represent an enumeration of values for TransientLoopMode
    int([x]) -> integer
    int(x, base=10) -> integer

    Convert a number or string to an integer, or return 0 if no arguments
    are given.  If x is a number, return x.__int__().  For floating point
    numbers, this truncates towards zero.

    If x is not a number or if base is given, then x must be a string,
    bytes, or bytearray instance representing an integer literal in the
    given base.  The literal can be preceded by '+' or '-' and be surrounded
    by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
    Base 0 means to interpret the base from the string as an integer literal.
    >>> int('0b100', base=0)
    4
    """

    off = 0
    forward = 1
    alternate = 2

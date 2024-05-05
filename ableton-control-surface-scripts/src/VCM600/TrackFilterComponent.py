# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/VCM600/TrackFilterComponent.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 3926 bytes
from _Framework import ControlSurfaceComponent
from _Generic.Devices import get_parameter_by_name

FILTER_DEVICES = {
    "AutoFilter": {"Frequency": "Frequency", "Resonance": "Resonance"},
    "Operator": {"Frequency": "Filter Freq", "Resonance": "Filter Res"},
    "OriginalSimpler": {"Frequency": "Filter Freq", "Resonance": "Filter Res"},
    "MultiSampler": {"Frequency": "Filter Freq", "Resonance": "Filter Res"},
    "UltraAnalog": {"Frequency": "F1 Freq", "Resonance": "F1 Resonance"},
    "StringStudio": {"Frequency": "Filter Freq", "Resonance": "Filter Reso"},
}


class TrackFilterComponent(ControlSurfaceComponent):
    def __init__(self):
        ControlSurfaceComponent.__init__(self)
        self._track = None
        self._device = None
        self._freq_control = None
        self._reso_control = None

    def disconnect(self):
        if self._freq_control is not None:
            self._freq_control.release_parameter()
            self._freq_control = None
        if self._reso_control is not None:
            self._reso_control.release_parameter()
            self._reso_control = None
        if self._track is not None:
            self._track.remove_devices_listener(self._on_devices_changed)
            self._track = None
        self._device = None

    def on_enabled_changed(self):
        self.update()

    def set_track(self, track):
        if self._track is not None:
            self._track.remove_devices_listener(self._on_devices_changed)
            if self._device is not None:
                if self._freq_control is not None:
                    self._freq_control.release_parameter()
                if self._reso_control is not None:
                    self._reso_control.release_parameter()
        self._track = track
        if self._track is not None:
            self._track.add_devices_listener(self._on_devices_changed)
        self._on_devices_changed()

    def set_filter_controls(self, freq, reso):
        if self._device is not None:
            if self._freq_control is not None:
                self._freq_control.release_parameter()
            if self._reso_control is not None:
                self._reso_control.release_parameter()
        self._freq_control = freq
        self._reso_control = reso
        self.update()

    def update(self):
        super().update()
        if self.is_enabled():
            if self._device is not None:
                device_dict = FILTER_DEVICES[self._device.class_name]
                if self._freq_control is not None:
                    self._freq_control.release_parameter()
                    parameter = get_parameter_by_name(self._device, device_dict["Frequency"])
                    if parameter is not None:
                        self._freq_control.connect_to(parameter)
                if self._reso_control is not None:
                    self._reso_control.release_parameter()
                    parameter = get_parameter_by_name(self._device, device_dict["Resonance"])
                    if parameter is not None:
                        self._reso_control.connect_to(parameter)

    def _on_devices_changed(self):
        self._device = None
        if self._track is not None:
            for index in range(len(self._track.devices)):
                device = self._track.devices[-1 * (index + 1)]
                if device.class_name in list(FILTER_DEVICES.keys()):
                    self._device = device
                    break

        self.update()

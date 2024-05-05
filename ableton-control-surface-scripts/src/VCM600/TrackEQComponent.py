# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/VCM600/TrackEQComponent.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 7704 bytes
from _Framework import ControlSurfaceComponent
from _Generic.Devices import get_parameter_by_name

EQ_DEVICES = {
    "Eq8": {"Gains": ["%i Gain A" % (index + 1) for index in range(8)]},
    "FilterEQ3": {"Gains": ["GainLo", "GainMid", "GainHi"], "Cuts": ["LowOn", "MidOn", "HighOn"]},
}


class TrackEQComponent(ControlSurfaceComponent):
    def __init__(self):
        ControlSurfaceComponent.__init__(self)
        self._track = None
        self._device = None
        self._gain_controls = None
        self._cut_buttons = None

    def disconnect(self):
        if self._gain_controls is not None:
            for control in self._gain_controls:
                control.release_parameter()

            self._gain_controls = None
        if self._cut_buttons is not None:
            for button in self._cut_buttons:
                button.remove_value_listener(self._cut_value)

        self._cut_buttons = None
        if self._track is not None:
            self._track.remove_devices_listener(self._on_devices_changed)
            self._track = None
        self._device = None
        if self._device is not None:
            device_dict = EQ_DEVICES[self._device.class_name]
            if "Cuts" in list(device_dict.keys()):
                cut_names = device_dict["Cuts"]
                for cut_name in cut_names:
                    parameter = get_parameter_by_name(self._device, cut_name)
                    if parameter is not None:
                        if parameter.value_has_listener(self._on_cut_changed):
                            parameter.remove_value_listener(self._on_cut_changed)

    def on_enabled_changed(self):
        self.update()

    def set_track(self, track):
        if self._track is not None:
            self._track.remove_devices_listener(self._on_devices_changed)
            if self._gain_controls is not None:
                if self._device is not None:
                    for control in self._gain_controls:
                        control.release_parameter()

        self._track = track
        if self._track is not None:
            self._track.add_devices_listener(self._on_devices_changed)
        self._on_devices_changed()

    def set_cut_buttons(self, buttons):
        if buttons != self._cut_buttons:
            if self._cut_buttons is not None:
                for button in self._cut_buttons:
                    button.remove_value_listener(self._cut_value)

            self._cut_buttons = buttons
            if self._cut_buttons is not None:
                for button in self._cut_buttons:
                    button.add_value_listener((self._cut_value), identify_sender=True)

            self.update()

    def set_gain_controls(self, controls):
        if self._device is not None:
            if self._gain_controls is not None:
                for control in self._gain_controls:
                    control.release_parameter()

        for control in controls:
            pass

        self._gain_controls = controls
        self.update()

    def update(self):
        super().update()
        if self.is_enabled() and self._device is not None:
            device_dict = EQ_DEVICES[self._device.class_name]
            if self._gain_controls is not None:
                gain_names = device_dict["Gains"]
                for index in range(len(self._gain_controls)):
                    self._gain_controls[index].release_parameter()
                    if len(gain_names) > index:
                        parameter = get_parameter_by_name(self._device, gain_names[index])
                        if parameter is not None:
                            self._gain_controls[index].connect_to(parameter)

            if self._cut_buttons is None or "Cuts" in list(device_dict.keys()):
                cut_names = device_dict["Cuts"]
                for index in range(len(self._cut_buttons)):
                    self._cut_buttons[index].turn_off()
                    if len(cut_names) > index:
                        parameter = get_parameter_by_name(self._device, cut_names[index])
                        if parameter is not None:
                            if parameter.value == 0.0:
                                self._cut_buttons[index].turn_on()
                            if not parameter.value_has_listener(self._on_cut_changed):
                                parameter.add_value_listener(self._on_cut_changed)

        else:
            if self._cut_buttons is not None:
                for button in self._cut_buttons:
                    if button is not None:
                        button.turn_off()

            if self._gain_controls is not None:
                for control in self._gain_controls:
                    control.release_parameter()

    def _cut_value(self, value, sender):
        if self.is_enabled():
            if self._device is not None:
                if not sender.is_momentary() or value != 0:
                    device_dict = EQ_DEVICES[self._device.class_name]
                    if "Cuts" in list(device_dict.keys()):
                        cut_names = device_dict["Cuts"]
                        index = list(self._cut_buttons).index(sender)
                        if index in range(len(cut_names)):
                            parameter = get_parameter_by_name(self._device, cut_names[index])
                            if parameter is not None:
                                if parameter.is_enabled:
                                    parameter.value = float(int(parameter.value + 1) % 2)

    def _on_devices_changed(self):
        if self._device is not None:
            device_dict = EQ_DEVICES[self._device.class_name]
            if "Cuts" in list(device_dict.keys()):
                cut_names = device_dict["Cuts"]
                for cut_name in cut_names:
                    parameter = get_parameter_by_name(self._device, cut_name)
                    if parameter is not None:
                        if parameter.value_has_listener(self._on_cut_changed):
                            parameter.remove_value_listener(self._on_cut_changed)

        self._device = None
        if self._track is not None:
            for index in range(len(self._track.devices)):
                device = self._track.devices[-1 * (index + 1)]
                if device.class_name in list(EQ_DEVICES.keys()):
                    self._device = device
                    break

        self.update()

    def _on_cut_changed(self):
        if self.is_enabled():
            if self._cut_buttons is not None:
                cut_names = EQ_DEVICES[self._device.class_name]["Cuts"]
                for index in range(len(self._cut_buttons)):
                    self._cut_buttons[index].turn_off()
                    if len(cut_names) > index:
                        parameter = get_parameter_by_name(self._device, cut_names[index])
                        if parameter is not None:
                            if parameter.value == 0.0:
                                self._cut_buttons[index].turn_on()

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Alesis_V/Alesis_V.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1465 bytes
import Live
from _Framework import ButtonMatrixElement, ControlSurface, DeviceComponent, EncoderElement, Layer
from _Framework.InputControlElement import MIDI_CC_TYPE


class Alesis_V(ControlSurface):
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        with self.component_guard():
            encoders = ButtonMatrixElement(
                rows=[
                    [
                        EncoderElement(
                            MIDI_CC_TYPE,
                            0,
                            (identifier + 20),
                            (Live.MidiMap.MapMode.absolute),
                            name=("Encoder_%d" % identifier),
                        )
                        for identifier in range(4)
                    ],
                ],
            )
            device = DeviceComponent(
                name="Device",
                is_enabled=False,
                layer=Layer(parameter_controls=encoders),
                device_selection_follows_track_selection=True,
            )
            device.set_enabled(True)
            self.set_device_component(device)

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Blackstar_Live_Logic/blackstar_live_logic.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1883 bytes
from ableton.v2.control_surface import Layer, SimpleControlSurface
from ableton.v2.control_surface.midi import is_sysex

from .elements import Elements
from .looper import LooperComponent


class Blackstar_Live_Logic(SimpleControlSurface):
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        with self.component_guard():
            self._elements = Elements()
            self._looper = LooperComponent(
                name="Looper",
                is_enabled=False,
                layer=Layer(foot_switches=(self._elements.foot_switches), time_display=(self._elements.time_display)),
            )

    def disconnect(self):
        super().disconnect()
        self._elements.live_integration_mode_switch.send_value(0)

    def port_settings_changed(self):
        self._elements.live_integration_mode_switch.send_value(1)
        self.schedule_message(1, self._looper.set_enabled, True)
        self.schedule_message(2, self.refresh_state)

    def process_midi_bytes(self, midi_bytes, midi_processor):
        if is_sysex(midi_bytes):
            return None
        return super().process_midi_bytes(midi_bytes, midi_processor)

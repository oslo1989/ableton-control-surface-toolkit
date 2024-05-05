# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Framework/MomentaryModeObserver.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1807 bytes
from . import Defaults


class MomentaryModeObserver:
    def __init__(self):
        object.__init__(self)
        self._controls = None
        self._mode_callback = None
        self._reset()

    def disconnect(self):
        self._reset()

    def set_mode_details(self, base_mode, controls, mode_callback=None):
        self._reset()
        if controls is not None:
            self._controls = controls
            for control in self._controls:
                control.add_value_listener(self._control_changed)

        self._base_mode = base_mode
        self._mode_callback = mode_callback

    def is_mode_momentary(self):
        return self._controls_changed or self._timer_count >= Defaults.MOMENTARY_DELAY_TICKS

    def on_timer(self):
        self._timer_count += 1

    def _control_changed(self, value):
        if self._mode_callback is None or self._mode_callback() == self._base_mode:
            self._controls_changed = True

    def _release_controls(self):
        if self._controls is not None:
            for control in self._controls:
                control.remove_value_listener(self._control_changed)

            self._controls = None

    def _reset(self):
        self._base_mode = -1
        self._controls_changed = False
        self._mode_callback = None
        self._timer_count = 0
        self._release_controls()

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Akai_Force_MPC/session_recording.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 885 bytes
from ableton.v2.control_surface.components import SessionRecordingComponent as SessionRecordingComponentBase
from ableton.v2.control_surface.control import ToggleButtonControl


class SessionRecordingComponent(SessionRecordingComponentBase):
    mpc_automation_toggle = ToggleButtonControl(toggled_color="Automation.On", untoggled_color="Automation.Off")

    def _on_session_automation_record_changed(self):
        super()._on_session_automation_record_changed()
        self.mpc_automation_toggle.is_toggled = self.song.session_automation_record

    @mpc_automation_toggle.toggled
    def mpc_automation_toggle(self, is_toggled, _):
        self.song.session_automation_record = is_toggled

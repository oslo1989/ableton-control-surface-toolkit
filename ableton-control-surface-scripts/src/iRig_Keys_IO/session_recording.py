# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/iRig_Keys_IO/session_recording.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 533 bytes
from ableton.v2.control_surface.components import SessionRecordingComponent as SessionRecordingComponentBase
from ableton.v2.control_surface.control import ButtonControl


class SessionRecordingComponent(SessionRecordingComponentBase):
    record_stop_button = ButtonControl()

    @record_stop_button.pressed
    def record_stop_button(self, _):
        self.song.session_record = False

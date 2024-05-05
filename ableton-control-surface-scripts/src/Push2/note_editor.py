# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/note_editor.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 494 bytes
from pushbase.note_editor_component import NoteEditorComponent


class Push2NoteEditorComponent(NoteEditorComponent):
    __events__ = ("mute_solo_stop_cancel_action_performed",)

    def _on_pad_pressed(self, coordinate):
        super()._on_pad_pressed(coordinate)
        self.notify_mute_solo_stop_cancel_action_performed()

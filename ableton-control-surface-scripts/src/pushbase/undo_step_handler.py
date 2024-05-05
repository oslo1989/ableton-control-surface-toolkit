# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/pushbase/undo_step_handler.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1461 bytes


class UndoStepHandler:
    def __init__(self, song=None):
        self._song = song
        self._clients = set()

    def _begin_step_with_client(self, client):
        if client not in self._clients:
            self._clients.add(client)
            if len(self._clients) == 1:
                self._song.begin_undo_step()

    def _end_step_with_client(self, client):
        if client in self._clients:
            self._clients.remove(client)
            if len(self._clients) == 0:
                self._song.end_undo_step()

    def begin_undo_step(self, client=None):
        if client:
            self._begin_step_with_client(client)
        else:
            self._song.begin_undo_step()

    def end_undo_step(self, client=None):
        if client:
            self._end_step_with_client(client)
        else:
            self._song.end_undo_step()
            if len(self._clients) > 0:
                self._song.begin_undo_step()

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Novation_Impulse/TransportViewModeSelector.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 3151 bytes
from _Framework import ModeSelectorComponent


class TransportViewModeSelector(ModeSelectorComponent):
    def __init__(self, transport, session, ffwd_button, rwd_button, loop_button):
        ModeSelectorComponent.__init__(self)
        self._transport = transport
        self._session = session
        self._ffwd_button = ffwd_button
        self._rwd_button = rwd_button
        self._loop_button = loop_button
        self.application().view.add_is_view_visible_listener("Session", self._on_view_changed)
        self.update()

    def disconnect(self):
        ModeSelectorComponent.disconnect(self)
        self._transport = None
        self._session = None
        self._ffwd_button = None
        self._rwd_button = None
        self._loop_button = None
        self.application().view.remove_is_view_visible_listener("Session", self._on_view_changed)

    def update(self):
        super().update()
        if self.is_enabled():
            if self._mode_index == 0:
                self._transport.set_seek_buttons(self._ffwd_button, self._rwd_button)
                self._transport.set_loop_button(self._loop_button)
                self._session.set_select_buttons(None, None)
                self._session.selected_scene().set_launch_button(None)
            else:
                self._transport.set_seek_buttons(None, None)
                self._transport.set_loop_button(None)
                self._session.set_select_buttons(self._ffwd_button, self._rwd_button)
                self._session.selected_scene().set_launch_button(self._loop_button)

    def _on_view_changed(self):
        if self.application().view.is_view_visible("Session"):
            self._mode_index = 1
        else:
            self._mode_index = 0
        self.update()
# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/novation/configurable_playable.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 554 bytes
from ableton.v2.control_surface.components import PlayableComponent


class ConfigurablePlayableComponent(PlayableComponent):
    def __init__(self, translation_channel, *a, **k):
        self._translation_channel = translation_channel
        (super().__init__)(*a, **k)

    def _note_translation_for_button(self, button):
        return (button.identifier, self._translation_channel)

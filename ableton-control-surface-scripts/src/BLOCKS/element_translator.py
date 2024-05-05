# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/BLOCKS/element_translator.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 821 bytes


class ElementTranslator:
    def __init__(self, elements=None, feedback_channel=None, non_feedback_channel=None, *a, **k):
        (super().__init__)(*a, **k)
        self._elements = elements
        self._feedback_channel = feedback_channel
        self._non_feedback_channel = non_feedback_channel

    def set_enabled(self, enable):
        for element in self._elements:
            channel = self._non_feedback_channel
            if enable:
                element.reset_state()
                channel = self._feedback_channel
            else:
                element.set_channel(channel)

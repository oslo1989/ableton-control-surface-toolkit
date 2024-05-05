# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/elements/display_line.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 3082 bytes
from typing import Generic, TypeVar, Union

from .. import NotifyingControlElement
from ..display import Text, updating_display

DisplayDataType = TypeVar("DisplayDataType")


class DisplayLineElement(NotifyingControlElement, Generic[DisplayDataType]):
    def __init__(
        self,
        display_fn,
        formatting_fn=lambda message: message.as_ascii(),
        default_formatting=Text(),
        *a,
        **k,
    ):
        (super().__init__)(*a, **k)
        self._display_fn = display_fn
        self._formatting_fn = formatting_fn
        self._default_formatting = default_formatting
        self._last_native_content = None

    def display_message(self, text):
        if updating_display:
            if self._last_native_content != text:
                self._last_native_content = text
                if not self.grabbed:
                    self._do_display(text)
        else:
            self._do_display(text)

    def _apply_default_formatting(self, text: Text):
        if text.max_width is None:
            text.max_width = self._default_formatting.max_width
        if text.justification is None:
            text.justification = self._default_formatting.justification

    def _do_display(self, message: Union[(Text, str)]):
        text = message if isinstance(message, Text) else Text(message)
        self._apply_default_formatting(text)
        self._display_fn(self._formatting_fn(text))

    @property
    def grabbed(self):
        return self.resource.stack_size > 1

    def clear_send_cache(self):
        self._last_native_content = None

    def reset(self):
        if self.grabbed:
            self._do_display("")
        else:
            self._redisplay_last_native_content()

    def _redisplay_last_native_content(self):
        if self._last_native_content is not None:
            self._do_display(self._last_native_content)

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/display/view/view.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 4413 bytes
from typing import Callable, Generic

from ....base import const, depends
from ..type_decl import DISCONNECT_EVENT, INIT_EVENT, ContentType, Event, Render, State


class View(Generic[ContentType]):
    def __init__(
        self,
        render: Render[ContentType],
        render_condition: Callable[([State], bool)] = lambda _: True,
        content_condition: Callable[([ContentType], bool)] = lambda content: content is not None,
    ):
        self._render = render
        self._render_condition = render_condition
        self._content_condition = content_condition

    @depends(register_react_fn=(const(None)))
    def __new__(cls, *a, register_react_fn=None, **k):
        obj = (super().__new__)(cls, *a, **k)
        if hasattr(obj, "react"):
            register_react_fn(obj.react)
        return obj

    def __call__(self, state: State) -> ContentType:
        return self.render(state)

    def render(self, state: State) -> ContentType:
        return self._render(state)

    def render_condition(self, state: State) -> bool:
        return self._render_condition(state)

    def content_condition(self, content) -> bool:
        return self._content_condition(content)


class CompoundView(View[ContentType], Generic[ContentType]):
    class NoRender:
        pass

    def __init__(self, *views):
        super().__init__(self.compound_render)
        self._views = tuple(reversed(views))

    def compound_render(self, state: State) -> ContentType:
        result = self.NoRender()
        for view in self._views:
            if view.render_condition(state):
                content = view.render(state)
                if view.content_condition(content):
                    result = content

        return result


class DisconnectedView(View[ContentType], Generic[ContentType]):
    def __init__(
        self,
        render=const(None),
        render_condition=lambda state: not state.connected
        or hasattr(state, "identification")
        and not state.identification.is_identified,
        content_condition=lambda _: True,
    ):
        super().__init__(render, render_condition=render_condition, content_condition=content_condition)

    @staticmethod
    def react(state: State, event: Event):
        if event is INIT_EVENT:
            state.connected = True
        else:
            if event is DISCONNECT_EVENT:
                state.connected = False
        return state

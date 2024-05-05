# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/elements/touch.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1886 bytes
from ...base import listenable_property, listens
from ...live import song
from . import ButtonElement


class TouchElement(ButtonElement):
    __events__ = ("assignment",)

    def __init__(self, *a, encoder=None, **k):
        (super().__init__)(*a, **k)
        self._TouchElement__on_parameter_changed.subject = encoder
        self._TouchElement__on_parameter_name_changed.subject = encoder
        self._TouchElement__on_parameter_value_changed.subject = encoder
        self._encoder = encoder

    @listenable_property
    def controlled_parameter(self):
        return self._encoder.mapped_object

    def receive_value(self, value):
        super().receive_value(value)
        if value:
            song().begin_undo_step()
        else:
            song().end_undo_step()

    @listens("parameter")
    def __on_parameter_changed(self):
        self.notify_assignment()

    @listens("parameter_name")
    def __on_parameter_name_changed(self):
        self.notify_controlled_parameter()

    @listens("parameter_value")
    def __on_parameter_value_changed(self):
        self.notify_controlled_parameter()

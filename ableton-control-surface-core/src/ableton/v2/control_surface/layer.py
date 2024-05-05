# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/layer.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 7553 bytes
from itertools import repeat

from future.utils import iteritems

from ..base import Disconnectable, nop
from .control_element import ControlElementClient, get_element
from .resource import CompoundResource, ExclusiveResource


class LayerError(Exception):
    pass


class UnhandledElementError(LayerError):
    pass


class SimpleLayerOwner(Disconnectable):
    def __init__(self, layer=None):
        self._layer = layer
        self._layer.grab(self)

    def disconnect(self):
        self._layer.release(self)


class LayerClient(ControlElementClient):
    def __init__(self, layer=None, layer_client=None, *a, **k):
        (super().__init__)(*a, **k)
        self.layer_client = layer_client
        self.layer = layer

    def set_control_element(self, control_element, grabbed):
        layer = self.layer
        owner = self.layer_client
        names = layer._element_to_names[control_element]
        if not grabbed:
            control_element = None
        for name in names:
            try:
                handler = getattr(owner, "set_" + name)
            except AttributeError:
                try:
                    control = getattr(owner, name)
                    handler = control.set_control_element
                except AttributeError:
                    if name[0] != "_":
                        raise UnhandledElementError(f"Component {owner!s} has no handler for control_element {name}")
                    else:
                        handler = nop

            handler(control_element or None)
            layer._name_to_elements[name] = control_element


class CompoundLayer(CompoundResource):
    @property
    def priority(self):
        return self.first.priority

    @priority.setter
    def priority(self, priority):
        self.first.priority = priority
        self.second.priority = priority

    def __getattr__(self, key):
        try:
            return getattr(self.first, key)
        except AttributeError:
            return getattr(self.second, key)


class LayerBase(ExclusiveResource):
    def __init__(self, priority=None, *a, **k):
        (super().__init__)(*a, **k)
        self._priority = priority

    def __add__(self, other):
        return CompoundLayer(self, other)

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, priority):
        if priority != self._priority:
            if self.owner:
                raise RuntimeError("Cannot change priority of a layer while it's owned")
            self._priority = priority

    def grab(self, client, *a, **k):
        if client == self.owner:
            (self.on_received)(client, *a, **k)
            return True
        return (super().grab)(client, *a, **k)


class Layer(LayerBase):
    def __init__(self, priority=None, **elements):
        super().__init__()
        self._priority = priority
        self._name_to_elements = dict(zip(list(elements), repeat(None)))
        self._element_to_names = {}
        self._element_clients = {}
        for name, element in iteritems(elements):
            self._element_to_names.setdefault(get_element(element), []).append(name)

    def __getattr__(self, name):
        try:
            return self._name_to_elements[name]
        except KeyError:
            raise AttributeError

    def on_received(self, client, *a, **k):
        for element in self._element_to_names:
            k.setdefault("priority", self._priority)
            (element.resource.grab)(self._get_control_client(client), *a, **k)

    def on_lost(self, client):
        for element in self._element_to_names:
            element.resource.release(self._get_control_client(client))

    def _get_control_client(self, client):
        try:
            element_client = self._element_clients[client]
        except KeyError:
            element_client = self._element_clients[client] = LayerClient(layer_client=client, layer=self)

        return element_client


class BackgroundLayer(LayerBase):
    def __init__(self, *elements, **k):
        (super().__init__)(**k)
        self._elements = [get_element(element) for element in elements]

    def on_received(self, client, *a, **k):
        for element in self._elements:
            k.setdefault("priority", self._priority)
            (element.resource.grab)(self, *a, **k)

    def on_lost(self, client):
        for element in self._elements:
            element.resource.release(self)

    def set_control_element(self, control_element, grabbed):
        if grabbed:
            control_element.reset()

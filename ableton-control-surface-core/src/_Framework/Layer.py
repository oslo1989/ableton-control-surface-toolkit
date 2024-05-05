# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Framework/Layer.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 6736 bytes
from itertools import repeat

from future.utils import raise_

from .ControlElement import ControlElementClient
from .Disconnectable import Disconnectable
from .Resource import CompoundResource, ExclusiveResource
from .Util import nop


class LayerError(Exception):
    pass


class UnhandledControlError(LayerError):
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
        names = layer._control_to_names[control_element]
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
                        raise_(
                            UnhandledControlError,
                            f"Component {owner!s} has no handler for control_element {name}",
                        )
                    else:
                        handler = nop

            handler(control_element or None)
            layer._name_to_controls[name] = control_element


class LayerBase:
    pass


class CompoundLayer(LayerBase, CompoundResource):
    def _get_priority(self):
        return self.first.priority

    def _set_priority(self, priority):
        self.first.priority = priority
        self.second.priority = priority

    priority = property(_get_priority, _set_priority)

    def __getattr__(self, key):
        try:
            return getattr(self.first, key)
        except AttributeError:
            return getattr(self.second, key)


class Layer(LayerBase, ExclusiveResource):
    def __init__(self, priority=None, **controls):
        super().__init__()
        self._priority = priority
        self._name_to_controls = dict(zip(iter(controls.keys()), repeat(None)))
        self._control_to_names = {}
        self._control_clients = {}
        for name, control in controls.items():
            self._control_to_names.setdefault(control, []).append(name)

    def __add__(self, other):
        return CompoundLayer(self, other)

    def _get_priority(self):
        return self._priority

    def _set_priority(self, priority):
        if priority != self._priority:
            if self.owner:
                raise RuntimeError("Cannot change priority of a layer while it's owned")
            self._priority = priority

    priority = property(_get_priority, _set_priority)

    def __getattr__(self, name):
        try:
            return self._name_to_controls[name]
        except KeyError:
            raise AttributeError

    def grab(self, client, *a, **k):
        if client == self.owner:
            (self.on_received)(client, *a, **k)
            return True
        return (super().grab)(client, *a, **k)

    def on_received(self, client, *a, **k):
        for control in self._control_to_names:
            k.setdefault("priority", self._priority)
            (control.resource.grab)(self._get_control_client(client), *a, **k)

    def on_lost(self, client):
        for control in self._control_to_names:
            control.resource.release(self._get_control_client(client))

    def _get_control_client(self, client):
        try:
            control_client = self._control_clients[client]
        except KeyError:
            control_client = self._control_clients[client] = LayerClient(layer_client=client, layer=self)

        return control_client

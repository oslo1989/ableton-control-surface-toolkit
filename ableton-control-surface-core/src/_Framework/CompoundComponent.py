# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Framework/CompoundComponent.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 2000 bytes
from .ControlSurfaceComponent import ControlSurfaceComponent


class CompoundComponent(ControlSurfaceComponent):
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._sub_components = []

    def update_all(self):
        self.update()
        for component in self._sub_components:
            component.update_all()

    def register_component(self, component):
        component._set_enabled_recursive(self.is_enabled())
        self._sub_components.append(component)
        return component

    def register_components(self, *a):
        return list(map(self.register_component, a))

    def has_component(self, component):
        return component in self._sub_components

    def set_enabled(self, enable):
        super().set_enabled(enable)
        for component in self._sub_components:
            component._set_enabled_recursive(self.is_enabled())

    def _set_enabled_recursive(self, enable):
        super()._set_enabled_recursive(enable)
        for component in self._sub_components:
            component._set_enabled_recursive(self.is_enabled())

    def set_allow_update(self, allow_updates):
        allow = bool(allow_updates)
        if self._allow_updates != allow:
            for component in self._sub_components:
                component.set_allow_update(allow)

            super().set_allow_update(allow)

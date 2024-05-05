# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Framework/Proxy.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 3335 bytes
from future.utils import raise_

from ableton.v2.base import old_hasattr

from .Util import BooleanContext


class ProxyBase:
    _skip_wrapper_lookup = None

    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._skip_wrapper_lookup = BooleanContext()

    def proxy_old_hasattr(self, attr):
        with self._skip_wrapper_lookup():
            return old_hasattr(self, attr)

    def __getattr__(self, name):
        if not self._skip_wrapper_lookup:
            obj = self.proxied_object
            interface = self.proxied_interface
            if obj:
                if old_hasattr(interface, name):
                    return getattr(obj, name)
            return getattr(interface, name)
        raise_(AttributeError, "Does not have attribute %s" % name)
        return None

    def __setattr__(self, name, value):
        obj = self.proxied_object
        interface = self.proxied_interface
        if obj and old_hasattr(interface, name):
            if self.proxy_old_hasattr(name):
                raise_(AttributeError, f"Ambiguous set attribute: {name} proxied: {obj}")
            setattr(obj, name, value)
        else:
            if old_hasattr(interface, name):
                raise_(AttributeError, f"Ambiguous set attribute: {name} proxied: {obj}")
            self.__dict__[name] = value

    @property
    def proxied_object(self):
        pass

    @property
    def proxied_interface(self):
        obj = self.proxied_object
        return getattr(obj, "proxied_interface", obj)


class Proxy(ProxyBase):
    proxied_object = None
    _proxied_interface = None

    @property
    def proxied_interface(self):
        return self._proxied_interface or super().proxied_interface

    def __init__(self, proxied_object=None, proxied_interface=None, *a, **k):
        (super().__init__)(*a, **k)
        self.proxied_object = proxied_object
        self._proxied_interface = proxied_interface

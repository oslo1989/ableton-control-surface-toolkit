# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/real_time_channel.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 3005 bytes
from ableton.v2.base import depends, listenable_property, liveobj_changed
from ableton.v2.control_surface import Component


def update_real_time_attachments(real_time_data_components):
    for d in real_time_data_components:
        d.detach()

    for d in real_time_data_components:
        d.attach()


class RealTimeDataComponent(Component):
    __events__ = ("attached",)

    @depends(real_time_mapper=None, register_real_time_data=None)
    def __init__(self, real_time_mapper=None, register_real_time_data=None, channel_type=None, *a, **k):
        (super().__init__)(*a, **k)
        self._channel_type = channel_type
        self._real_time_channel_id = ""
        self._object_id = ""
        self._real_time_mapper = real_time_mapper
        self._data = None
        self._valid = True
        register_real_time_data(self)

    def disconnect(self):
        super().disconnect()
        self._data = None

    @listenable_property
    def channel_id(self):
        return self._real_time_channel_id

    @listenable_property
    def object_id(self):
        return self._object_id

    @property
    def attached_object(self):
        return self._data

    def on_enabled_changed(self):
        super().on_enabled_changed()
        self.invalidate()
        self._update_attachment()

    def _update_attachment(self):
        self.detach()
        self.attach()

    def set_data(self, data):
        if liveobj_changed(data, self._data):
            self._data = data
            self.invalidate()

    def invalidate(self):
        self._valid = False

    def detach(self):
        if not self._valid:
            if self._real_time_channel_id != "":
                self._real_time_mapper.detach_channel(self._real_time_channel_id)
                self._real_time_channel_id = ""

    def device_visualisation(self):
        return self._real_time_mapper.device_visualisation

    def attach(self):
        if not self._valid:
            data = self._data if self.is_enabled() else None
            if data is not None:
                self._real_time_channel_id, self._object_id = self._real_time_mapper.attach_object(
                    data,
                    self._channel_type,
                )
            self.notify_channel_id()
            self.notify_object_id()
            self._valid = True
            self.notify_attached()

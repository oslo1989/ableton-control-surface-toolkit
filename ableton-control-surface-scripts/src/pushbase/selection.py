# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/pushbase/selection.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 3222 bytes
import Live


class Selection:
    @property
    def selected_device(self):
        raise NotImplementedError

    @property
    def selected_object(self):
        raise NotImplementedError

    @property
    def selected_track(self):
        raise NotImplementedError

    @property
    def selected_scene(self):
        raise NotImplementedError

    @property
    def hotswap_target(self):
        raise NotImplementedError


class PushSelection(Selection):
    def __init__(self, application=None, device_component=None, navigation_component=None, *a, **k):
        (super().__init__)(*a, **k)
        self._device_component = device_component
        self._navigation_component = navigation_component
        self._application = application
        self._browser = application.browser

    @property
    def selected_device(self):
        return self._device_component.device()

    def _get_selected_object(self):
        return self._navigation_component.selected_object

    def _set_selected_object(self, lom_object):
        if isinstance(lom_object, Live.DrumPad.DrumPad):
            lom_object.canonical_parent.view.selected_drum_pad = lom_object
        if isinstance(lom_object, Live.Chain.Chain):
            lom_object.canonical_parent.view.selected_chain = lom_object
        else:
            self._application.get_document().view.select_device(lom_object, False)

    selected_object = property(_get_selected_object, _set_selected_object)

    @property
    def selected_track(self):
        return self._application.get_document().view.selected_track

    @property
    def hotswap_target(self):
        return self._browser.hotswap_target

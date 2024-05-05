# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/browser_modes.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 4548 bytes
import Live
from ableton.v2.base import depends, liveobj_valid
from ableton.v2.control_surface.mode import LazyEnablingMode, Mode, ModeButtonBehaviour
from pushbase.browser_modes import BrowserHotswapMode
from pushbase.device_chain_utils import is_empty_drum_pad


def get_filter_type_for_track(song):
    has_midi_support = song.view.selected_track.has_midi_input
    if has_midi_support:
        return Live.Browser.FilterType.midi_track_devices
    return Live.Browser.FilterType.audio_effect_hotswap


class BrowserModeBehaviour(ModeButtonBehaviour):
    def press_immediate(self, component, mode):
        if mode == component.selected_mode:
            component.selected_mode = component.active_modes[0]
        else:
            component.push_mode(mode)


class BrowserComponentMode(LazyEnablingMode):
    def __init__(self, model_ref, *a, **k):
        (super().__init__)(*a, **k)
        self._model_ref = model_ref

    def enter_mode(self):
        model = self._model_ref()
        model.browserView = self.enableable
        model.browserData = self.enableable
        super().enter_mode()


class BrowseModeBase(Mode):
    def __init__(self, enabling_mode=None, *a, **k):
        super().__init__()
        self.enabling_mode = enabling_mode

    def enter_mode(self):
        self.enabling_mode.enter_mode()

    def leave_mode(self):
        self.enabling_mode.leave_mode()


class HotswapBrowseMode(BrowseModeBase):
    def __init__(self, application, drum_group_component, *a, **k):
        (super().__init__)(*a, **k)
        self._hotswap_mode = BrowserHotswapMode(application=application)
        self._in_hotswap_mode = False
        self._drum_group_component = drum_group_component

    def leave_mode(self):
        super().leave_mode()
        if self._in_hotswap_mode:
            self._hotswap_mode.leave_mode()
            self._drum_group_component.hotswap_indication_mode = None

    def _enter_hotswap_mode(self):
        self._hotswap_mode.enter_mode()
        self._in_hotswap_mode = True
        hotswap_target = self._browser.hotswap_target
        if liveobj_valid(hotswap_target):
            if isinstance(hotswap_target, Live.DrumPad.DrumPad):
                self._drum_group_component.hotswap_indication_mode = "current_pad"
            else:
                if isinstance(hotswap_target, Live.RackDevice.RackDevice):
                    if hotswap_target.can_have_drum_pads:
                        if hotswap_target == self._drum_group_component.drum_group_device:
                            self._drum_group_component.hotswap_indication_mode = "all_pads"


class AddDeviceMode(HotswapBrowseMode):
    @depends(selection=None)
    def __init__(self, song, browser, selection=None, *a, **k):
        (super().__init__)(*a, **k)
        self._song = song
        self._browser = browser
        self._selection = selection

    def enter_mode(self):
        if is_empty_drum_pad(self._selection.selected_object):
            self._enter_hotswap_mode()
            self._browser.filter_type = Live.Browser.FilterType.disabled
        else:
            self._browser.hotswap_target = None
            self._browser.filter_type = get_filter_type_for_track(self._song)
        super().enter_mode()


class AddTrackMode(BrowseModeBase):
    def __init__(self, browser, *a, **k):
        (super().__init__)(*a, **k)
        self._browser = browser

    def enter_mode(self):
        self._browser.hotswap_target = None
        super().enter_mode()


class BrowseMode(HotswapBrowseMode):
    def __init__(self, song, browser, *a, **k):
        (super().__init__)(*a, **k)
        self._song = song
        self._browser = browser

    def enter_mode(self):
        if self.enabling_mode.enableable.browse_for_audio_clip:
            self._browser.filter_type = Live.Browser.FilterType.samples
        else:
            self._enter_hotswap_mode()
            if liveobj_valid(self._browser.hotswap_target):
                self._browser.filter_type = Live.Browser.FilterType.disabled
            else:
                self._browser.filter_type = get_filter_type_for_track(self._song)
        super().enter_mode()

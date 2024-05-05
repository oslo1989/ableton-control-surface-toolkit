# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push/mode_behaviours.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 5330 bytes
from ableton.v2.control_surface.mode import ModeButtonBehaviour


class CancellableBehaviour(ModeButtonBehaviour):
    _previous_mode = None

    def press_immediate(self, component, mode):
        active_modes = component.active_modes
        groups = component.get_mode_groups(mode)
        can_cancel_mode = mode in active_modes or any(
            groups & component.get_mode_groups(other) for other in active_modes
        )
        if can_cancel_mode:
            if groups:
                component.pop_groups(groups)
            else:
                component.pop_mode(mode)
            self.restore_previous_mode(component)
        else:
            self.remember_previous_mode(component)
            component.push_mode(mode)

    def remember_previous_mode(self, component):
        self._previous_mode = component.active_modes[0] if component.active_modes else None

    def restore_previous_mode(self, component):
        if len(component.active_modes) == 0:
            if self._previous_mode is not None:
                component.push_mode(self._previous_mode)


class AlternativeBehaviour(CancellableBehaviour):
    def __init__(self, alternative_mode=None, *a, **k):
        (super().__init__)(*a, **k)
        self._alternative_mode = alternative_mode

    def _check_mode_groups(self, component, mode):
        mode_groups = component.get_mode_groups(mode)
        alt_group = component.get_mode_groups(self._alternative_mode)
        return mode_groups and mode_groups & alt_group

    def release_delayed(self, component, mode):
        component.pop_groups(component.get_mode_groups(mode))
        self.restore_previous_mode(component)

    def press_delayed(self, component, mode):
        self.remember_previous_mode(component)
        component.push_mode(self._alternative_mode)

    def release_immediate(self, component, mode):
        super().press_immediate(component, mode)

    def press_immediate(self, component, mode):
        pass


class DynamicBehaviourMixin(ModeButtonBehaviour):
    def __init__(self, mode_chooser=None, *a, **k):
        (super().__init__)(*a, **k)
        self._mode_chooser = mode_chooser
        self._chosen_mode = None

    def press_immediate(self, component, mode):
        self._chosen_mode = self._mode_chooser() or mode
        super().press_immediate(component, self._chosen_mode)

    def release_delayed(self, component, mode):
        super().release_delayed(component, self._chosen_mode)

    def press_delayed(self, component, mode):
        super().press_delayed(component, self._chosen_mode)

    def release_immediate(self, component, mode):
        super().release_immediate(component, self._chosen_mode)


class ExcludingBehaviourMixin(ModeButtonBehaviour):
    def __init__(self, excluded_groups=None, *a, **k):
        if excluded_groups is None:
            excluded_groups = set()
        (super().__init__)(*a, **k)
        self._excluded_groups = set(excluded_groups)

    def is_excluded(self, component, selected):
        return bool(component.get_mode_groups(selected) & self._excluded_groups)

    def press_immediate(self, component, mode):
        if not self.is_excluded(component, component.selected_mode):
            super().press_immediate(component, mode)

    def release_delayed(self, component, mode):
        if not self.is_excluded(component, component.selected_mode):
            super().release_delayed(component, mode)

    def press_delayed(self, component, mode):
        if not self.is_excluded(component, component.selected_mode):
            super().press_delayed(component, mode)

    def release_immediate(self, component, mode):
        if not self.is_excluded(component, component.selected_mode):
            super().release_immediate(component, mode)

    def update_button(self, component, mode, selected_mode):
        component.get_mode_button(mode).enabled = not self.is_excluded(component, selected_mode)

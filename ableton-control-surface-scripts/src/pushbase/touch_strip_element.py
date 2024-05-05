# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/pushbase/touch_strip_element.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 5702 bytes
import Live
from ableton.v2.base import NamedTuple, clamp, in_range, nop
from ableton.v2.control_surface import MIDI_PB_TYPE, InputControlElement

MAX_PITCHBEND = 16384.0


class TouchStripModes:
    (
        CUSTOM_PITCHBEND,
        CUSTOM_VOLUME,
        CUSTOM_PAN,
        CUSTOM_DISCRETE,
        CUSTOM_FREE,
        PITCHBEND,
        VOLUME,
        PAN,
        DISCRETE,
        MODWHEEL,
        COUNT,
    ) = list(range(11))


class TouchStripStates:
    STATE_OFF, STATE_HALF, STATE_FULL = list(range(3))


class TouchStripBehaviour:
    mode = NotImplemented

    def handle_touch(self, value):
        raise NotImplementedError

    def handle_value(self, value, notify):
        raise NotImplementedError


class SimpleBehaviour(TouchStripBehaviour):
    def __init__(self, mode=TouchStripModes.PITCHBEND, *a, **k):
        (super().__init__)(*a, **k)
        self._mode = mode

    @property
    def mode(self):
        return self._mode

    def handle_value(self, value, notify):
        notify(value)

    def handle_touch(self, value):
        pass


class TouchStripHandle(NamedTuple):
    range = (0, 2048)
    position = 0


class SelectingBehaviour(TouchStripBehaviour):
    handle = TouchStripHandle()
    mode = TouchStripModes.CUSTOM_FREE
    _offset = 0
    _grabbed = False

    def handle_value(self, value, notify):
        range, position = self.handle.range, self.handle.position
        if self._grabbed or range[0] <= value - position < range[1]:
            self._offset = value - position
            self._grabbed = True
        else:
            notify(clamp(value - self._offset, 0, MAX_PITCHBEND))

    def handle_touch(self, value):
        self._offset = 0
        self._grabbed = False


class DraggingBehaviour(SelectingBehaviour):
    def handle_value(self, value, notify):
        def notify_if_dragging(value):
            if self._grabbed:
                notify(value)

        super().handle_value(value, notify_if_dragging)


DEFAULT_BEHAVIOUR = SimpleBehaviour()
MODWHEEL_BEHAVIOUR = SimpleBehaviour(mode=(TouchStripModes.MODWHEEL))


class TouchStripElement(InputControlElement):
    class ProxiedInterface(InputControlElement.ProxiedInterface):
        set_mode = nop
        turn_off = nop
        turn_on_index = nop
        send_state = nop
        is_pressed = nop
        behaviour = DEFAULT_BEHAVIOUR
        state_count = 24

    state_count = 24

    def __init__(self, touch_button=None, mode_element=None, light_element=None, *a, **k):
        (super().__init__)(MIDI_PB_TYPE, 0, 0, *a, **k)
        self._mode_element = mode_element
        self._light_element = light_element
        self._touch_button = touch_button
        self._touch_slot = self.register_slot(touch_button, None, "value")
        self._force_next_behaviour = False
        self._behaviour = None
        self.behaviour = None

    @property
    def touch_button(self):
        return self._touch_button

    def _get_mode(self):
        if self._behaviour is not None:
            return self._behaviour.mode
        return None

    def set_mode(self, mode):
        if not in_range(mode, 0, TouchStripModes.COUNT):
            raise IndexError("Invalid Touch Strip Mode %d" % mode)
        self.behaviour = SimpleBehaviour(mode=mode)

    mode = property(_get_mode, set_mode)

    def _set_behaviour(self, behaviour):
        behaviour = behaviour or DEFAULT_BEHAVIOUR
        if behaviour != self._behaviour or self._force_next_behaviour:
            self._behaviour = behaviour
            self._touch_slot.listener = behaviour.handle_touch
            self._mode_element.send_value(behaviour.mode)
        self._force_next_behaviour = False

    def _get_behaviour(self):
        return self._behaviour

    behaviour = property(_get_behaviour, _set_behaviour)

    def message_map_mode(self):
        return Live.MidiMap.MapMode.absolute_14_bit

    def is_pressed(self):
        return self._touch_button is not None and self._touch_button.is_pressed()

    def reset(self):
        self.behaviour = None

    def clear_send_cache(self):
        self._force_next_behaviour = True
        super().clear_send_cache()

    def notify_value(self, value):
        notify = super().notify_value
        self._behaviour.handle_value(value, notify)

    def turn_on_index(self, index, on_state=TouchStripStates.STATE_FULL, off_state=TouchStripStates.STATE_OFF):
        states = [off_state] * self.state_count
        states[index] = on_state
        self.send_state(states)

    def turn_off(self, off_state=TouchStripStates.STATE_OFF):
        self.send_state((off_state,) * self.state_count)

    def send_state(self, state):
        if self._behaviour.mode == TouchStripModes.CUSTOM_FREE:
            self._light_element.send_value(state)
        else:
            pass

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Akai_Force_MPC/ping_pong.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1881 bytes
from ableton.v2.base import task
from ableton.v2.control_surface import Component
from ableton.v2.control_surface.control.control import InputControl

PING_PERIOD = 3


class PingPongComponent(Component):
    pong = InputControl()

    def __init__(self, on_pong_callback=None, on_ping_timeout=None, *a, **k):
        (super().__init__)(*a, **k)
        self._on_pong_callback = on_pong_callback
        self._on_ping_timeout = on_ping_timeout
        self._ping = None
        self._pong_received = False
        self._keepalive_task = self._tasks.add(
            task.sequence(task.run(self._send_ping), task.wait(PING_PERIOD), task.run(self._check_pong_received)),
        )
        self._keepalive_task.kill()
        self._keepalive_starter_task = self._tasks.add(task.run(self._keepalive_task.restart))
        self._keepalive_starter_task.kill()

    @pong.value
    def pong(self, value, _):
        self._pong_received = True
        if not self._keepalive_task.is_running:
            self._keepalive_starter_task.restart()
        self._on_pong_callback(value)

    def set_ping(self, button):
        self._ping = button
        self._keepalive_starter_task.restart()

    def _send_ping(self):
        if self._ping:
            if self.is_enabled():
                self._pong_received = False
                self._ping.send_value(0)

    def _check_pong_received(self):
        if not self._pong_received:
            self._keepalive_task.kill()
            self._on_ping_timeout()
        else:
            self._keepalive_starter_task.restart()

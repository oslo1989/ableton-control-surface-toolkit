# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/base/task.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 11776 bytes
import functools
import logging
import traceback

from past.utils import old_div

from .dependency import depends
from .util import const, find_if, nop, remove_if
from .util import linear as linear_fn

logger = logging.getLogger(__name__)


class TaskError(Exception):
    pass


KILLED = 0
RUNNING = 1
PAUSED = 2


class Task:
    def __init__(self, *a, **k):
        (super().__init__)(*a, **k)
        self._state = RUNNING
        self._next = []
        self._task_manager = None

    def clear(self):
        pass

    def do_update(self, timer):
        pass

    def do_restart(self):
        pass

    def add_next(self, task):
        self._next.append(task)
        return task

    def update(self, timer):
        if self._state == RUNNING:
            self.do_update(timer)
        return self._state

    def pause(self):
        if self._state != KILLED:
            self._state = PAUSED
        return self

    def resume(self):
        if self._state != KILLED:
            self._state = RUNNING
        return self

    def toggle_pause(self):
        if self._state != KILLED:
            self._state = RUNNING if self._state == PAUSED else PAUSED
        return self

    def restart(self):
        self.do_restart()
        self._state = RUNNING
        if self._task_manager:
            if self._task_manager.find(self) is None:
                manager = self._task_manager
                self._task_manager = None
                manager.add(self)
        return self

    def kill(self):
        self._state = KILLED
        if self._task_manager:
            for task in self._next:
                self._task_manager.add(task)

        return self

    @property
    def is_running(self):
        return self._state == RUNNING

    @property
    def is_paused(self):
        return self._state == PAUSED

    @property
    def is_killed(self):
        return self._state == KILLED

    @property
    def state(self):
        return self._state

    @property
    def parent_task(self):
        return self._task_manager

    def _set_parent(self, manager):
        if self._task_manager:
            if manager:
                raise TaskError("Already attached to: " + str(self._task_manager))
        self._task_manager = manager

    def _task_equivalent(self, other):
        return self == other


class WrapperTask(Task):
    def __init__(self, wrapped_task=None, *a, **k):
        (super().__init__)(*a, **k)
        self.wrapped_task = wrapped_task

    def update(self, delta):
        super().update(delta)
        self.wrapped_task.update(delta)

    def _set_parent(self, manager):
        super()._set_parent(manager)
        self.wrapped_task._set_parent(manager)

    def _task_equivalent(self, other):
        return self.wrapped_task._task_equivalent(other)


class FuncTask(Task):
    def __init__(self, func=None, equivalent=None, *a, **k):
        (super().__init__)(*a, **k)
        self._func = func
        self._equivalent = equivalent

    @property
    def func(self):
        return self._orig

    @func.setter
    def func(self, func):
        self._func = func

    def do_update(self, timer):
        super().do_update(timer)
        action = self._func(timer)
        if not action or action == KILLED:
            self.kill()
        else:
            if action == PAUSED:
                self.pause()

    def _task_equivalent(self, other):
        return other in (self, self._func, self._equivalent)


class GeneratorTask(Task):
    class Param:
        delta = 0

    def __init__(self, generator=None, equivalent=None, *a, **k):
        (super().__init__)(*a, **k)
        self._param = GeneratorTask.Param()
        self.generator = generator
        self._equivalent = equivalent

    @property
    def generator(self):
        return self._orig

    @generator.setter
    def generator(self, generator):
        self._orig = generator
        self._iter = generator(self._param)

    def do_update(self, delta):
        super().do_update(delta)
        self._param.delta = delta
        try:
            action = next(self._iter)
        except StopIteration:
            action = KILLED

        if not action or action == KILLED:
            self.kill()
        else:
            if action == PAUSED:
                self.pause()

    def _task_equivalent(self, other):
        return other in (self, self._orig, self._equivalent)


class TaskGroup(Task):
    auto_kill = True
    auto_remove = True
    loop = False

    def __init__(self, tasks=None, auto_kill=None, auto_remove=None, loop=None, *a, **k):
        if tasks is None:
            tasks = []
        (super().__init__)(*a, **k)
        if auto_kill is not None:
            self.auto_kill = auto_kill
        if auto_remove is not None:
            self.auto_remove = auto_remove
        if loop is not None:
            self.loop = loop
        self._tasks = []
        for task in tasks:
            self.add(task)

    def clear(self):
        for t in self._tasks:
            t._set_parent(None)

        self._tasks = []
        super().clear()

    @depends(traceback=(const(traceback)))
    def do_update(self, timer, traceback=None):
        super().do_update(timer)
        for task in self._tasks:
            if not task.is_killed:
                try:
                    task.update(timer)
                except Exception:
                    task.kill()
                    logger.error("Error when executing task")
                    traceback.print_exc()

        if self.auto_remove:
            self._tasks = remove_if(lambda t: t.is_killed, self._tasks)
        all_killed = len(list(filter(lambda t: t.is_killed, self._tasks))) == self.count
        if self.auto_kill and all_killed:
            self.kill()
        else:
            if self.loop:
                if all_killed:
                    self.restart()

    def add(self, task):
        task = totask(task)
        task._set_parent(self)
        self._tasks.append(task)
        if self.is_killed:
            super().restart()
        return task

    def remove(self, task):
        self._tasks.remove(task)
        task._set_parent(None)

    def find(self, task):
        return find_if(lambda t: t._task_equivalent(task), self._tasks)

    def restart(self):
        super().restart()
        for x in self._tasks:
            x.restart()

    @property
    def count(self):
        return len(self._tasks)


class WaitTask(Task):
    duration = 1.0

    def __init__(self, duration=None, *a, **k):
        (super().__init__)(*a, **k)
        if duration is not None:
            self.duration = duration
        self.remaining = self.duration

    def do_update(self, delta):
        super().do_update(delta)
        self.remaining -= delta
        if self.remaining <= 0:
            self.kill()
            self.remaining = 0

    def do_restart(self):
        self.remaining = self.duration


class DelayTask(Task):
    duration = 1

    def __init__(self, duration=None, *a, **k):
        (super().__init__)(*a, **k)
        if duration is not None:
            self.duration = duration
        self.remaining = self.duration

    def do_restart(self):
        self.remaining = self.duration

    def do_update(self, delta):
        super().do_update(delta)
        self.remaining -= 1
        if self.remaining <= 0:
            self.kill()
            self.remaining = 0


class TimerTask(WaitTask):
    def do_update(self, timer):
        super().do_update(timer)
        if self.remaining == 0:
            self.on_finish()
        else:
            self.on_tick()

    def on_tick(self):
        pass

    def on_finish(self):
        pass


class FadeTask(Task):
    def __init__(self, func=lambda x: x, duration=1.0, loop=False, init=False, *a, **k):
        (super().__init__)(*a, **k)
        self.func = func
        self.curr = 0.0
        self.loop = loop
        self.duration = duration
        if init:
            func(0.0)

    def do_update(self, delta):
        super().do_update(delta)
        self.func(old_div(self.curr, self.duration))
        self.curr += delta
        if self.curr >= self.duration:
            if self.loop:
                self.curr -= self.duration
            else:
                self.curr = self.duration
                self.kill()
                self.func(old_div(self.curr, self.duration))

    def do_restart(self):
        super().do_restart()
        self.curr = 0.0


class SequenceTask(Task):
    def __init__(self, tasks=None, *a, **k):
        if tasks is None:
            tasks = []
        (super().__init__)(*a, **k)
        self._tasks = tasks
        self._iter = iter(tasks)
        self._current = None
        self._advance_sequence()

    def _advance_sequence(self):
        try:
            self._current = next(self._iter)
        except StopIteration:
            self.kill()

    def do_update(self, delta):
        super().do_update(delta)
        if self._current is not None:
            self._current.update(delta)
            if self._current.is_killed:
                self._advance_sequence()

    def do_restart(self):
        for x in self._tasks:
            x.restart()

        self._iter = iter(self._tasks)
        self._advance_sequence()


class TimedCallbackTask(SequenceTask):
    _callback = nop

    def start(self, duration, callback):
        if duration is not None:
            self._tasks = [DelayTask(duration), FuncTask(self._call)]
            self._callback = callback or nop
        else:
            self._tasks = []
        self.restart()

    def _call(self, _time_expired):
        self.cancel()
        self._callback()

    def cancel(self):
        self.kill()


def totask(task):
    if not isinstance(task, Task):
        if not callable(task):
            raise TaskError("You can add either tasks or callables. " + str(task))
        task = FuncTask(func=task)
    return task


def generator(orig):
    equiv = [None]

    @functools.wraps(orig)
    def wrapper():
        return GeneratorTask(orig, equiv[0])

    equiv[0] = wrapper
    return wrapper


def sequence(*tasks):
    return SequenceTask(list(map(totask, tasks)))


def parallel(*tasks):
    return TaskGroup(tasks=tasks, auto_remove=False)


def loop(*tasks):
    return TaskGroup(tasks=tasks, auto_remove=False, auto_kill=False, loop=True)


wait = WaitTask
fade = FadeTask
delay = DelayTask


def invfade(f, *a, **k):
    return fade(lambda x: f(1.0 - x), *a, **k)


def linear(f, min, max, *a, **k):
    return fade(lambda x: f(linear_fn(min, max, x)), *a, **k)


try:
    import math

    def sinusoid(f, min=0.0, max=1.0, *a, **k):
        return fade(lambda x: f(min + (max - min) * math.sin(x * old_div(math.pi, 2.0))), *a, **k)


except ImportError:
    try:
        pass
    finally:
        err = None
        del err


def run(func, *a, **k):
    return FuncTask(
        lambda t: None if func(*a, **k) else None,
    )


def repeat(task):
    task = totask(task)
    task.kill = task.restart
    return WrapperTask(task)

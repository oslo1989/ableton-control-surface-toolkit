# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Framework/SubjectSlot.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 13732 bytes
import contextlib
from functools import partial, wraps
from itertools import repeat

from future.utils import with_metaclass
from past.builtins import basestring

from .Disconnectable import CompoundDisconnectable, Disconnectable
from .Signal import Signal
from .Util import NamedTuple, instance_decorator, mixin, monkeypatch, monkeypatch_extend


class SubjectSlotError(Exception):
    pass


class SubjectEvent(NamedTuple):
    name = None
    doc = ""
    signal = Signal
    override = False


def subject_add_event(cls, event_name_or_event):
    if isinstance(event_name_or_event, basestring):
        event = SubjectEvent(name=event_name_or_event)
    else:
        event = event_name_or_event
    signal_attr = "_" + event.name + "_signal"

    def get_signal(self):
        try:
            return getattr(self, signal_attr)
        except AttributeError:
            signal = event.signal(sender=self)
            setattr(self, signal_attr, signal)
            return signal

    kwargs = {"doc": event.doc, "override": event.override}

    @monkeypatch(cls, (event.name + "_has_listener"), **kwargs)
    def has_method(self, slot):
        return get_signal(self).is_connected(slot)

    @monkeypatch(cls, ("add_" + event.name + "_listener"), **kwargs)
    def add_method(self, slot, identify_sender=False, *a, **k):
        sender = self if identify_sender else None
        return (get_signal(self).connect)(slot, *a, sender=sender, **k)

    @monkeypatch(cls, ("remove_" + event.name + "_listener"), **kwargs)
    def remove_method(self, slot):
        return get_signal(self).disconnect(slot)

    @monkeypatch(cls, ("notify_" + event.name), **kwargs)
    def notify_method(self, *a, **k):
        return (get_signal(self))(*a, **k)

    @monkeypatch(cls, ("clear_" + event.name + "_listeners"), **kwargs)
    def clear_method(self):
        return get_signal(self).disconnect_all()

    @monkeypatch(cls, (event.name + "_listener_count"), **kwargs)
    def listener_count_method(self):
        return get_signal(self).count

    @monkeypatch_extend(cls)
    def disconnect(self):
        get_signal(self).disconnect_all()


def setup_subject(cls, listeners):
    for lst in listeners:
        subject_add_event(cls, lst)


class SubjectMeta(type):
    def __new__(cls, name, bases, dct):
        events = dct.get("__subject_events__", [])
        if events:
            if "disconnect" not in dct:
                dct["disconnect"] = lambda self: super(cls, self).disconnect()
        cls = super().__new__(cls, name, bases, dct)
        setup_subject(cls, events)
        return cls


class Subject(with_metaclass(SubjectMeta, Disconnectable)):
    pass


class SlotManager(CompoundDisconnectable):
    def register_slot(self, *a, **k):
        if a:
            slot = a[0] if isinstance(a[0], SubjectSlot) else SubjectSlot(*a, **k)
            self.register_disconnectable(slot)
            return slot
        return None

    def register_slot_manager(self, *a, **k):
        if a:
            manager = a[0] if isinstance(a[0], SlotManager) else SlotManager(*a, **k)
            self.register_disconnectable(manager)
            return manager
        return None


class SubjectSlot(Disconnectable):
    _extra_kws = {}
    _extra_args = []

    def __init__(self, subject=None, listener=None, event=None, extra_kws=None, extra_args=None, *a, **k):
        (super().__init__)(*a, **k)
        self._event = event
        if extra_kws is not None:
            self._extra_kws = extra_kws
        if extra_args is not None:
            self._extra_args = extra_args
        self._subject = None
        self._listener = None
        self.subject = subject
        self.listener = listener

    def disconnect(self):
        self.subject = None
        self.listener = None
        super().disconnect()

    def _check_subject_interface(self, subject):
        if not callable(getattr(subject, "add_" + self._event + "_listener", None)):
            raise SubjectSlotError(f'Subject {subject} missing "add" method for event: {self._event}')
        if not callable(getattr(subject, "remove_" + self._event + "_listener", None)):
            raise SubjectSlotError(f'Subject {subject} missing "remove" method for event: {self._event}')
        if not callable(getattr(subject, self._event + "_has_listener", None)):
            raise SubjectSlotError(f'Subject {subject} missing "has" method for event: {self._event}')

    def connect(self):
        if (self.is_connected or self._subject) is None or self._listener is not None:
            add_method = getattr(self._subject, "add_" + self._event + "_listener")
            all_args = (*tuple(self._extra_args), self._listener)
            with contextlib.suppress(RuntimeError):
                add_method(*all_args, **self._extra_kws)

    def soft_disconnect(self):
        if not self.is_connected and self._subject is not None or self._listener is not None:
            all_args = (*tuple(self._extra_args), self._listener)
            remove_method = getattr(self._subject, "remove_" + self._event + "_listener")
            with contextlib.suppress(RuntimeError):
                remove_method(*all_args)

    @property
    def is_connected(self):
        all_args = (*tuple(self._extra_args), self._listener)
        with contextlib.suppress(RuntimeError):
            return bool(
                self._subject is not None
                and self._listener is not None
                and (getattr(self._subject, self._event + "_has_listener"))(*all_args),
            )

    def _get_subject(self):
        return self._subject

    def _set_subject(self, subject):
        if subject != self._subject:
            if subject is not None:
                self._check_subject_interface(subject)
            self.soft_disconnect()
            self._subject = subject
            self.connect()

    subject = property(_get_subject, _set_subject)

    def _get_listener(self):
        return self._listener

    def _set_listener(self, listener):
        if listener != self._listener:
            self.soft_disconnect()
            self._listener = listener
            self.connect()

    listener = property(_get_listener, _set_listener)


class CallableSlotMixin:
    def __init__(self, function=None, *a, **k):
        (super().__init__)(*a, **k)
        self.function = function

    def __call__(self, *a, **k):
        return (self.function)(*a, **k)


class SubjectSlotGroup(SlotManager):
    listener = None
    _extra_kws = None
    _extra_args = None

    def __init__(self, listener=None, event=None, extra_kws=None, extra_args=None, *a, **k):
        (super().__init__)(*a, **k)
        self.listener = listener
        self._event = event
        if listener is not None:
            self.listener = listener
        if extra_kws is not None:
            self._extra_kws = extra_kws
        if extra_args is not None:
            self._extra_args = extra_args

    def replace_subjects(self, subjects, identifiers=repeat(None)):
        self.disconnect()
        for subject, identifier in zip(subjects, identifiers):
            self.add_subject(subject, identifier=identifier)

    def add_subject(self, subject, identifier=None):
        if identifier is None:
            identifier = subject
        listener = self._listener_for_subject(identifier)
        self.register_slot(subject, listener, self._event, self._extra_kws, self._extra_args)

    def remove_subject(self, subject):
        slot = self.find_disconnectable(
            lambda x: x.subject == subject,
        )
        self.disconnect_disconnectable(slot)

    def has_subject(self, subject):
        return (
            self.find_disconnectable(
                lambda x: x.subject == subject,
            )
            is not None
        )

    def _listener_for_subject(self, identifier):
        return lambda *a, **k: self.listener and (self.listener)(*(*a, identifier), **k)


class MultiSubjectSlot(SlotManager, SubjectSlot):
    def __init__(self, subject=None, listener=None, event=None, extra_kws=None, extra_args=None, *a, **k):
        self._original_listener = listener
        self._slot_subject = None
        self._nested_slot = None
        super().__init__(
            event=(event[0]),
            listener=(self._event_fired),
            subject=subject,
            extra_kws=extra_kws,
            extra_args=extra_args,
        )
        if len(event) > 1:
            self._nested_slot = self.register_disconnectable(
                MultiSubjectSlot(
                    event=(event[1:]),
                    listener=listener,
                    subject=subject,
                    extra_kws=extra_kws,
                    extra_args=extra_args,
                ),
            )
            self._update_nested_subject()

    def _get_subject(self):
        return super()._get_subject()

    def _set_subject(self, subject):
        try:
            try:
                super()._set_subject(subject)
            except SubjectSlotError:
                if self._nested_slot is None:
                    raise

        finally:
            self._slot_subject = subject
            self._update_nested_subject()

    subject = property(_get_subject, _set_subject)

    def _event_fired(self, *a, **k):
        self._update_nested_subject()
        (self._original_listener)(*a, **k)

    def _update_nested_subject(self):
        if self._nested_slot is not None:
            self._nested_slot.subject = (
                getattr(self._slot_subject, self._event) if self._slot_subject is not None else None
            )


def subject_slot(events, *a, **k):
    @instance_decorator
    def decorator(self, method):
        function = partial(method, self)
        event_list = events.split(".")
        num_events = len(event_list)
        event = event_list if num_events > 1 else events
        base_class = MultiSubjectSlot if num_events > 1 else SubjectSlot
        slot = wraps(method)(
            mixin(base_class, CallableSlotMixin)(
                event=event,
                extra_kws=k,
                extra_args=a,
                listener=function,
                function=function,
            ),
        )
        self.register_slot(slot)
        return slot

    return decorator


class CallableSubjectSlotGroup(SubjectSlotGroup, CallableSlotMixin):
    pass


def subject_slot_group(event, *a, **k):
    @instance_decorator
    def decorator(self, method):
        function = partial(method, self)
        slot = wraps(method)(
            CallableSubjectSlotGroup(event=event, extra_kws=k, extra_args=a, listener=function, function=function),
        )
        self.register_slot_manager(slot)
        return slot

    return decorator

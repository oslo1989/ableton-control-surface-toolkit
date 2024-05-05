# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Framework/NotifyingControlElement.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 579 bytes
from .ControlElement import ControlElement
from .SubjectSlot import Subject, SubjectEvent


class NotifyingControlElement(Subject, ControlElement):
    __subject_events__ = (
        SubjectEvent(
            name="value",
            doc=" Called when the control element receives a MIDI value\n                             from the hardware ",
        ),
    )

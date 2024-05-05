# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/APC_Key_25/MixerComponent.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 847 bytes
from _APC.MixerComponent import ChanStripComponent as ChanStripComponentBase
from _APC.MixerComponent import MixerComponent as MixerComponentBase
from _Framework.Util import nop


class ChanStripComponent(ChanStripComponentBase):
    def __init__(self, *a, **k):
        self.reset_button_on_exchange = nop
        (super().__init__)(*a, **k)


class MixerComponent(MixerComponentBase):
    def on_num_sends_changed(self):
        if self.send_index is None:
            if self.num_sends > 0:
                self.send_index = 0

    def _create_strip(self):
        return ChanStripComponent()

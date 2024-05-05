# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/layer.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 695 bytes
from ableton.v2.control_surface import Layer as LayerBaseClass


class Layer(LayerBaseClass):
    def on_received(self, client, *a, **k):
        (super().on_received)(client, *a, **k)
        client.num_layers += 1

    def on_lost(self, client):
        super().on_lost(client)
        client.num_layers -= 1

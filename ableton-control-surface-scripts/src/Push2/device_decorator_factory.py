# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/device_decorator_factory.py
# Compiled at: 2023-12-21 15:35:34
# Size of source mod 2**32: 3611 bytes
from ableton.v2.control_surface import DeviceDecoratorFactory as DeviceDecoratorFactoryBase

from .amp import AmpDeviceDecorator
from .analog import AnalogDeviceDecorator
from .auto_filter import AutoFilterDeviceDecorator
from .beatrepeat import BeatRepeatDeviceDecorator
from .cccontrol import CcControlDeviceDecorator
from .chorus2 import Chorus2DeviceDecorator
from .collision import CollisionDeviceDecorator
from .compressor import CompressorDeviceDecorator
from .corpus import CorpusDeviceDecorator
from .delay import DelayDeviceDecorator
from .device_decoration import (
    DrumBussDeviceDecorator,
    PedalDeviceDecorator,
    SamplerDeviceDecorator,
    UtilityDeviceDecorator,
)
from .drift import DriftDeviceDecorator
from .drumcell import DrumCellDeviceDecorator
from .echo import EchoDeviceDecorator
from .eq3 import EqThreeDeviceDecorator
from .eq8 import Eq8DeviceDecorator
from .filterdelay import FilterDelayDeviceDecorator
from .graindelay import GrainDelayDeviceDecorator
from .hybrid_reverb import HybridReverbDeviceDecorator
from .meld import MeldDeviceDecorator
from .operator import OperatorDeviceDecorator
from .phasernew import PhaserNewDeviceDecorator
from .redux2 import Redux2DeviceDecorator
from .resonator import ResonatorDeviceDecorator
from .reverb import ReverbDeviceDecorator
from .roar import RoarDeviceDecorator
from .saturator import SaturatorDeviceDecorator
from .shifter import ShifterDeviceDecorator
from .simpler import SimplerDeviceDecorator
from .spectral import SpectralDeviceDecorator
from .tension import TensionDeviceDecorator
from .transmute import TransmuteDeviceDecorator
from .vinyl import VinylDistortionDecorator
from .wavetable import WavetableDeviceDecorator


class DeviceDecoratorFactory(DeviceDecoratorFactoryBase):
    DECORATOR_CLASSES = {
        "Amp": AmpDeviceDecorator,
        "AutoFilter": AutoFilterDeviceDecorator,
        "BeatRepeat": BeatRepeatDeviceDecorator,
        "Chorus2": Chorus2DeviceDecorator,
        "Collision": CollisionDeviceDecorator,
        "Compressor2": CompressorDeviceDecorator,
        "Corpus": CorpusDeviceDecorator,
        "Delay": DelayDeviceDecorator,
        "Drift": DriftDeviceDecorator,
        "DrumBuss": DrumBussDeviceDecorator,
        "DrumCell": DrumCellDeviceDecorator,
        "Echo": EchoDeviceDecorator,
        "Eq8": Eq8DeviceDecorator,
        "FilterDelay": FilterDelayDeviceDecorator,
        "FilterEQ3": EqThreeDeviceDecorator,
        "GrainDelay": GrainDelayDeviceDecorator,
        "Hybrid": HybridReverbDeviceDecorator,
        "InstrumentVector": WavetableDeviceDecorator,
        "InstrumentMeld": MeldDeviceDecorator,
        "MidiCcControl": CcControlDeviceDecorator,
        "MultiSampler": SamplerDeviceDecorator,
        "OriginalSimpler": SimplerDeviceDecorator,
        "Operator": OperatorDeviceDecorator,
        "Pedal": PedalDeviceDecorator,
        "PhaserNew": PhaserNewDeviceDecorator,
        "Redux2": Redux2DeviceDecorator,
        "Resonator": ResonatorDeviceDecorator,
        "Reverb": ReverbDeviceDecorator,
        "Roar": RoarDeviceDecorator,
        "Saturator": SaturatorDeviceDecorator,
        "Spectral": SpectralDeviceDecorator,
        "StereoGain": UtilityDeviceDecorator,
        "StringStudio": TensionDeviceDecorator,
        "Shifter": ShifterDeviceDecorator,
        "Transmute": TransmuteDeviceDecorator,
        "UltraAnalog": AnalogDeviceDecorator,
        "Vinyl": VinylDistortionDecorator,
    }

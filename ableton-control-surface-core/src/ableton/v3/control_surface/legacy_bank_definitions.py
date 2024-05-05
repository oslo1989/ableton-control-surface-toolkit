# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v3/control_surface/legacy_bank_definitions.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1948 bytes
from _Generic.Devices import BANK_NAME_DICT, DEVICE_BOB_DICT, DEVICE_DICT

from ableton.v2.base.collection import IndexedDict

from ..base import memoize
from . import BANK_PARAMETERS_KEY

BEST_OF_PARAMETERS_KEY = "Best of Parameters"


@memoize
def banked():
    return {
        device_name: IndexedDict(
            [
                (bank_name, {BANK_PARAMETERS_KEY: parameters})
                for bank_name, parameters in zip(bank_names, DEVICE_DICT[device_name])
            ],
        )
        for device_name, bank_names in BANK_NAME_DICT.items()
    }


@memoize
def best_of_banks():
    return {
        device_name: IndexedDict([(BEST_OF_PARAMETERS_KEY, {BANK_PARAMETERS_KEY: parameters[0]})])
        for device_name, parameters in DEVICE_BOB_DICT.items()
    }

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_MxDCore/__init__.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 2238 bytes
import sys
import warnings

from ableton.v2.base import old_hasattr

from .MxDCore import MxDCore as _MxDCore


def set_manager(manager):
    _MxDCore.instance = _MxDCore()
    _MxDCore.instance.set_manager(manager)


def disconnect():
    _MxDCore.instance.disconnect()
    del _MxDCore.instance


def execute_command(device_id, object_id, command, arguments):
    if old_hasattr(_MxDCore.instance, command):
        try:
            with warnings.catch_warnings(record=True) as caught_warnings:
                _MxDCore.instance.update_device_context(device_id, object_id)
                function = getattr(_MxDCore.instance, command)
                function(device_id, object_id, arguments)
                for warning in caught_warnings:
                    _MxDCore.instance._print_warning(device_id, object_id, str(warning.message))

        except:
            assert_reason = str(sys.exc_info()[1]) if sys.exc_info()[0].__name__ == "RuntimeError" else "Invalid syntax"
            _MxDCore.instance._print_error(device_id, object_id, assert_reason)

    else:
        _MxDCore.instance._print_error(device_id, object_id, "Unknown command: " + command)

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_Framework/Capabilities.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 2670 bytes
from past.builtins import basestring

GENERIC_SCRIPT_KEY = "generic_script"
PORTS_KEY = "ports"
CONTROLLER_ID_KEY = "controller_id"
TYPE_KEY = "surface_type"
FIRMWARE_KEY = "firmware_version"
AUTO_LOAD_KEY = "auto_load"
VENDORID = "vendor_id"
PRODUCTIDS = "product_ids"
MODEL_NAMES = "model_names"
DIRECTIONKEY = "direction"
PORTNAMEKEY = "name"
MACNAMEKEY = "mac_name"
PROPSKEY = "props"
HIDDEN = "hidden"
SYNC = "sync"
SCRIPT = "script"
NOTES_CC = "notes_cc"
REMOTE = "remote"
PLAIN_OLD_MIDI = "plain_old_midi"


def __create_port_dict(direction, port_name, mac_name, props):
    if props:
        for prop in props:
            pass

    capabilities = {DIRECTIONKEY: direction, PORTNAMEKEY: port_name, PROPSKEY: props}
    if mac_name:
        capabilities[MACNAMEKEY] = mac_name
    return capabilities


def inport(port_name="", props=None, mac_name=None):
    if props is None:
        props = []
    return __create_port_dict("in", port_name, mac_name, props)


def outport(port_name="", props=None, mac_name=None):
    if props is None:
        props = []
    return __create_port_dict("out", port_name, mac_name, props)


def controller_id(vendor_id, product_ids, model_name):
    for product_id in product_ids:
        pass

    model_names = [model_name] if isinstance(model_name, basestring) else model_name
    return {VENDORID: vendor_id, PRODUCTIDS: product_ids, MODEL_NAMES: model_names}

# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.16 (default, Jan 17 2023, 09:28:58)
# [Clang 14.0.6 ]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/APC_Key_25_mk2/__init__.py
# Compiled at: 2023-11-21 10:21:18
# Size of source mod 2**32: 1409 bytes
from ableton.v3.control_surface import ControlSurfaceSpecification, create_control_surface, create_skin
from ableton.v3.control_surface.capabilities import (
    CONTROLLER_ID_KEY,
    HIDDEN,
    NOTES_CC,
    PORTS_KEY,
    SCRIPT,
    SYNC,
    controller_id,
    inport,
    outport,
)

from .colors import Rgb, Skin
from .elements import Elements
from .mappings import create_mappings


def get_capabilities():
    return {
        CONTROLLER_ID_KEY: controller_id(vendor_id=2536, product_ids=[78], model_name=["APC Key 25 mk2"]),
        PORTS_KEY: [
            inport(props=[NOTES_CC]),
            inport(props=[NOTES_CC, SCRIPT]),
            outport(props=[NOTES_CC]),
            outport(props=[NOTES_CC, SCRIPT, SYNC, HIDDEN]),
        ],
    }


def create_instance(c_instance):
    return create_control_surface(name="APC_Key_25_mk2", specification=Specification, c_instance=c_instance)


class Specification(ControlSurfaceSpecification):
    elements_type = Elements
    control_surface_skin = create_skin(skin=Skin, colors=Rgb)
    num_tracks = 8
    num_scenes = 5
    include_returns = True
    identity_response_id_bytes = (71, 78, 0, 25)
    create_mappings_function = create_mappings

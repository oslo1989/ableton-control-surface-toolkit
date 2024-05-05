from typing import Any

from ableton.v2.control_surface import ControlSurface

from .processor import process_module
from .writer import add_all_modules, write_module


class EnablerDocSurface(ControlSurface):
    def __init__(self, c_instance: Any) -> None:
        ControlSurface.__init__(self, c_instance)
        import Live
        import MidiRemoteScript

        clean_path = True
        for m in [Live, MidiRemoteScript]:
            mod = process_module(m)
            write_module(mod=mod, all_modules=add_all_modules(module=mod), clean_path=clean_path)
            clean_path = False

    def disconnect(self) -> None:
        ControlSurface.disconnect(self)

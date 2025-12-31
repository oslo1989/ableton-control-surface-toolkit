import traceback
from typing import Any

from ableton.v2.control_surface import ControlSurface

from .logging_utils import get_logger
from .processor import process_module
from .writer import add_all_modules, write_module

logger = get_logger(__name__)


class EnablerDocSurface(ControlSurface):
    def __init__(self, c_instance: Any) -> None:
        ControlSurface.__init__(self, c_instance)
        import Live
        import MidiRemoteScript

        logger.info("Initializing EnablerDocSurface")
        clean_path = True
        for m in [Live, MidiRemoteScript]:
            logger.info(f"Processing module: {m.__name__}")
            try:
                mod = process_module(m)
                write_module(mod=mod, all_modules=add_all_modules(module=mod), clean_path=clean_path)
            except Exception:
                logger.error(f"Failed to process or write module {m.__name__}")
                logger.error(traceback.format_exc())
            clean_path = False
        logger.info("EnablerDocSurface initialization complete")

    def disconnect(self) -> None:
        ControlSurface.disconnect(self)

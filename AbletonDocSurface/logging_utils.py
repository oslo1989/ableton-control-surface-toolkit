import logging
import os
from datetime import datetime
from typing import Optional

_shared_handler: Optional[logging.Handler] = None


def get_logger(name: str) -> logging.Logger:
    global _shared_handler
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        if _shared_handler is None:
            log_dir = os.path.join(os.path.expanduser("~"), "enabler-doc-surface-logs")
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            log_file = os.path.join(log_dir, f"{timestamp}.txt")

            _shared_handler = logging.FileHandler(log_file)
            formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            _shared_handler.setFormatter(formatter)

        logger.addHandler(_shared_handler)

    return logger

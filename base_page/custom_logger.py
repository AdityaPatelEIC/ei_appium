import logging
import inspect
import os
from colorlog import ColoredFormatter


def customLogger():
    # Get name of the file where logger is being called
    caller_file = inspect.stack()[1].filename
    log_name = os.path.splitext(os.path.basename(caller_file))[0]

    # Create logger
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.INFO)

    # Avoid adding multiple handlers
    if not logger.handlers:
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # Colored formatter
        formatter = ColoredFormatter(
            fmt="%(log_color)s%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%d/%m/%y %I:%M:%S %p %A",
            log_colors={
                'DEBUG': 'white',
                'INFO': 'white',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'bold_red',
            }
        )
        console_handler.setFormatter(formatter)

        # Add handler to logger
        logger.addHandler(console_handler)

    return logger

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

    # Prevent duplicate logs
    logger.propagate = False

    # Avoid adding multiple handlers
    if not logger.handlers:
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # Colored formatter with filename and line number for certain log levels
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

        # Create filter for ERROR, WARNING, CRITICAL
        def add_filename_line_num(record):
            # Add filename and line number for ERROR, WARNING, CRITICAL
            if record.levelname in ['ERROR', 'WARNING', 'CRITICAL']:
                record.msg = f"{record.filename}:{record.lineno} - {record.msg}"
            return record

        # Set the custom filter
        console_handler.addFilter(add_filename_line_num)
        console_handler.setFormatter(formatter)

        # Add handler to logger
        logger.addHandler(console_handler)

    return logger

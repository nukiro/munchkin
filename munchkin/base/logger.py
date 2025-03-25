from enum import Enum
from logging import DEBUG, INFO, FileHandler, Formatter, StreamHandler, getLogger
from sys import stdout as sys_stdout
from typing import Optional


class LoggingHandler(Enum):
    FILE = "file"
    STDOUT = "stdout"


def configure(
    debug: Optional[bool] = True,
    handler: Optional[LoggingHandler] = LoggingHandler.STDOUT,
    filename: Optional[str] = "log",
):
    # Configure a new formatters for out logger
    fmt = Formatter(
        fmt="[%(asctime)s] %(levelname)s \t%(message)s",
        datefmt="%Y/%m/%d %H:%M:%S",
    )
    # Configure Handler to send the logs to a given destination
    logger_handler = (
        FileHandler(f"{filename}.txt")
        if handler is LoggingHandler.FILE
        else StreamHandler(stream=sys_stdout)
    )
    logger_handler.setFormatter(fmt)

    # create a new logger
    logger = getLogger()
    # Assign the handler to the logger
    logger.addHandler(logger_handler)
    # Assign logger message level
    logger.setLevel(DEBUG if debug else INFO)

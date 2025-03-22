from logging import DEBUG, INFO, Formatter, StreamHandler, getLogger
from sys import stdout as sys_stdout
from typing import Optional


def configure(debug: Optional[bool] = True):
    # Configure a new formatters for out logger
    fmt = Formatter(
        fmt="[%(asctime)s] %(levelname)s \t%(message)s",
        datefmt="%Y/%m/%d %H:%M:%S",
    )
    # Configure Handler to send the logs to a given destination
    stdout = StreamHandler(stream=sys_stdout)
    stdout.setFormatter(fmt)

    # create a new logger
    logger = getLogger()
    # Assign the handler to the logger
    logger.addHandler(stdout)
    # Assign logger message level
    logger.setLevel(DEBUG if debug else INFO)

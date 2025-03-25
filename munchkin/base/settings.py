import os
from enum import Enum
from logging import info, warning
from os import getenv
from pathlib import Path
from typing import TypedDict

from dotenv import load_dotenv

from munchkin.base.logger import LoggingHandler
from munchkin.base.logger import configure as configure_logger
from munchkin.base.validations import validate_text


class Environment(Enum):
    LOCAL = "local"
    DEV = "development"
    TEST = "test"
    INT = "integration"
    PROD = "production"


class Settings(TypedDict):
    package: str
    environment: Environment


def _boolean_from_env(value: str) -> bool:
    if not value:
        return False

    return value.lower() in ["true", "1", "t", "y"]


def build_settings() -> Settings:
    env_file = Path(f"{os.getcwd()}/.env")
    if not env_file.exists():
        raise FileNotFoundError(f"There is no environment file on: '{os.getcwd()}'.")

    load_dotenv(dotenv_path=env_file, verbose=True, override=True)

    logging = _boolean_from_env(getenv("LOGGING"))
    if logging:
        debug = _boolean_from_env(getenv("LOGGING_DEBUG"))
        handler = LoggingHandler.STDOUT
        try:
            handler = LoggingHandler[getenv("LOGGING_HANDLER").upper()]
            configure_logger(
                debug,
                handler,
                getenv("LOGGING_FILENAME"),
            )
        except Exception:
            configure_logger(
                debug,
                handler,
                getenv("LOGGING_FILENAME"),
            )
            warning(
                "Logging handler is not defined or it is correctly defined. Default will be set."
            )

    info("-----")
    package = validate_text("Package Name", getenv("PACKAGE"))
    info(f"Package: {package}")

    # as default if value is not defined in the .env file
    env = Environment.LOCAL
    try:
        env = Environment[getenv("ENVIRONMENT").upper()]
    except Exception:
        warning(
            "Environment is not defined or it is correctly defined. Default will be set."
        )

    info(f"Environment: {env.value}")
    print()

    return dict(package=package, environment=env)

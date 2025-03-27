from enum import Enum
from typing import Type


def validate_exist(field: str, value: any) -> any:
    value_error = f"{field} must exist"

    if not value:
        raise ValueError(value_error)


def validate_text(field: str, text: str) -> str:
    # error messages
    type_error = f"{field} must be a string"
    value_error = f"{field} must be a non-empty string"

    if not isinstance(text, str):
        raise TypeError(type_error)

    if not text:
        raise ValueError(value_error)

    if text == "":
        raise ValueError(value_error)

    if text.strip() == "":
        raise ValueError(value_error)

    return text.strip()


def validate_number(field: str, number: int | float) -> int | float:
    type_error = f"{field} must be a number: integer or float"

    # a boolean in Python is an int instance
    # a custom validation for this case is required
    if isinstance(number, bool):
        raise TypeError(type_error)

    if not isinstance(number, int | float):
        raise TypeError(type_error)

    return number


def validate_positive_number(field: str, number: int | float) -> int | float:
    value_error = f"{field} must be equal or greater than zero"

    validate_number(field, number)

    if number < 0:
        raise ValueError(value_error)

    return number


def validate_email(email: str) -> str:
    field = "email"
    value_error = f"{field} must be valid"
    EMAIL_REGEX = compile(r"[^@]+@[^@]+\.[^@]+")

    validate_text(field, email)

    if not EMAIL_REGEX.match(email):
        raise ValueError(value_error)

    return email


def validate_enum(field: str, enun_class: Type[Enum], value: Enum) -> Enum:
    type_error = f"{field} must be {enun_class.__name__}"

    if not isinstance(value, enun_class):
        raise TypeError(type_error)

    return value


def validate_bool(field: str, value: bool) -> bool:
    type_error = f"{field} must be a boolean"

    if not isinstance(value, bool):
        raise TypeError(type_error)

    return value

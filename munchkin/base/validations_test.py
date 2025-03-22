from pytest import mark, raises

from munchkin.base.validations import (
    validate_email,
    validate_number,
    validate_positive_number,
    validate_text,
)


class TestValidateText:
    @mark.parametrize(
        "field,text,error,match",
        [
            ("name", 123, TypeError, "name must be a string"),
            ("name", None, TypeError, "name must be a string"),
            ("name", "", ValueError, "name must be a non-empty string"),
            ("name", "    ", ValueError, "name must be a non-empty string"),
        ],
    )
    def test_raise_exception(self, field, text, error, match):
        with raises(error, match=match):
            validate_text(field, text)

    @mark.parametrize(
        "text",
        [
            ("name"),
            ("  name "),
            ("name    "),
            ("     name"),
        ],
    )
    def test_return_text(self, text):
        assert validate_text("field", text) == "name"


class TestValidateNumber:
    @mark.parametrize(
        "field,number,error,match",
        [
            ("number", None, TypeError, "number must be a number: integer or float"),
            (
                "number",
                "this is a string",
                TypeError,
                "number must be a number: integer or float",
            ),
            ("number", True, TypeError, "number must be a number: integer or float"),
        ],
    )
    def test_raise_exception(self, field, number, error, match):
        with raises(error, match=match):
            validate_number(field, number)

    @mark.parametrize(
        "number",
        [
            (3),  # integer
            (12.3),  # float
            (7.90),  # float
            (float(3)),
            (int(6.878)),
            (0),
            (0.001),
            (0.0000000001),
        ],
    )
    def test_return_number(self, number):
        assert validate_number("number", number) == number


class TestValidatePositiveNumber:
    @mark.parametrize(
        "field,number,error,match",
        [
            (
                "number",
                -0.00000001,
                ValueError,
                "number must be equal or greater than zero",
            ),
            ("number", -1, ValueError, "number must be equal or greater than zero"),
        ],
    )
    def test_raise_exception(self, field, number, error, match):
        with raises(error, match=match):
            validate_positive_number(field, number)


class TestValidateEmail:
    @mark.parametrize(
        "email,error,match",
        [
            ("@email.com", ValueError, "email must be valid"),
            ("@.com", ValueError, "email must be valid"),
            ("a@.com", ValueError, "email must be valid"),
            ("@", ValueError, "email must be valid"),
            ("a@a", ValueError, "email must be valid"),
            ("a@", ValueError, "email must be valid"),
        ],
    )
    def test_raise_exception(self, email, error, match):
        with raises(error, match=match):
            assert validate_email(email)

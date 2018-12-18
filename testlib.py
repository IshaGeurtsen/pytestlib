"""
test library for python
written by Isha Geurtsen
"""

TESTS = []


def unit_test(func):
    "adds function to tests"
    TESTS.append(func)
    return func


class Asserts:
    "contains formated assertions"
    @staticmethod
    def equal(value, expected_value):
        "raises assertion error if not value == expected_value"
        assert value == expected_value, \
            f"{type(value)}({value}) != {type(expected_value)}({expected_value})"

    @staticmethod
    def not_equal(value, expected_value):
        "raises assertion error if not value != expected_value"
        assert value != expected_value, \
            f"{type(value)}({value}) != {type(expected_value)}({expected_value})"


def run_tests():
    "executes all registered unit tests"
    failed = []
    for test in TESTS:
        try:
            test()
        except AssertionError as error:
            failed.append([test, error])
    if failed:
        for test, error in failed:
            print(f"{test.__name__} failed, {error}")

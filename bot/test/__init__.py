"""
Tests for ensuring all features work properly for the smooth functioning of the bot later on
"""
from . import meme
from . import database

tests = [meme, database]


def run_all_tests() -> None:
    """
    Tests for ensuring all features work properly for the smooth functioning of the bot later on

    :return: None
    """
    for test in tests:
        test_result = test.run_test()
        print(f'Test "{test.__name__}":', test_result)

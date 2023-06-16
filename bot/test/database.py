"""
A Test to check if  helper classes and functions for database interaction are properly working.
"""
import os
from sqlalchemy import create_engine
from ..lib import Base, Guild


def run_test() -> bool:
    """
    A Test to check if  helper classes and functions for database interaction are properly working.

    :return: Test passed or not
    :rtype: bool
    """
    try:
        if os.path.exists("test.db"):
            os.remove("test.db")
        engine = create_engine("sqlite:///test.db")
        Base.metadata.create_all(engine)
        Base.engine = engine
        Guild.new(1234)
        Guild.update(1234, frequency=10)
        Guild.remove(1234)
        return True
    except Exception as error:  # pylint: disable=broad-exception-caught
        print(error)
        return False

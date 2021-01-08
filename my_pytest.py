#!/usr/bin/env python

"""
Author: Pawel Rydzkowski
Purpose: A test case file for the get_greetings.py.
Used to illustrate Test Driven Development (TDD) and DevOps CI/CD.
"""

import pytest
import get_greetings
#from get_greetings import get_hello
#from get_greetings import get_good_morning
#from get_greetings import get_good_evening


#@pytest.fixture

def test_get_hello():
    """
    Test the "get_hello()" function. This doesn't follow TDD since we have already 
    written the code for this function a long time ago.
    """
    assert get_greetings.get_hello().upper() == "HELLO WORLD!"

def test_get_good_morning():
    """
    Test the "get_good_morning()" function. This doesn't follow TDD since we have already 
    written the code for this function a long time ago.
    """
    assert get_greetings.get_good_morning().upper() == "GOOD MORNING!"

def test_get_good_evening():
    """
    Test the "get_good_evening()" function. This does follow TDD since we wrote 
    this test before the funciton was implemented.
    """
    assert get_greetings.get_good_evening().upper() == "GOOD EVENING!"

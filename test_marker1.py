#marker will execute only marked test

import pytest


@pytest.mark.sanity
def testLogin():
    print("Successful")


def testLogout():
    print("Failed")

def testCal():
    assert 2+2==4
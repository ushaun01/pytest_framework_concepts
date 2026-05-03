import pytest


@pytest.fixture()
def profile():
    print("What is your name")
    yield
    print("what is your surname")

def testSignin(profile):
    print("Enter details")

def testSignout(profile):
    print("Successful signin")
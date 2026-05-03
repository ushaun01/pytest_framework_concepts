import pytest


@pytest.yield_fixture()
def details():
    print("Enter Details")
    yield
    print("Welcome to Login")

def testLogin(details):
    print("Successfully Login")

def testLogout(details):
    print("Successfully Logout")
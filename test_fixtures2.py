#teardown
import pytest

@pytest.fixture()

def login():
    print("Enter Login Details")
    yield                                  #it helps next line to execute after
    print("Login Successful")



def testName(login):
    print("Enter your name")

def testPlace(login):
    print("Enter your location")

def testID():
    print("Enter Your ID")
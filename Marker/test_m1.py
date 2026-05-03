import pytest


def test_login():
    print("successfully logged")

@pytest.mark.sanity
def test_sum():
    a=2
    b=5
    assert a==b
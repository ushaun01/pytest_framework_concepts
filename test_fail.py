import pytest
@pytest.mark.xfail
def test_fail1():
    a=5
    b=10
    assert a==b
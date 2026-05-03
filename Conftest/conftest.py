import pytest

# @pytest.fixture(Autouse=True)
@pytest.fixture()                                              #scope="session"
def tc_setup():
    print("Learn browser")
    print("Login")
    print("Browse product")
    yield
    print("logout")
    print("close browser")
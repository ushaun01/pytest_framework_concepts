import pytest


@pytest.fixture(scope="session",autouse=True)                                              #scope="session"
def tc_setup(browser):
    if browser== "chrome":
        print("launch chrome")
    elif browser=="ff":
        print("launch firefox")
    else:
        print("valid browser")
    print("Learn browser")
    print("Login")
    print("Browse product")
    yield
    print("logout")
    print("close browser")


def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture(scope="session",autouse=True)
def browser(request):
    return  request.config.getoption("--browser")
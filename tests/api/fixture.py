import pytest

from actions.api_actions.register import RegisterAPI


@pytest.fixture(scope="session")
def registry():
    return RegisterAPI()

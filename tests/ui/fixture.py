import pytest

from actions.ui_actions.UIPages import UIPages


@pytest.fixture(scope="session")
def pages() -> UIPages:
    return UIPages()

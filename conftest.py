import random
import string

import allure
import pytest

from models.auth_obj import AuthObj

pytest_plugins = [
    "tests.api.fixture",
    "tests.ui.fixture",
]


HOLYWEB_DOMAIN: str = "holyweb.ru"


@pytest.fixture(scope="function")
@allure.title("Генерация данных для регистрации")
def credentials() -> AuthObj:
    password: str = generate_string(length=20)
    credentials = AuthObj(
        email=f"{generate_string(length=12)}@{HOLYWEB_DOMAIN}",
        password=password,
        confirm_password=password,
    )
    return credentials


@allure.step("Генерация строки длиной {length} символ(ов)")
def generate_string(length: int) -> str:
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))

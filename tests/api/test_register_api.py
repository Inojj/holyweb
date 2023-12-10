import allure
from assertpy import assert_that

from models.auth_obj import AuthObj


@allure.tag("API")
@allure.suite("API тесты")
@allure.sub_suite("Endpoint register")
@allure.title("Проверка регистрации")
def test_register(credentials: AuthObj, registry):
    response = registry.post_register(
        email=credentials.email,
        password=credentials.password,
        confirm_password=credentials.confirm_password,
    )
    assert_that(response.email, "Email").is_equal_to(credentials.email)

import allure
from assertpy import assert_that

from actions.api_actions.register import RegisterAPI
from models.auth_obj import AuthObj


@allure.tag("API")
@allure.title("Регистрация пользователя")
def test_register(credentials: AuthObj):
    response = RegisterAPI.post_register(
        email=credentials.email,
        password=credentials.password,
        confirm_password=credentials.confirm_password,
    )
    assert_that(response.email, "Email").is_equal_to(credentials.email)

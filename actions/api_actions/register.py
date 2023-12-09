import json

import allure
import requests
from allure_commons.types import AttachmentType

from config.config import Config
from models.auth_obj import AuthObj
from models.register_response import RegisterResponse


class RegisterAPI:
    @staticmethod
    @allure.step(
        "Отпрвка запроса на регистрацию. email: {email}, password: {password}, "
        "confirm_password: {confirm_password}"
    )
    def post_register(
        email: str, password: str, confirm_password: str
    ) -> RegisterResponse:
        body = AuthObj(
            email=email, password=password, confirm_password=confirm_password
        )
        response = requests.post(
            url=f"{Config.API_HOST}/register", json=body.model_dump()
        )
        response.raise_for_status()
        allure.attach(
            json.dumps(response.json()),
            name="Response",
            attachment_type=AttachmentType.JSON,
        )
        return RegisterResponse(**response.json())

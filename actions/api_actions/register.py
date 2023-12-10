import json

import allure
import requests
from allure_commons.types import AttachmentType
from requests import Response

from config.config import Config
from models.auth_obj import AuthObj
from models.register_response import RegisterResponse


class RegisterAPI:
    @allure.step(
        "Запрос на регистрацию. email: {email}, password: {password}, "
        "confirm_password: {confirm_password}"
    )
    def post_register(
        self, email: str, password: str, confirm_password: str
    ) -> RegisterResponse:
        body = AuthObj(
            email=email, password=password, confirm_password=confirm_password
        )
        response = requests.post(
            url=f"{Config.API_HOST}/register", json=body.model_dump()
        )
        response.raise_for_status()
        self._allure_attach(response)
        return RegisterResponse(**response.json())

    def _allure_attach(self, response: Response) -> None:
        allure.attach(
            json.dumps(self._get_response_data(response)),
            name="Response",
            attachment_type=AttachmentType.JSON,
        )

    @staticmethod
    def _get_response_data(response: Response) -> dict:
        return {
            "body": response.json(),
            "status_code": response.status_code,
            "url": response.url,
        }

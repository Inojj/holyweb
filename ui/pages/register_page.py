import allure
from playwright.sync_api import Page

from config.config import Config


class RegisterPage:
    _LOGIN: str = '//*[@id="login"]'
    _PASSWORD: str = '//*[@id="password"]//input'
    _CONFORM_PASSWORD: str = '//*[@id="confirm_password"]//input'
    _SUBMIT_BUTTON: str = "//span[@class='p-button-label']"
    STRONG_PASSWORD_PANEL: str = "#pv_id_4_panel"

    @staticmethod
    @allure.step("Открыть страницу регистрации")
    def open_register_page(page: Page) -> None:
        page.goto(f"{Config.UI_HOST}/#/register")

    @allure.step("Заполнить поле Login. Login: {login}")
    def fill_login(self, page: Page, login: str) -> None:
        page.locator(self._LOGIN).press_sequentially(login)

    @allure.step("Заполнить поле Password. Password: {password}")
    def fill_password(self, page: Page, password: str) -> None:
        page.locator(self._PASSWORD).press_sequentially(password)

    @allure.step(
        "Заполненить поле Confirm password. Confirm password: {confirm_password}"
    )
    def fill_confirm_password(self, page: Page, confirm_password: str) -> None:
        page.locator(self._CONFORM_PASSWORD).press_sequentially(confirm_password)
        page.click(self.STRONG_PASSWORD_PANEL)

    @allure.step("Нажать кнопку submit")
    def click_submit_button(self, page: Page) -> None:
        page.click(self._SUBMIT_BUTTON)

import allure
from playwright.sync_api import Page

from config.config import Config


class ProfilePage:
    NO_RECORD_TEXT: str = "No records found."
    EMPTY_MESSAGE: str = "//div[@class='p-dataview-emptymessage']"

    @allure.step("Ссылка ведет на страницу profile")
    def is_profile_url(self, page: Page) -> bool:
        return page.url == f"{Config.UI_HOST}/#/profile"

    @allure.step("Есть ли на странице текст 'No records found.'")
    def have_text_no_records_found(self, page: Page) -> bool:
        return page.text_content(self.EMPTY_MESSAGE) == self.NO_RECORD_TEXT

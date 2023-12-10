import allure
from assertpy import assert_that, soft_assertions


@allure.tag("UI")
@allure.suite("UI тесты")
@allure.sub_suite("Форма регистрации")
@allure.title("Проверка регистрации")
def test_ui_register(credentials, pages, page):
    pages.register.open_register_page(page)
    pages.register.fill_login(page, credentials.email)
    pages.register.fill_password(page, credentials.password)
    pages.register.fill_confirm_password(page, credentials.confirm_password)
    pages.register.click_submit_button(page)
    with soft_assertions():
        assert_that(
            pages.profile.have_text_no_records_found(page), "Текст No records found."
        ).is_true()
        assert_that(pages.profile.is_profile_url(page), "URL").is_true()

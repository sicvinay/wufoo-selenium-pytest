import pytest
from framework.settings import LiveSettings, wait_timeout
from pages.login_page import LoginPage
from pages.home_page import HomePage


@pytest.mark.live
def test_live_login_reaches_forms(driver):
    settings = LiveSettings.from_env()
    LoginPage(driver, wait_timeout()).open(settings.login_url).login(settings.email, settings.password)
    assert HomePage(driver, wait_timeout()).heading_text() == "Forms"

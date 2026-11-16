import pytest
from selenium.webdriver.common.by import By
from pages.home_page import HomePage

pytestmark = pytest.mark.ui


@pytest.mark.smoke
def test_login_reaches_forms_page(login_page, driver):
    login_page.login("demo@example.test", "demo-only-password")
    assert HomePage(driver).heading_text() == "Forms"
    assert not driver.find_element(By.ID, "loginForm").is_displayed()


@pytest.mark.negative
@pytest.mark.parametrize("email,password", [("", ""),("demo@example.test", ""),("", "demo-only-password")])
def test_required_fields(login_page, email, password):
    login_page.login(email, password)
    assert login_page.error_text() == "Email and password are required."


@pytest.mark.negative
@pytest.mark.parametrize("email,password", [("wrong@example.test", "wrong"),("demo@example.test", "wrong")])
def test_invalid_credentials(login_page, email, password):
    login_page.login(email, password)
    assert login_page.error_text() == "Invalid email or password."


def test_welcome_modal_can_be_closed(login_page, driver):
    login_page.login("demo@example.test", "demo-only-password")
    home = HomePage(driver)
    assert home.heading_text() == "Forms"
    assert home.close_optional_modal()
    assert not driver.find_element(By.ID, "modal").is_displayed()
    assert home.close_optional_modal(timeout=0.2) is False


def test_failed_login_can_be_corrected(login_page, driver):
    login_page.login("demo@example.test", "wrong")
    assert login_page.error_text() == "Invalid email or password."
    login_page.login("demo@example.test", "demo-only-password")
    assert HomePage(driver).heading_text() == "Forms"

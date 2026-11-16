from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL = (By.ID, "emailInput")
    PASSWORD = (By.ID, "passwordLogin")
    SUBMIT = (By.CSS_SELECTOR, 'input[value="LOGIN"]')
    ERROR = (By.ID, "loginError")  # Demo-only; live error markup may differ.

    def open(self, url):
        self.driver.get(url)
        self.visible(self.EMAIL)
        return self

    def login(self, email, password):
        self.fill(self.EMAIL, email)
        self.fill(self.PASSWORD, password)
        self.click(self.SUBMIT)

    def error_text(self):
        return self.visible(self.ERROR).text

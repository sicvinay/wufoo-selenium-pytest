from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class HomePage(BasePage):
    HEADING = (By.XPATH, "//h1[normalize-space()='Forms']")
    CLOSE_MODAL = (By.CSS_SELECTOR, 'button[aria-label="Close Modal"]')
    MODAL = (By.CSS_SELECTOR, '[role="dialog"]')

    def heading_text(self):
        return self.visible(self.HEADING).text

    def close_optional_modal(self, timeout=2):
        try:
            button = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(self.CLOSE_MODAL))
        except TimeoutException:
            return False
        button.click()
        self.wait.until(EC.invisibility_of_element_located(self.MODAL))
        return True

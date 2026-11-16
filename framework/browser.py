import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def create_driver(headless=True):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,1000")
    if os.getenv("CHROME_BINARY"):
        options.binary_location = os.environ["CHROME_BINARY"]
    service = Service(executable_path=os.environ["CHROMEDRIVER"]) if os.getenv("CHROMEDRIVER") else Service()
    driver = webdriver.Chrome(service=service, options=options)
    try:
        driver.set_page_load_timeout(30)
        driver.implicitly_wait(0)
    except Exception:
        driver.quit()
        raise
    return driver

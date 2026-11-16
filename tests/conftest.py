import base64
import logging
from pathlib import Path
import re
import uuid
import pytest
import pytest_html
from framework.browser import create_driver
from framework.settings import wait_timeout
from pages.login_page import LoginPage

ROOT = Path(__file__).resolve().parents[1]


def pytest_addoption(parser):
    parser.addoption("--live", action="store_true", help="Enable real account login")
    parser.addoption("--headed", action="store_true", help="Show Chrome")


def pytest_collection_modifyitems(config, items):
    if not config.getoption("--live"):
        for item in items:
            if "live" in item.keywords:
                item.add_marker(pytest.mark.skip(reason="Live login disabled; explicitly pass --live"))


def pytest_configure(config):
    worker = getattr(config, "workerinput", {}).get("workerid", "main")
    config.option.log_file = str(ROOT / "reports" / f"execution-{worker}.log")
    config.option.log_file_level = "INFO"
    # Selenium debug messages can contain typed passwords.
    logging.getLogger("selenium").setLevel(logging.CRITICAL)
    logging.getLogger("urllib3").setLevel(logging.WARNING)


@pytest.fixture
def driver(request):
    instance = create_driver(headless=not request.config.getoption("--headed"))
    try:
        yield instance
    finally:
        instance.quit()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver, wait_timeout()).open((ROOT / "demo" / "login.html").as_uri())


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    # Do not capture private account screens or credential values in live mode.
    if report.failed and "live" not in item.keywords and "driver" in item.funcargs:
        try:
            screenshot = item.funcargs["driver"].get_screenshot_as_png()
            folder = ROOT / "reports" / "screenshots"
            folder.mkdir(parents=True, exist_ok=True)
            name = re.sub(r"[^a-zA-Z0-9_.-]", "_", item.nodeid)[-100:]
            (folder / f"{name}-{uuid.uuid4().hex[:8]}.png").write_bytes(screenshot)
            report.extras = getattr(report, "extras", []) + [
                pytest_html.extras.png(base64.b64encode(screenshot).decode(), name="Failure screenshot")]
        except Exception as error:
            report.sections.append(("Screenshot capture", type(error).__name__))

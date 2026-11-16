import pytest
from framework.settings import LiveSettings, wait_timeout


def test_missing_live_settings(monkeypatch):
    for name in ("WUFOO_LOGIN_URL","WUFOO_EMAIL","WUFOO_PASSWORD"):
        monkeypatch.delenv(name, raising=False)
    with pytest.raises(ValueError, match="Set WUFOO"):
        LiveSettings.from_env()


@pytest.mark.parametrize("url", ["http://demo.wufoo.com/login/", "https://example.test/login/", "https://wufoo.com.evil.test/login/"])
def test_live_url_validation(monkeypatch, url):
    monkeypatch.setenv("WUFOO_LOGIN_URL", url)
    monkeypatch.setenv("WUFOO_EMAIL", "demo@example.test")
    monkeypatch.setenv("WUFOO_PASSWORD", "synthetic-test-value")
    with pytest.raises(ValueError):
        LiveSettings.from_env()


def test_password_not_in_settings_repr(monkeypatch):
    monkeypatch.setenv("WUFOO_LOGIN_URL", "https://demo.wufoo.com/login/")
    monkeypatch.setenv("WUFOO_EMAIL", "demo@example.test")
    monkeypatch.setenv("WUFOO_PASSWORD", "synthetic-test-value")
    assert "synthetic-test-value" not in repr(LiveSettings.from_env())


@pytest.mark.parametrize("value", ["0", "-1", "nan", "inf", "invalid"])
def test_invalid_wait_timeout(monkeypatch, value):
    monkeypatch.setenv("WAIT_TIMEOUT", value)
    with pytest.raises(ValueError):
        wait_timeout()

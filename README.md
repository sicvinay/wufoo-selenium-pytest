# Wufoo-inspired Selenium + Pytest Framework

A Python Selenium portfolio project refactored from an earlier Wufoo login
exercise. Uses Page Objects, explicit waits, independent browser fixtures,
failure screenshots, HTML/JUnit reports and parallel CI execution.

## What is actually tested?

| Suite | Target | Default |
| --- | --- | --- |
| 8 UI cases | Included synthetic HTML login fixture, in real Chrome | Enabled |
| 40 Python/configuration cases | Bundled practice algorithms and environment validation | Enabled |
| 1 live login case | Your explicitly configured Wufoo account | Skipped |

The local page is **not Wufoo** and does not implement secure authentication.
Its public demo credentials are `demo@example.test` / `demo-only-password`.
Passing demo checks establishes that the Page Objects work with that fixture;
it does not establish that Wufoo's current login flow works. Original Wufoo
field locators are retained as a starting point for the opt-in live test and
must be reviewed if the real service changes its markup or authentication.

This is an independent learning/portfolio project, not an official Wufoo product.
No original account credentials, old reports or Git history are included.

## Setup

Python 3.12+ and Chrome are required. From the repository root:

```bash
python -m venv .venv
```

Windows PowerShell activation:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS/Linux activation:

```bash
source .venv/bin/activate
```

Install and run:

```bash
python -m pip install -r requirements.txt
python -m pytest --html=reports/report.html --self-contained-html
python -m pytest -n 2 -m "not live" --html=reports/parallel.html --self-contained-html
```

Chrome runs headless by default. Pass `--headed` to see it. Selenium Manager
resolves the driver when none is configured; first use may require internet.
`CHROME_BINARY` and `CHROMEDRIVER` can point to existing compatible installations.
The test suite fails clearly if the browser cannot start; it does not silently
skip UI checks or replace them with mocked success.

## Useful selections

```bash
python -m pytest -m ui
python -m pytest -m smoke
python -m pytest -m "not ui and not live"
python -m pytest tests/test_login_ui.py::test_welcome_modal_can_be_closed
```

Each UI case creates a fresh browser, uses explicit waits, and always calls
`quit()` at fixture teardown. No test relies on another test signing in first.
Optional modal absence is handled narrowly; unrelated Selenium errors propagate.
There are no sleeps or import-time browser sessions.

## Reports and artifacts

- Open the generated HTML report in your browser.
- Add `--junitxml=reports/junit.xml` for JUnit output.
- Local-demo failures capture PNG files under `reports/screenshots/` and embed
  them into HTML reports when `pytest-html` is enabled.
- Each parallel worker writes to its own `reports/execution-<worker>.log`.
- Reports and screenshots are ignored by Git and uploaded as CI artifacts.
- Live tests never capture screenshots or HTML source because account screens
  may contain private information. Low-level Selenium debug logs are suppressed.
  Treat any manually generated live reports as private; do not use `--showlocals`
  or enable verbose transport logging when working with real credentials.

## Optional live Wufoo login

Only use a dedicated test account you own. Set these variables in your shell:

```powershell
$env:WUFOO_LOGIN_URL = "https://your-account.wufoo.com/login/"
$env:WUFOO_EMAIL = "your-test-account-email"
$env:WUFOO_PASSWORD = "your-test-account-password"
```

On Bash, use `export NAME="value"`. `.env.example` documents names but is not
automatically loaded. Then run:

```bash
python -m pytest --live -m live --headed
```

The URL must use HTTPS on a Wufoo subdomain. Live test failures remain failures;
there is no CAPTCHA bypass, MFA bypass, automatic retry of logins, or account
creation. The live flow only signs in and checks the Forms heading; it does not
create, modify, submit or delete forms. Run it serially to avoid concurrent login
sessions. CI deliberately does not use account credentials or run live login.

## Included Python practice

The original ZIP bundled unrelated practice scripts. They remain separate in
`exercises/algorithms.py` as pure functions with edge-case tests:

- Odd/even and prime checks (negative numbers, 0 and 1 handled correctly).
- Anagrams (case-sensitive; spaces and punctuation count).
- Character frequency, all unique characters and the first unique character.
- Exactly N Fibonacci terms, starting at 0; negative counts rejected.
- Non-empty contiguous substrings, retaining repeated occurrences.
- String reversal without slicing or adding a trailing space.

## Structure

| Path | Responsibility |
| --- | --- |
| `pages/` | Base, login and home Page Objects |
| `framework/` | Browser creation and environment settings |
| `demo/login.html` | Synthetic local login fixture |
| `tests/test_login_ui.py` | Real browser UI cases |
| `tests/test_live_wufoo.py` | Opt-in real account login |
| `tests/test_settings.py` | Configuration validation |
| `exercises/` | Refactored Python practice functions |
| `tests/test_exercises.py` | Practice edge cases |
| `.github/workflows/tests.yml` | Python 3.12–3.14 CI, parallel tests and artifacts |

## Changes from the original

Removed embedded account credentials, fixed sleeps, positional homepage login
locators, ordering-dependent tests, print-only checks, the import-time standalone
browser script, generated reports and unrelated logging demonstrations. Page
Objects now expose actions rather than returning raw elements to every test.
Use a current disposable password for any real account; the uploaded historical
files included credentials and should be treated as private.

References: [Selenium waits](https://www.selenium.dev/documentation/webdriver/waits/),
[Selenium Manager](https://www.selenium.dev/documentation/selenium_manager/),
[browser cleanup](https://www.selenium.dev/documentation/webdriver/interactions/windows/).

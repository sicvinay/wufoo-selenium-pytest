from dataclasses import dataclass, field
import math
import os
from urllib.parse import urlparse


@dataclass(frozen=True)
class LiveSettings:
    login_url: str
    email: str
    password: str = field(repr=False)

    @classmethod
    def from_env(cls):
        values = [os.getenv(name, "") for name in
                  ("WUFOO_LOGIN_URL", "WUFOO_EMAIL", "WUFOO_PASSWORD")]
        if not all(values):
            raise ValueError("Set WUFOO_LOGIN_URL, WUFOO_EMAIL and WUFOO_PASSWORD")
        parsed = urlparse(values[0])
        if (parsed.scheme != "https" or not (parsed.hostname or "").endswith(".wufoo.com")
                or parsed.username or parsed.password or parsed.query or parsed.fragment):
            raise ValueError("Live URL must be HTTPS on a Wufoo subdomain, without credentials/query/fragment")
        return cls(*values)


def wait_timeout():
    value = float(os.getenv("WAIT_TIMEOUT", "10"))
    if not math.isfinite(value) or value <= 0:
        raise ValueError("WAIT_TIMEOUT must be finite and positive")
    return value

import secrets

from faker.providers.date_time import Provider as DateTimeProvider
from faker.providers.python import Provider


class CustomProviders(Provider, DateTimeProvider):
    def safe_password(self, **kwargs) -> str:
        return secrets.token_urlsafe(10)

    def fake_stringify_future_date(self, *args, **kwargs) -> str:
        return self.future_date(*args, **kwargs).strftime("%Y-%m-%d")

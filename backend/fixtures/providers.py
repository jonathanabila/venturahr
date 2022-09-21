import secrets

from faker.providers.python import Provider


class CustomProviders(Provider):
    def safe_password(self, **kwargs):
        return secrets.token_urlsafe(10)

import logging

import factory

from fixtures.providers import CustomProviders

logging.disable(logging.CRITICAL)
factory.Faker.add_provider(CustomProviders)

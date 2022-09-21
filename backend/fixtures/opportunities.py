import factory

from fixtures.models.opportunities import OpportunityStub


class OpportunityFormFactory(factory.Factory):
    class Meta:
        model = OpportunityStub

    name = factory.Faker("name")
    description = factory.Faker("text")

    expires_at = factory.Faker("fake_stringify_future_date", end_date="+15d")

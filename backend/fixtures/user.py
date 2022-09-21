import factory.django

from core.models import User
from fixtures.company import CompanyFactory
from fixtures.models.user import UserStub


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")

    email = factory.Faker("email")
    username = factory.LazyAttribute(lambda u: str(u.email).split("@")[0])

    company = factory.SubFactory(CompanyFactory)


class UserFormFactory(factory.Factory):
    class Meta:
        model = UserStub

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")

    email = factory.Faker("email")
    username = factory.LazyAttribute(lambda u: u.email)

    password1 = factory.Faker("safe_password")
    password2 = factory.SelfAttribute(".password1")

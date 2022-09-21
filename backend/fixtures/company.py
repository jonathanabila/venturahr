import factory.django

from companies.models import Company


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    name = factory.Faker("company_suffix")
    identifier = factory.LazyAttribute(lambda n: str(n.name).replace(" ", ""))

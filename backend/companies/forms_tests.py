import pytest
from unittest.mock import MagicMock

from companies.forms import CompaniesRecruiterRegistrationForm, CompaniesRegistrationForm
from companies.models import Company
from fixtures.company import CompanyFactory
from fixtures.user import UserWithCompanyFormFactory
from fixtures.utils import factory_boy_decoder


@pytest.mark.django_db(transaction=True, reset_sequences=True)
class TestCompaniesRegistrationFormFormTransaction:
    @pytest.fixture(autouse=True)
    def setup(self) -> None:
        self.sut = CompaniesRegistrationForm

    def test_companies_exists(self) -> None:
        company = CompanyFactory()

        payload = factory_boy_decoder(UserWithCompanyFormFactory(company=company.name))
        form = self.sut(factory_boy_decoder(payload))

        user = form.save()

        assert Company.objects.filter(name=user.company.name).exists()
        assert Company.objects.filter(name=company.name).exists()

    def test_companies_not_exists(self) -> None:
        payload = factory_boy_decoder(UserWithCompanyFormFactory())
        form = self.sut(factory_boy_decoder(payload))

        user = form.save()

        assert Company.objects.filter(name=user.company.name).exists()
        assert Company.objects.filter(name=payload["company"]).exists()


@pytest.mark.django_db
class TestCompaniesRegistrationFormForm:
    @pytest.fixture(autouse=True)
    def setup(self) -> None:
        self.sut = CompaniesRegistrationForm
        self.payload = factory_boy_decoder(UserWithCompanyFormFactory())

    @pytest.mark.parametrize(
        "field",
        ("email", "username", "first_name", "last_name", "password1", "password2", "company"),
    )
    def test_required_fields(self, field) -> None:
        self.payload.pop(field)

        form = self.sut(self.payload)
        assert form.is_valid() is False

    def test_form_is_valid(self) -> None:
        form = self.sut(self.payload)
        assert form.is_valid() is True

    def test_user_company(self) -> None:
        form = self.sut(self.payload)

        user = form.save()
        company = Company.objects.get(name=self.payload["company"])

        assert user.company.id == company.id

    def test_candidate_form_permissions_is_admin(self):
        form = self.sut(self.payload)
        form.is_valid()

        user = form.save()

        assert user.is_admin is True

    def test_candidate_permissions(self) -> None:
        form = self.sut(self.payload)
        form.is_valid()

        user = form.save()

        user.has_perms(
            tuple(
                (
                    (
                        f"companies.{p}"
                        for p in (
                            "view_companyuser",
                            "view_company",
                            "change_companyuser",
                            "change_companyrecruiteruser",
                            "add_companyrecruiteruser",
                            "delete_companyrecruiteruser",
                            # Opportunities
                        )
                    ),
                    *("opportunities.view_opportunity",),
                )
            )
        )


@pytest.mark.django_db
class TestCompaniesRecruiterRegistrationForm:
    @pytest.fixture(autouse=True)
    def setup(self) -> None:
        company = CompanyFactory()
        current_user = MagicMock(company=company)

        self.payload = factory_boy_decoder(UserWithCompanyFormFactory(company=company.name))

        def sut(*args, **kwargs):
            return CompaniesRecruiterRegistrationForm(*args, current_user=current_user, **kwargs)

        self.sut = sut

    @pytest.mark.parametrize(
        "field",
        ("email", "username", "first_name", "last_name", "password1", "password2", "company"),
    )
    def test_required_fields(self, field) -> None:
        self.payload.pop(field)

        form = self.sut(self.payload)
        assert form.is_valid() is False

    def test_form_is_valid(self) -> None:
        form = self.sut(self.payload)
        assert form.is_valid() is True

    def test_user_company(self) -> None:
        form = self.sut(self.payload)

        user = form.save()
        company = Company.objects.get(name=self.payload["company"])

        assert user.company.id == company.id

    def test_candidate_form_permissions_is_candidate(self):
        form = self.sut(self.payload)
        form.is_valid()

        user = form.save()

        assert user.is_recruiter is True

    def test_candidate_permissions(self) -> None:
        form = self.sut(self.payload)
        form.is_valid()

        user = form.save()

        user.has_perms(
            tuple(
                (
                    (
                        f"companies.{p}"
                        for p in (
                            "view_companyuser",
                            "view_company",
                            "change_companyuser",
                            "change_companyrecruiteruser",
                        )
                    ),
                    (
                        f"opportunities.{p}"
                        for p in (
                            "add_opportunity",
                            "change_opportunity",
                            "delete_opportunity",
                            "view_opportunity",
                        )
                    ),
                )
            )
        )

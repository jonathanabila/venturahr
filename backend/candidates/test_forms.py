import pytest

from candidates.forms import CandidatesRegistrationForm
from fixtures.user import UserFormFactory
from fixtures.utils import factory_boy_decoder


@pytest.mark.django_db
class TestCandidatesRegistrationForm:
    @pytest.fixture(autouse=True)
    def setup(self) -> None:
        self.sut = CandidatesRegistrationForm

    @pytest.mark.parametrize(
        "field", ("email", "username", "first_name", "last_name", "password1", "password2")
    )
    def test_required_fields(self, field) -> None:
        payload = factory_boy_decoder(UserFormFactory())
        payload.pop(field)

        form = self.sut(factory_boy_decoder(payload))
        assert form.is_valid() is False

    def test_form_is_valid(self) -> None:
        payload = factory_boy_decoder(UserFormFactory())

        form = self.sut(factory_boy_decoder(payload))
        assert form.is_valid() is True

    def test_candidate_permissions(self) -> None:
        payload = factory_boy_decoder(UserFormFactory())

        form = self.sut(factory_boy_decoder(payload))
        form.is_valid()

        user = form.save()

        user.has_perms(
            tuple(
                f"opportunities.{p}"
                for p in (
                    "view_candidateuser",
                    "change_candidateuser",
                    "view_opportunity",
                    "signup_opportunity",
                )
            )
        )

    def test_candidate_form_permissions_is_candidate(self):
        payload = factory_boy_decoder(UserFormFactory())

        form = self.sut(factory_boy_decoder(payload))
        form.is_valid()

        user = form.save()

        assert user.is_candidate is True

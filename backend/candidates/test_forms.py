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

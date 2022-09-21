import pytest
from datetime import datetime, timedelta

from core.constants import MAXIMUM_OPPORTUNITY_INTERVAL
from fixtures.opportunities import OpportunityFormFactory
from fixtures.user import UserFactory
from fixtures.utils import factory_boy_decoder, rgetattr
from opportunities.forms import OpportunityNewForm

DATE_FORMAT = "%Y-%m-%d"


@pytest.mark.django_db
class TestOpportunityNewForm:
    @pytest.fixture(autouse=True)
    def setup(self) -> None:
        self.user = UserFactory()

        def sut(*args, **kwargs):
            return OpportunityNewForm(*args, current_user=self.user)

        self.sut = sut
        self.payload = factory_boy_decoder(OpportunityFormFactory())

    def test_smaller_than_minimum_interval(self) -> None:
        self.payload["expires_at"] = datetime.now().strftime(DATE_FORMAT)

        form = self.sut(self.payload)

        assert form.is_valid() is False
        assert form.has_error("expires_at") is True

    def test_bigger_than_minimum_interval(self) -> None:
        self.payload["expires_at"] = (
            datetime.now() + timedelta(days=MAXIMUM_OPPORTUNITY_INTERVAL + 1)
        ).strftime(DATE_FORMAT)

        form = self.sut(self.payload)

        assert form.is_valid() is False
        assert form.has_error("expires_at") is True

    @pytest.mark.parametrize(
        "opportunity_field, user_field", (("company.id", "company_id"), ("created_by_id", "id"))
    )
    def test_opportunity_company(self, opportunity_field, user_field) -> None:
        form = self.sut(self.payload)
        form.is_valid()

        opportunity = form.save()

        assert rgetattr(opportunity, opportunity_field) == rgetattr(self.user, user_field)

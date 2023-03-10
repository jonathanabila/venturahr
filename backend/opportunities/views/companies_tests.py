import pytest
from http import HTTPStatus

from django.test import Client
from django.urls import reverse

from core.models import User
from fixtures.user import UserFactory
from opportunities.views import OpportunitiesNewOpportunityView, OpportunityCandidateView


@pytest.fixture()
def user() -> User:
    return UserFactory()


@pytest.fixture()
def unauthorized_client(user: User) -> Client:
    client = Client()
    client.force_login(user=user)
    return client


@pytest.fixture()
def non_authenticated_client(user: User) -> Client:
    client = Client()
    return client


@pytest.mark.django_db
class TestOpportunitiesNewOpportunityView:
    @pytest.fixture(autouse=True)
    def setup(self) -> None:
        self.sut = OpportunitiesNewOpportunityView
        self.reverse_url = reverse("opportunities:private-new-opportunity")

    def test_not_logged(self, non_authenticated_client) -> None:
        response = non_authenticated_client.get(self.reverse_url, follow=True)
        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_non_authorized(self, unauthorized_client) -> None:
        response = unauthorized_client.get(self.reverse_url, follow=True)
        assert response.status_code == HTTPStatus.FORBIDDEN


@pytest.mark.django_db
class TestOpportunityCandidateView:
    @pytest.fixture(autouse=True)
    def setup(self, user) -> None:
        self.sut = OpportunityCandidateView
        self.reverse_url = reverse(
            "opportunities:private-opportunity-answer-candidate",
            kwargs={"pk": 1, "candidate_pk": user.id},
        )

    def test_not_logged(self, non_authenticated_client) -> None:
        response = non_authenticated_client.get(self.reverse_url, follow=True)
        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_non_authorized(self, unauthorized_client) -> None:
        response = unauthorized_client.get(self.reverse_url, follow=True)
        assert response.status_code == HTTPStatus.FORBIDDEN

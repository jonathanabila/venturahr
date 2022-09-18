from django.urls import path

import opportunities.views.opportunities

from . import views

app_name = "opportunities"

urlpatterns = [
    path(
        "private/opportunities/new",
        views.OpportunitiesNewOpportunityView.as_view(),
        name="private-new-opportunity",
    ),
    path(
        "private/opportunities/<int:pk>",
        opportunities.views.opportunities.OpportunitiesOpportunityView.as_view(),
        name="private-opportunity",
    ),
    path(
        "private/opportunities/",
        opportunities.views.opportunities.OpportunitiesRecruiterOpportunities.as_view(),
        name="private-opportunities",
    ),
    path(
        "private/opportunities/<int:pk>/apply",
        opportunities.views.OpportunitiesCandidateApplyView.as_view(),
        name="private-apply-opportunity",
    ),
    path(
        "private/opportunities/<int:pk>/candidates",
        opportunities.views.OpportunityCandidatesView.as_view(),
        name="private-candidates",
    ),
]

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
]
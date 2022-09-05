from django.urls import path

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
        views.OpportunitiesRecruiterOpportunityView.as_view(),
        name="private-opportunity",
    ),
]

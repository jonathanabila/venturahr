from django.urls import path

from . import views

app_name = "candidates"


urlpatterns = [
    path("home/", views.CandidateHomePageView.as_view(), name="home"),
]

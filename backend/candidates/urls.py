from django.urls import path

from . import views

app_name = "candidates"


urlpatterns = [
    path("home/", views.CandidatesHomePageView.as_view(), name="home"),
    path("login/", views.CandidatesLoginPageView.as_view(), name="login"),
    path("register/", views.CandidatesRegisterView.as_view(), name="register"),
]

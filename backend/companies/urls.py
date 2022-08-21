from django.urls import path

from . import views

app_name = "companies"


urlpatterns = [
    path("home/", views.CompaniesHomePageView.as_view(), name="home"),
    path("login/", views.CompaniesLoginView.as_view(), name="login"),
    path("register/", views.CompaniesRegisterView.as_view(), name="register"),
    path("private/home/", views.CompaniesPrivateHomePageView.as_view(), name="private-home"),
    path(
        "private/recruiter/",
        views.CompaniesNewRecruiterView.as_view(),
        name="private-new-recruiter",
    ),
]

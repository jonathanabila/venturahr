from django.urls import path

from . import views

app_name = "companies"


urlpatterns = [
    path("home/", views.CompanyHomePageView.as_view(), name="home"),
    path("login/", views.CompanyLoginView.as_view(), name="login"),
]

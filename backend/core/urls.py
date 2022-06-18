from django.urls import path

from . import views

app_name = "core"


urlpatterns = [
    path("home/", views.HomePageView.as_view(), name="home"),
    path("login/", views.VenturaHRLoginView.as_view(), name="login"),
]

from django.urls import path

from . import views

app_name = "core"


urlpatterns = [
    path("home/", views.HomePageView.as_view(), name="home"),
    path("logout/", views.VenturaHRLogoutView.as_view(), name="logout"),
]

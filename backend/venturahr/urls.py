"""venturahr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from venturahr.views import index

schema_view = get_schema_view(
    openapi.Info(
        title="VenturaHR API",
        default_version="v1",
        description="PB-2023.1",
        terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True,
)

urlpatterns = [
    path("ping/", index),
    path("health/", include("health_check.urls")),
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("", RedirectView.as_view(url="home/")),
    path("companies/", include("companies.urls")),
    path("candidates/", include("candidates.urls")),
    path("opportunities/", include("opportunities.urls")),
    re_path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]

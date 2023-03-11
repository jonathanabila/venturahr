import os

from django.http import HttpResponse


def index(request):
    version = os.getenv("COMMIT_HASH")
    return HttpResponse(f"VenturaHR@{version}")

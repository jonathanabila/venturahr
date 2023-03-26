import os

from django.http import HttpResponse


def index(*_, **__):
    version = os.getenv("COMMIT_HASH")
    return HttpResponse(f"VenturaHR@{version}")

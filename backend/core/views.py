import logging

from django.views import View, generic

logger = logging.getLogger(__name__)


class VenturaHRView(View):
    ...


class HomePageView(VenturaHRView, generic.base.TemplateView):
    template_name = "core/home.html"

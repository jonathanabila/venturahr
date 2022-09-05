from django.db import models
from django.utils import timezone


class Opportunity(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=254)

    created_at = models.DateTimeField(default=timezone.now)
    expires_at = models.DateField()

    company = models.ForeignKey(
        "companies.Company",
        null=True,
        on_delete=models.CASCADE,
        verbose_name="company",
        help_text="User company",
    )

    created_by = models.ForeignKey(
        "core.User",
        null=False,
        on_delete=models.CASCADE,
        verbose_name="created by",
    )

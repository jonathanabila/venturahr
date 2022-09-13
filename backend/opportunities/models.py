from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone


class Opportunity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=3000)

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


class OpportunityRequirement(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=3000)

    created_at = models.DateTimeField(default=timezone.now)

    weight = models.IntegerField(
        null=False, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    opportunity = models.ForeignKey(
        "opportunities.Opportunity",
        null=False,
        on_delete=models.CASCADE,
        verbose_name="opportunity",
        related_name="requirements",
    )

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

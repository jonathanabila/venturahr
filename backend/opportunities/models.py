from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

MAXIMUM_OPPORTUNITY_INTERVAL = 30


class Opportunity(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=254)

    created_at = models.DateTimeField(_("date joined"), default=timezone.now)
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

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if (self.expires_at - timezone.now()) > MAXIMUM_OPPORTUNITY_INTERVAL:
            raise ValidationError(
                f"A Oppportunity can only last for {MAXIMUM_OPPORTUNITY_INTERVAL} days."
            )
        super().save(force_insert, force_update, using, update_fields)

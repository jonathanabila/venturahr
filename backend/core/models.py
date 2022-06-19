from django.contrib.auth.models import AbstractUser
from django.db import models

from companies.models import Company


class User(AbstractUser):
    company = models.ForeignKey(
        Company,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="company",
        help_text="User company",
    )

    class Meta:
        unique_together = ("email", "company")
        indexes = [
            models.Index(name="email_at_index", fields=["email"]),
            models.Index(name="email_company_at_index", fields=["email", "company"]),
        ]

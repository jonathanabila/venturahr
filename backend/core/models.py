from django.contrib.auth.models import AbstractUser
from django.db import models

from .constants import NAMESPACE_CANDIDATE_PERMISSIONS, NAMESPACE_RECRUITER_PERMISSIONS


class User(AbstractUser):
    company = models.ForeignKey(
        "companies.Company",
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

    @property
    def is_recruiter(self) -> bool:
        return self.has_perms(NAMESPACE_RECRUITER_PERMISSIONS)

    @property
    def is_candidate(self) -> bool:
        return self.has_perms(NAMESPACE_CANDIDATE_PERMISSIONS)

    @property
    def is_admin(self) -> bool:
        return self.has_perms(
            "companies.change_companyuser",
            "companies.change_companyrecruiteruser",
        )

    @property
    def get_full_name(self) -> str:
        return super().get_full_name().title()

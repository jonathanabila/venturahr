from django.db import models

from core.models import User


class Company(models.Model):
    name = models.CharField(max_length=250)
    identifier = models.CharField(max_length=30)

    class Meta:
        unique_together = ("identifier",)


class CompanyUser(User):
    class Meta:
        proxy = True


class CompanyRecruiterUser(CompanyUser):
    class Meta:
        proxy = True

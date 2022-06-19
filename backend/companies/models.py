from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=250)
    identifier = models.CharField(max_length=30)

    class Meta:
        unique_together = ("identifier",)

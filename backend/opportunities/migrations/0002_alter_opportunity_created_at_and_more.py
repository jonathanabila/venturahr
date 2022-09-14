# Generated by Django 4.1 on 2022-09-07 23:56

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("companies", "0003_companyrecruiteruser"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("opportunities", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="opportunity",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="opportunity",
            name="description",
            field=models.TextField(max_length=3000),
        ),
        migrations.CreateModel(
            name="OpportunityRequirement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=254)),
                ("description", models.TextField(max_length=3000)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("weight", models.IntegerField()),
                (
                    "company",
                    models.ForeignKey(
                        help_text="User company",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="companies.company",
                        verbose_name="company",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="created by",
                    ),
                ),
                (
                    "opportunity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="opportunities.opportunity",
                        verbose_name="opportunity",
                    ),
                ),
            ],
        ),
    ]
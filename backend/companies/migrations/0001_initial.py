# Generated by Django 4.0.5 on 2022-06-19 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []  # type: ignore

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                ("identifier", models.CharField(max_length=30)),
            ],
            options={
                "unique_together": {("identifier",)},
            },
        ),
    ]
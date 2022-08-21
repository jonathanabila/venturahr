# Generated by Django 4.1 on 2022-08-21 02:45

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
        ("candidates", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Candidate",
        ),
        migrations.CreateModel(
            name="CandidateUser",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("core.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]

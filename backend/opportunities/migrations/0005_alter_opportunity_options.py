# Generated by Django 4.1 on 2022-09-14 00:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("opportunities", "0004_alter_opportunityrequirement_weight"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="opportunity",
            options={"permissions": [("signup_opportunity", "Can sign up for an opportunity")]},
        ),
    ]

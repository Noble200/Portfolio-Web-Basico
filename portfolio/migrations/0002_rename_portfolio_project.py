# Generated by Django 5.1.4 on 2025-01-08 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Portfolio",
            new_name="Project",
        ),
    ]

# Generated by Django 5.1.5 on 2025-03-31 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                blank=True, default="default.jpg", null=True, upload_to="profile_pics"
            ),
        ),
    ]

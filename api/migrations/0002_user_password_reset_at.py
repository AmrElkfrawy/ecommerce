# Generated by Django 5.1 on 2024-08-19 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="password_reset_at",
            field=models.DateTimeField(null=True),
        ),
    ]

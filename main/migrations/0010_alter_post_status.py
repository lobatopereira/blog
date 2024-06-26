# Generated by Django 5.0.2 on 2024-04-25 19:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0009_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="status",
            field=models.CharField(
                choices=[
                    ("Draft", "Draft"),
                    ("Published", "Published"),
                    ("Scheduled", "Scheduled"),
                ],
                default="draft",
                max_length=20,
            ),
        ),
    ]

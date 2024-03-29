# Generated by Django 5.0.2 on 2024-03-17 03:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_categoria_portfolio_enderesu_url_portfolio_status_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="portfolio",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="portfolio",
                to="main.portfolio",
            ),
        ),
    ]

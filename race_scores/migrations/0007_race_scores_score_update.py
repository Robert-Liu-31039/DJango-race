# Generated by Django 5.2.2 on 2025-06-10 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("race_scores", "0006_race_scores_projection_tag"),
    ]

    operations = [
        migrations.AddField(
            model_name="race_scores",
            name="score_update",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

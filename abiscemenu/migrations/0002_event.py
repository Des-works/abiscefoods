# Generated by Django 4.2.2 on 2023-07-14 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("abiscemenu", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                ("breve_description", models.CharField(max_length=50)),
                ("date_time", models.DateTimeField(auto_now_add=True)),
                (
                    "image",
                    models.ImageField(blank=True, default="", upload_to="events"),
                ),
            ],
        ),
    ]

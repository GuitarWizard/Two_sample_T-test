# Generated by Django 4.1 on 2022-11-20 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EntryOne",
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
                ("input_one", models.CharField(max_length=1000)),
                ("input_two", models.CharField(max_length=1000)),
            ],
        ),
    ]

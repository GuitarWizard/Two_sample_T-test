# Generated by Django 4.1 on 2022-11-20 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("t_test_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="EntryTwo",
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
                ("input_two", models.CharField(max_length=1000)),
            ],
        ),
        migrations.RemoveField(model_name="entryone", name="input_two",),
    ]

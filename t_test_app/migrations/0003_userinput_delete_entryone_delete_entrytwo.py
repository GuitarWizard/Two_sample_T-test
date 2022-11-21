# Generated by Django 4.1 on 2022-11-21 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("t_test_app", "0002_entrytwo_remove_entryone_input_two"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserInput",
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
        migrations.DeleteModel(name="EntryOne",),
        migrations.DeleteModel(name="EntryTwo",),
    ]

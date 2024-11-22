# Generated by Django 5.1.3 on 2024-11-17 12:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Error",
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
                ("description", models.TextField()),
                ("received_date", models.DateField()),
                (
                    "error_level",
                    models.CharField(
                        choices=[
                            ("Критична", "Критична"),
                            ("Важлива", "Важлива"),
                            ("Незначна", "Незначна"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Інтерфейс", "Інтерфейс"),
                            ("Дані", "Дані"),
                            ("Розрахунковий алгоритм", "Розрахунковий алгоритм"),
                            ("Інше", "Інше"),
                            ("Невідома категорія", "Невідома категорія"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "source",
                    models.CharField(
                        choices=[
                            ("Користувач", "Користувач"),
                            ("Тестувальник", "Тестувальник"),
                        ],
                        max_length=15,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Programmer",
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
                ("last_name", models.CharField(max_length=50)),
                ("first_name", models.CharField(max_length=50)),
                ("phone", models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name="Fix",
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
                ("start_date", models.DateField()),
                ("duration", models.IntegerField()),
                ("daily_rate", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "error",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="projects.error"
                    ),
                ),
                (
                    "programmer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projects.programmer",
                    ),
                ),
            ],
        ),
    ]

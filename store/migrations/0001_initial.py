# Generated by Django 4.1.7 on 2023-02-22 21:57

# django imports
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Store",
            fields=[
                (
                    "store_id",
                    models.PositiveBigIntegerField(
                        db_index=True, primary_key=True, serialize=False
                    ),
                ),
                ("time_zone_str", models.CharField(max_length=50)),
            ],
            options={"db_table": "store"},
        ),
        migrations.CreateModel(
            name="StoreStatus",
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
                (
                    "status",
                    models.CharField(
                        choices=[("active", "active"), ("inactive", "inactive")],
                        max_length=8,
                    ),
                ),
                ("timestamp", models.DateTimeField()),
                (
                    "store_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.store"
                    ),
                ),
            ],
            options={"db_table": "store_status"},
        ),
        migrations.CreateModel(
            name="StoreHours",
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
                (
                    "day_of_week",
                    models.IntegerField(
                        choices=[
                            (0, "Monday"),
                            (1, "Tuesday"),
                            (2, "Wednesday"),
                            (3, "Thursday"),
                            (4, "Friday"),
                            (5, "Saturday"),
                            (6, "Sunday"),
                        ]
                    ),
                ),
                ("start_time_local", models.TimeField()),
                ("end_time_local", models.TimeField()),
                (
                    "store_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.store"
                    ),
                ),
            ],
            options={"db_table": "store_hours"},
        ),
    ]

# Generated by Django 4.1.4 on 2023-01-05 14:48

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("title", models.CharField(max_length=150)),
                ("description", models.TextField(max_length=250)),
                ("completed", models.BooleanField()),
                ("date_added", models.DateTimeField()),
                ("due_date", models.DateTimeField()),
                (
                    "priority",
                    models.IntegerField(
                        default=1,
                        validators=[
                            django.core.validators.MaxValueValidator(3),
                            django.core.validators.MinValueValidator(1),
                        ],
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-due_date"],
            },
        ),
    ]

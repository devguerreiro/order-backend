# Generated by Django 3.1.7 on 2021-03-15 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_add__client"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150)),
                (
                    "currency",
                    models.CharField(
                        choices=[("R$", "Real"), ("$", "Dolar"), ("€", "Euro")],
                        default="R$",
                        max_length=5,
                    ),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=9)),
                ("multiplier", models.IntegerField(default=1)),
            ],
        ),
    ]

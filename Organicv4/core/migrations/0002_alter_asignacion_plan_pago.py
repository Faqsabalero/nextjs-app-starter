# Generated by Django 5.2.1 on 2025-05-15 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="asignacion",
            name="plan_pago",
            field=models.CharField(
                choices=[
                    ("1", "Cuota 1"),
                    ("2", "Cuota 2"),
                    ("3", "Cuota 3"),
                    ("4", "Cuota 4"),
                ],
                max_length=20,
            ),
        ),
    ]

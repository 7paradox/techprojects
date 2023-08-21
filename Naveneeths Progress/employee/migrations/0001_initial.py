# Generated by Django 4.2.4 on 2023-08-09 19:13

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("firstname", models.CharField(max_length=30)),
                ("lastname", models.CharField(max_length=30)),
                ("hiredate", models.DateField()),
                ("exitdate", models.DateField()),
                ("managerid", models.IntegerField()),
                ("employeeid", models.IntegerField()),
                ("salary", models.IntegerField()),
                ("bonuspercent", models.IntegerField()),
                ("status", models.CharField(max_length=1)),
            ],
        ),
    ]
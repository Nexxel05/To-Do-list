# Generated by Django 4.2.3 on 2023-07-26 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="created",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="deadline",
            field=models.DateField(blank=True, null=True),
        ),
    ]

# Generated by Django 5.1.3 on 2024-12-14 18:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0008_alter_destination_image_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="destination",
            name="currency",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="destination",
            name="language",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="destination",
            name="timezone",
            field=models.CharField(max_length=100),
        ),
    ]

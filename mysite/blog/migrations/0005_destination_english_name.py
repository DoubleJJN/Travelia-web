# Generated by Django 5.1.2 on 2024-11-16 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_destination_city_remove_destination_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='english_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

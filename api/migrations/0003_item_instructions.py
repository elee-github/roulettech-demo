# Generated by Django 4.2.14 on 2024-07-15 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_item_ingredients_item_time_to_cook'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='instructions',
            field=models.TextField(default='To be written...'),
        ),
    ]

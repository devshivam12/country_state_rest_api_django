# Generated by Django 4.2 on 2024-04-03 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='description',
            field=models.TextField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]

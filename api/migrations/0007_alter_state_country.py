# Generated by Django 4.2 on 2024-04-04 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_state_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='Country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.country'),
        ),
    ]

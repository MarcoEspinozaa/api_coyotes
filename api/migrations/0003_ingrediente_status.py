# Generated by Django 4.0.5 on 2022-06-24 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_plato_ingrediente_plato_ingredientes'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingrediente',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]

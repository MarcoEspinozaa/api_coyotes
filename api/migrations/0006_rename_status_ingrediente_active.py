# Generated by Django 4.0.5 on 2022-06-24 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_ingrediente_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingrediente',
            old_name='status',
            new_name='active',
        ),
    ]

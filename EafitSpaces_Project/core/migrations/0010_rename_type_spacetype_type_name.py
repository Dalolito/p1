# Generated by Django 5.0.7 on 2024-08-29 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_space_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spacetype',
            old_name='type',
            new_name='type_name',
        ),
    ]

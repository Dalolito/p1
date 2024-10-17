# Generated by Django 5.0.7 on 2024-10-11 04:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_rename_space_reservation_space_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='type',
            new_name='name',
        ),
        migrations.CreateModel(
            name='SpaceXResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('resource_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.resource')),
                ('space_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.space')),
            ],
            options={
                'unique_together': {('space_id', 'resource_id')},
            },
        ),
    ]
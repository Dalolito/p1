# Generated by Django 5.1.1 on 2024-11-13 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0020_alter_spacexresource_quantity"),
    ]

    operations = [
        migrations.AddField(
            model_name="reports",
            name="range_type",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

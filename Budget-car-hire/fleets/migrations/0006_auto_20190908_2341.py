# Generated by Django 2.2.4 on 2019-09-08 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleets', '0005_remove_fleet_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fleet',
            options={'ordering': ['is_approved']},
        ),
        migrations.AddField(
            model_name='fleet',
            name='is_freezed',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 3.0 on 2019-12-16 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoreApp', '0002_auto_20191217_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='is_hired',
            field=models.BooleanField(default=False),
        ),
    ]
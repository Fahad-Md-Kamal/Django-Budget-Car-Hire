# Generated by Django 2.2.4 on 2019-09-19 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_auto_20190919_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='is_booked',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 2.2.4 on 2019-09-11 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20190911_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fleetpayment',
            name='account_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fleetpayment',
            name='payment_medium',
            field=models.IntegerField(choices=[(0, 'Direct Payment'), (1, 'Nagad App-pay'), (2, 'Bank Transection'), (3, 'VISA Payment'), (4, 'MASTERCARD Payment'), (5, 'AMERICAN EXPRESS')], default=0),
        ),
    ]
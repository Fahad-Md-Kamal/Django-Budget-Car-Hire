# Generated by Django 2.2.4 on 2019-09-03 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicle', '0005_auto_20190903_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fleet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('fleet_duration', models.DateTimeField(blank=True, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('is_paid', models.BooleanField(default=False)),
                ('fleet_vehicles', models.ManyToManyField(related_name='fleet_vehicle', to='vehicle.Vehicle')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_fleet', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
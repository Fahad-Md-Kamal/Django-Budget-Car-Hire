# Generated by Django 2.2.4 on 2019-10-08 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import vehicle.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.IntegerField(choices=[(0, 'Other'), (1, 'Audi'), (2, 'BMW'), (3, 'Chevrolet'), (4, 'Ford'), (5, 'Honda'), (6, 'Hyundai'), (7, 'Jeep'), (8, 'Kia'), (9, 'Lexus'), (10, 'Mazda'), (11, 'Mercedes-Benz'), (12, 'Mitsubishi'), (13, 'Nissan'), (14, 'Renault'), (15, 'Suzuki'), (16, 'Subaru'), (17, 'Tata'), (18, 'Toyota'), (19, 'VolksWagen'), (20, 'Volvo')], default=0)),
                ('model_year', models.DateField(blank=True, null=True)),
                ('reg_no', models.CharField(max_length=20, unique=True)),
                ('vehicle_type', models.IntegerField(choices=[(0, 'Small'), (1, 'Medium'), (2, 'Large'), (3, 'Van')], default=0)),
                ('added_on', models.DateField(auto_now_add=True)),
                ('rent', models.PositiveIntegerField(default=2000)),
                ('capacity', models.PositiveIntegerField(default=2)),
                ('is_freezed', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=False)),
                ('is_booked', models.BooleanField(default=False)),
                ('booked_date', models.DateTimeField(auto_now=True, null=True)),
                ('is_hired', models.BooleanField(default=False)),
                ('image', models.ImageField(default='default_vehicle.png', upload_to=vehicle.models.photo_path)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicel_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-is_approved', '-added_on'],
            },
        ),
    ]

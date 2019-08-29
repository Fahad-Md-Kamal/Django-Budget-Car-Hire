# Generated by Django 2.2.4 on 2019-08-29 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


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
                ('reg_no', models.TextField(max_length=20, unique=True)),
                ('model_name', models.TextField(max_length=20)),
                ('vehicle_type', models.IntegerField(choices=[(0, 'Small Car'), (1, 'Medium Car'), (2, 'Large Car'), (3, 'Van')], default=0)),
                ('is_hired', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=True)),
                ('added_on', models.DateField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicel_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['vehicle_type'],
            },
        ),
    ]

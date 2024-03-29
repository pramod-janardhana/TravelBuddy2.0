# Generated by Django 2.2.6 on 2019-10-22 18:44

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
            name='Packages',
            fields=[
                ('location_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('location_name', models.CharField(max_length=50)),
                ('sub_title', models.TextField()),
                ('price', models.IntegerField()),
                ('offer', models.BooleanField(default=False)),
                ('days', models.IntegerField()),
                ('date', models.DateField()),
                ('vacancies', models.IntegerField()),
                ('destination_image', models.ImageField(upload_to='destinations')),
            ],
        ),
        migrations.CreateModel(
            name='PackagesVehicle',
            fields=[
                ('reg_number', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('vehicle_name', models.CharField(max_length=50)),
                ('capacity', models.IntegerField()),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travello.Packages')),
            ],
        ),
        migrations.CreateModel(
            name='PackagesHotel',
            fields=[
                ('hotel_id', models.CharField(max_length=35, primary_key=True, serialize=False)),
                ('hotel_name', models.CharField(max_length=20)),
                ('room_capacity', models.IntegerField()),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travello.Packages')),
            ],
        ),
        migrations.CreateModel(
            name='PackagesGuide',
            fields=[
                ('guide_id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('guide_name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('experience', models.IntegerField()),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travello.Packages')),
            ],
        ),
        migrations.CreateModel(
            name='PackagesBookings',
            fields=[
                ('booking_id', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('number_of_seats', models.IntegerField()),
                ('total_amount', models.IntegerField()),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travello.Packages')),
                ('username', models.ForeignKey(max_length=150, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DestinationDetails',
            fields=[
                ('place_id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('place_name', models.CharField(max_length=50)),
                ('visiting_on', models.IntegerField(default=0)),
                ('place_image', models.ImageField(upload_to='places')),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travello.Packages')),
            ],
        ),
    ]

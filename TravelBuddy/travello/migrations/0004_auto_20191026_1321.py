# Generated by Django 2.2.6 on 2019-10-26 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0003_packagesguide_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='destinationdetails',
            options={'verbose_name_plural': 'Destination details'},
        ),
        migrations.AlterModelOptions(
            name='packages',
            options={'verbose_name_plural': 'Packages'},
        ),
        migrations.AlterModelOptions(
            name='packagesbookings',
            options={'verbose_name_plural': 'Booking details'},
        ),
        migrations.AlterModelOptions(
            name='packagesguide',
            options={'verbose_name_plural': 'Package guide'},
        ),
        migrations.AlterModelOptions(
            name='packageshotel',
            options={'verbose_name_plural': 'Package hotels'},
        ),
        migrations.AlterModelOptions(
            name='packagesvehicle',
            options={'verbose_name_plural': 'Package vehicles'},
        ),
    ]
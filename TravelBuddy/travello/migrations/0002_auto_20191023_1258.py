# Generated by Django 2.2.6 on 2019-10-23 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='packages',
            old_name='vacancies',
            new_name='total_number_seats',
        ),
    ]
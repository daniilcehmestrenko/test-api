# Generated by Django 4.1.4 on 2022-12-10 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0004_alter_carrier_flowering_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrier',
            name='flowering_date',
        ),
    ]
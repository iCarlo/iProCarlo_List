# Generated by Django 3.0.4 on 2020-03-26 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iprocarlo_app', '0003_auto_20200326_1517'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Filters',
            new_name='Filter',
        ),
    ]
# Generated by Django 3.0.4 on 2020-03-31 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iprocarlo_app', '0012_auto_20200331_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='history_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='history date'),
        ),
    ]

# Generated by Django 3.0.4 on 2020-03-31 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iprocarlo_app', '0015_customer_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default_photo.jpg', null=True, upload_to=''),
        ),
    ]

# Generated by Django 3.0.4 on 2020-03-26 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iprocarlo_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter_text', models.CharField(max_length=200)),
                ('searched', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iprocarlo_app.Search')),
            ],
        ),
    ]
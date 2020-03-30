# Generated by Django 3.0.4 on 2020-03-30 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iprocarlo_app', '0009_auto_20200330_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filter',
            name='searched',
        ),
        migrations.AddField(
            model_name='filter',
            name='filter_code',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='filter',
            name='filter_text',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='iprocarlo_app.Customer')),
                ('filter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='iprocarlo_app.Filter')),
                ('search', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='iprocarlo_app.Search')),
            ],
        ),
    ]
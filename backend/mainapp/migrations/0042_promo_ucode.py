# Generated by Django 5.0.6 on 2024-06-05 21:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0041_integration_integrationlink'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=250)),
                ('client_name', models.CharField(max_length=250)),
                ('start_date', models.CharField(max_length=250)),
                ('end_date', models.CharField(max_length=250)),
                ('promo_text', models.CharField(max_length=16)),
                ('sale', models.IntegerField()),
                ('activate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('before_head', models.CharField(max_length=2000)),
                ('before_body', models.CharField(max_length=2000)),
                ('widget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.widget')),
            ],
        ),
    ]
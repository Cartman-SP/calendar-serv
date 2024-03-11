# Generated by Django 5.0.2 on 2024-03-08 13:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0024_remove_project_employee_employee_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('design', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('plashka', models.CharField(max_length=100)),
                ('back', models.CharField(max_length=100)),
                ('main', models.CharField(max_length=100)),
                ('theme', models.BooleanField(default=False)),
                ('ogranichenie', models.CharField(max_length=100)),
                ('interval', models.CharField(max_length=100)),
                ('cancellation', models.BooleanField(default=False)),
                ('employee', models.BooleanField(default=False)),
                ('company', models.BooleanField(default=False)),
                ('feedback', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='WidgetImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='widget_images')),
                ('widget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='mainapp.widget')),
            ],
        ),
    ]
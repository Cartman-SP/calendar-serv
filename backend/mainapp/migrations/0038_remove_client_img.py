# Generated by Django 5.0.1 on 2024-06-04 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0037_client_application'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='img',
        ),
    ]

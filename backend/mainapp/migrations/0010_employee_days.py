# Generated by Django 5.0.1 on 2024-02-19 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_employee_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='days',
            field=models.CharField(default='Пн,Вс', max_length=100),
            preserve_default=False,
        ),
    ]
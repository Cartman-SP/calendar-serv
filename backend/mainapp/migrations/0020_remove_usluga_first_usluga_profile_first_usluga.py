# Generated by Django 5.0.2 on 2024-03-03 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_remove_profile_first_usluga_usluga_first_usluga'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usluga',
            name='first_usluga',
        ),
        migrations.AddField(
            model_name='profile',
            name='first_usluga',
            field=models.BooleanField(default=False),
        ),
    ]

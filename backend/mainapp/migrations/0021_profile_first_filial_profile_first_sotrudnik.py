# Generated by Django 5.0.2 on 2024-03-04 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0020_remove_usluga_first_usluga_profile_first_usluga'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_filial',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_sotrudnik',
            field=models.BooleanField(default=False),
        ),
    ]

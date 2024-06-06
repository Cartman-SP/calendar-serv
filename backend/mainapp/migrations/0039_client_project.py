# Generated by Django 5.0.1 on 2024-06-04 18:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0038_remove_client_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.project'),
            preserve_default=False,
        ),
    ]
# Generated by Django 5.0.2 on 2024-03-28 21:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0029_remove_widget_link_widget_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='widget',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.project'),
            preserve_default=False,
        ),
    ]
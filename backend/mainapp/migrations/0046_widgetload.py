# Generated by Django 5.0.6 on 2024-07-06 13:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0045_widget_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='WidgetLoad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('load_time', models.DateTimeField(auto_now_add=True)),
                ('widget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.widget')),
            ],
        ),
    ]

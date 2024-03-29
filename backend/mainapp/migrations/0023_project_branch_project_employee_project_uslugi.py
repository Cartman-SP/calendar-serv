# Generated by Django 5.0.2 on 2024-03-04 19:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0022_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.branch')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.project')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.employee')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.project')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Uslugi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.project')),
                ('usluga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.usluga')),
            ],
        ),
    ]

# Generated by Django 5.0.2 on 2024-03-03 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_branch_phone_branch_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='password_changed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='serviceid',
            field=models.CharField(max_length=256),
        ),
    ]

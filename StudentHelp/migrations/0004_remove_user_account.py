# Generated by Django 5.0.2 on 2024-05-06 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudentHelp', '0003_user_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='account',
        ),
    ]

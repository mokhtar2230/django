# Generated by Django 5.0.2 on 2024-05-07 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentHelp', '0011_comment_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='li',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
# Generated by Django 5.0.2 on 2024-05-06 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudentHelp', '0006_alter_reaction_comment_alter_reaction_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reaction',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='reaction',
            name='like',
        ),
    ]
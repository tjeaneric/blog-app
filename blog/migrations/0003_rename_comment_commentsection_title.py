# Generated by Django 3.2 on 2021-04-23 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_commentsection'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentsection',
            old_name='comment',
            new_name='title',
        ),
    ]

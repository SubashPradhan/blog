# Generated by Django 2.2.6 on 2019-10-11 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='text',
            new_name='comment',
        ),
    ]

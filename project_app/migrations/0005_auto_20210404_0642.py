# Generated by Django 3.1.6 on 2021-04-03 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0004_history_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history_list',
            old_name='date',
            new_name='check_date',
        ),
    ]
# Generated by Django 3.1.6 on 2021-04-09 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0010_group_store'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group_store',
            old_name='shelf_id',
            new_name='shop_id',
        ),
    ]
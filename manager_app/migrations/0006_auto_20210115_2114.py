# Generated by Django 3.1.5 on 2021-01-15 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager_app', '0005_auto_20210115_1734'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='status_Choice',
            new_name='status',
        ),
    ]
# Generated by Django 3.1.5 on 2021-01-15 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager_app', '0007_auto_20210115_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='status_Choice',
        ),
    ]

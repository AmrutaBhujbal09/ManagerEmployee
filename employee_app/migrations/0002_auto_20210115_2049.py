# Generated by Django 3.1.5 on 2021-01-15 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='first_name',
            field=models.CharField(default='kiran', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='password',
            field=models.CharField(default='kiran', max_length=50),
        ),
    ]

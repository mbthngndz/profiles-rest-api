# Generated by Django 3.1.3 on 2020-12-01 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0002_test_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='userProfile',
        ),
    ]
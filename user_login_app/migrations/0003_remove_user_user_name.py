# Generated by Django 2.2.4 on 2021-03-24 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_login_app', '0002_user_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_name',
        ),
    ]
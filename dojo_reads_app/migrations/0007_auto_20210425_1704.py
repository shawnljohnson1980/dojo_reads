# Generated by Django 2.2.4 on 2021-04-25 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_reads_app', '0006_rating_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_rating', to='user_login_app.User'),
        ),
    ]

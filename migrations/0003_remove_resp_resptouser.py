# Generated by Django 4.0.1 on 2022-08-27 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_resp_resptouser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resp',
            name='respToUser',
        ),
    ]
# Generated by Django 4.0.1 on 2022-08-27 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('blog', '0004_resp_resptouser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resp',
            name='respToUser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='userResps', to='user.profile'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-29 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zombie_app', '0003_zombieattack'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zombieattack',
            name='attacks',
        ),
        migrations.RemoveField(
            model_name='zombieattack',
            name='zombies',
        ),
        migrations.AddField(
            model_name='zombieattack',
            name='zombie',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='zombie_app.zombie'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-29 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zombie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zombie',
            name='antidote',
            field=models.CharField(default=None, max_length=255),
        ),
    ]

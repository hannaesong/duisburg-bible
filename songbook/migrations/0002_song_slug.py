# Generated by Django 4.2.2 on 2023-11-29 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songbook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]

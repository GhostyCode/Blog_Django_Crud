# Generated by Django 4.2.2 on 2023-06-25 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='fix-me'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.7 on 2022-11-16 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_auto_20221114_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='slug',
            field=models.SlugField(default='-'),
        ),
    ]
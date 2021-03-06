# Generated by Django 3.2 on 2021-04-10 05:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210410_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator()], verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='user',
            name='pick_up_point',
            field=models.CharField(max_length=100, verbose_name='pick_up_point'),
        ),
    ]

# Generated by Django 3.2 on 2021-04-10 19:37

from django.db import migrations, models
import users.validations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210410_0147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pick_up_point',
        ),
        migrations.AddField(
            model_name='user_appointment',
            name='pick_up',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=256, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=15, validators=[users.validations.validate_password], verbose_name='password'),
        ),
    ]

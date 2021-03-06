# Generated by Django 3.2 on 2021-04-09 19:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('walkers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dog_type', models.CharField(default='Pick the breed of your dog', max_length=15)),
                ('dog_size', models.CharField(choices=[('SM', 'small'), ('MD', 'medium'), ('LG', 'large')], default=('SM', 'small'), max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()])),
                ('password', models.CharField(max_length=50)),
                ('pick_up_point', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User_Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment', models.DateTimeField(default=django.utils.timezone.now)),
                ('slots', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5, 'I can only take 5 dogs at a time')])),
                ('walker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='walkers.walker')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5, 'MAX RATING IS 5')])),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.dog')),
            ],
        ),
        migrations.AddField(
            model_name='dog',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]

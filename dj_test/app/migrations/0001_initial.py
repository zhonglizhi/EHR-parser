# Generated by Django 2.0.2 on 2018-04-08 12:13

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('career', django_mysql.models.JSONField(default=dict, null=True)),
                ('training', django_mysql.models.JSONField(default=dict, null=True)),
                ('cv_ref', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('working_schedule', models.CharField(max_length=20, null=True)),
                ('salary', models.CharField(max_length=20, null=True)),
                ('niv_etude', models.CharField(max_length=10, null=True)),
                ('experience', models.IntegerField(default=0)),
                ('requirements', django_mysql.models.JSONField(default=dict, null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('location', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('summary', models.TextField(null=True)),
            ],
        ),
    ]

# Generated by Django 3.0.6 on 2020-05-17 23:10

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=80)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation timestamp')),
                ('user_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Figure',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=80)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('params', django.contrib.postgres.fields.jsonb.JSONField()),
                ('modify_at', models.DateTimeField(auto_now_add=True, verbose_name='creation timestamp')),
                ('dashboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Dashboard')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='blog',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]

# Generated by Django 3.0.6 on 2020-05-18 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20200518_1740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dashboard',
            old_name='title',
            new_name='name',
        ),
    ]

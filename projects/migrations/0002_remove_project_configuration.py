# Generated by Django 3.2.8 on 2021-10-09 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='configuration',
        ),
    ]

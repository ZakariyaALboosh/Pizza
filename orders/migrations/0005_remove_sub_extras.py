# Generated by Django 2.2.6 on 2019-10-30 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20191030_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sub',
            name='extras',
        ),
    ]
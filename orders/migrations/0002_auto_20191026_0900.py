# Generated by Django 2.0.3 on 2019-10-26 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dinnerplatters',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='pasta',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='salads',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='subs',
            name='price',
            field=models.FloatField(),
        ),
    ]
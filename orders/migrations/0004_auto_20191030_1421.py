# Generated by Django 2.2.6 on 2019-10-30 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20191030_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='topping',
            field=models.IntegerField(choices=[(0, 'No toppings'), (1, 'One topping'), (2, 'Two toppings'), (3, 'Three toppings')]),
        ),
    ]

# Generated by Django 2.2.6 on 2019-10-30 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='topping',
            field=models.IntegerField(choices=[('0', 'No toppings'), ('1', 'One topping'), ('2', 'Two toppings'), ('3', 'Three toppings')], default=0),
        ),
    ]

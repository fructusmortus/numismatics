# Generated by Django 3.1.7 on 2021-05-30 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0004_remove_currency_collection'),
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='currencies',
            field=models.ManyToManyField(to='currency.Currency'),
        ),
    ]
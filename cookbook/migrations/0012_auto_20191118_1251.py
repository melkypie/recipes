# Generated by Django 2.2.7 on 2019-11-18 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0011_recipe_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='time',
            field=models.IntegerField(default=0),
        ),
    ]

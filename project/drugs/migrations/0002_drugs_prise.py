# Generated by Django 3.2.13 on 2022-04-25 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drugs',
            name='prise',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.2.13 on 2022-05-31 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drugs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='subcategories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='drugs.category', verbose_name='подкатегории'),
        ),
    ]

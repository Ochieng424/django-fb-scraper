# Generated by Django 3.2.7 on 2021-09-16 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0004_auto_20210916_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

# Generated by Django 2.2.6 on 2019-11-09 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pp', '0008_auto_20191108_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='tif',
            field=models.CharField(help_text='relative file path to root directory containing all images', max_length=2000),
        ),
    ]

# Generated by Django 2.2.7 on 2019-11-11 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pp', '0009_auto_20191109_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='estc',
            field=models.CharField(blank=True, db_index=True, editable=False, help_text='English Short Title Catalogue Number', max_length=50),
        ),
        migrations.AddField(
            model_name='book',
            name='tcp',
            field=models.CharField(blank=True, db_index=True, editable=False, help_text='TCP ID', max_length=50),
        ),
    ]

# Generated by Django 2.2.6 on 2019-10-05 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='characterclass',
            options={'ordering': ['classname']},
        ),
    ]

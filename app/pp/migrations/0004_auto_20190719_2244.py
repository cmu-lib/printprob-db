# Generated by Django 2.2.3 on 2019-07-20 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pp', '0003_auto_20190719_1750'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='spread',
            options={'ordering': ('book', 'sequence')},
        ),
    ]

# Generated by Django 2.2.6 on 2019-11-08 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pp', '0006_auto_20191108_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='x_max',
        ),
        migrations.RemoveField(
            model_name='page',
            name='x_min',
        ),
        migrations.AddField(
            model_name='page',
            name='h',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='rot1',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='rot2',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='w',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='x',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='y',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]

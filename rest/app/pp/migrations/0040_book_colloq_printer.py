# Generated by Django 3.1.3 on 2020-12-16 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pp', '0039_auto_20201216_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='colloq_printer',
            field=models.CharField(blank=True, db_index=True, default='', help_text='Commonly-held printer identification', max_length=2000),
        ),
    ]

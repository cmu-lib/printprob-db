# Generated by Django 3.1.3 on 2020-12-16 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pp', '0038_book_repository'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pp_notes',
            field=models.TextField(blank=True, default='', help_text='Free notes by the P&P team'),
        ),
        migrations.AddField(
            model_name='book',
            name='pp_printer',
            field=models.CharField(blank=True, db_index=True, default='', help_text='Printer as asserted by P&P team', max_length=2000),
        ),
    ]

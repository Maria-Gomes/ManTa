# Generated by Django 3.2.5 on 2021-07-26 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_alter_entry_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='diary',
        ),
        migrations.DeleteModel(
            name='Diary',
        ),
    ]

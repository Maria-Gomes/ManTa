# Generated by Django 3.2.5 on 2021-08-12 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_auto_20210726_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

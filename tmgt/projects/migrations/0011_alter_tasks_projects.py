# Generated by Django 3.2.5 on 2021-07-23 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_alter_tasks_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='projects',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='projects.projects'),
        ),
    ]

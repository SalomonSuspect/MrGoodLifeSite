# Generated by Django 4.0.2 on 2022-04-22 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeprojects', '0008_remove_step_time_estimate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
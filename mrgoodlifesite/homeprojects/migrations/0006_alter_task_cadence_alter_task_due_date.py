# Generated by Django 4.0.2 on 2022-02-18 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeprojects', '0005_tool_name_alter_tool_task_step'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='cadence',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
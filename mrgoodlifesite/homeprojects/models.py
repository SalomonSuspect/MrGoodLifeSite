from django.db import models


class Task(models.Model):
    """
    Model to capture info about a task
    """
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, blank=True)
    priority = models.IntegerField(default=0)
    due_date = models.DateTimeField(blank=True)
    cadence = models.DurationField(blank=True)
    # tool foreign key to Tool
    # journal foreign key to JournalEntry


class Tool(models.Model):
    task = models.ForeignKey('Task', related_name="tool", on_delete=models.CASCADE)


class JournalEntry(models.Model):
    entry = models.TextField(blank=True)
    creation_date = models.DateTimeField()
    task = models.ForeignKey('Task', related_name="journal", on_delete=models.CASCADE)


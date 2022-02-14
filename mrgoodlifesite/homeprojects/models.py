from django.db import models


class Task(models.Model):
    """
    Model to capture info about a task
    """
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, blank=True)
    priority = models.IntegerField(default=0)
    due_date = models.DateTimeField(blank=True, null=True)
    cadence = models.DurationField(blank=True, null=True)
    active = models.BooleanField(default=True)
    # steps foriegn key to Step
    # tool foreign key to Tool
    # journal foreign key to JournalEntry

    def __str__(self):
        return f"{self.name} - priority: {self.priority}"


class Tool(models.Model):
    task = models.ForeignKey('Task', related_name="tools", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Step(models.Model):
    task = models.ForeignKey('Task', related_name='steps', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name}'


class JournalEntry(models.Model):
    entry = models.TextField(blank=True)
    creation_date = models.DateTimeField()
    task = models.ForeignKey('Task', related_name="journal", on_delete=models.CASCADE)

    def __str__(self):
        return f"JournalEntry - {self.creation_date}"

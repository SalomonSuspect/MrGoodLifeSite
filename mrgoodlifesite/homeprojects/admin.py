from django.contrib import admin
from .models import Task, Tool, Step


class StepInLine(admin.TabularInline):
    model = Step
    extra = 3

class ToolInLine(admin.TabularInline):
    model = Tool
    extra = 3


class TaskAdmin(admin.ModelAdmin):
    inlines = [ToolInLine, StepInLine]
    list_display = ['name', 'priority', 'due_date']

admin.site.register(Task, TaskAdmin)

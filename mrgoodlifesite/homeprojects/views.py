from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.template import loader
from django.views import generic


def index(request):
    """
    Using function instead of generic ListView so we can have multiple lists (priority and due date)
    """
    prority_tasks = Task.objects.order_by("priority")
    due_date_tasks = Task.objects.order_by('due_date')
    template = loader.get_template('homeprojects/index.html')
    context = {
        'prioritized_list': prority_tasks,
        'due_date_list': due_date_tasks
    }
    return HttpResponse(template.render(context, request))

class DetailView(generic.DetailView):
    """
    View to display the details of a TAsk
    """
    template_name = 'homeprojects/details.html'
    model = Task

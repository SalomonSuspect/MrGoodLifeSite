from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.template import loader


def index(request):
    tasks = Task.objects.order_by("priority")
    template = loader.get_template('homeprojects/index.html')
    context = {
        'prioritized_list': tasks
    }
    return HttpResponse(template.render(context, request))


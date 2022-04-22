from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.template import loader
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'homeprojects/index.html'
    context_object_name = "prioritized_list"

    def get_queryset(self):
        return Task.objects.order_by("priority")




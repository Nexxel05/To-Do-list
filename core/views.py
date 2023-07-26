from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from core.models import Task


def index(request):
    tasks = Task.objects.all()

    context = {
        "tasks": tasks
    }
    return render(request, "core/index.html", context)


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("core:index")
from django.shortcuts import render

from core.models import Task


def index(request):
    tasks = Task.objects.all()

    context = {
        "tasks": tasks
    }
    return render(request, "core/index.html", context)
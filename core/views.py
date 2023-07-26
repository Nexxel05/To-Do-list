from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from core.forms import TaskForm
from core.models import Task


def index(request):
    tasks = Task.objects.all()

    context = {
        "tasks": tasks
    }
    return render(request, "core/index.html", context)


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("core:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("core:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("core:index")


def task_change_status(request, pk):
    task = get_object_or_404(Task, id=pk)

    task.is_completed = not task.is_completed
    task.save()

    return HttpResponseRedirect(reverse_lazy("core:index"))

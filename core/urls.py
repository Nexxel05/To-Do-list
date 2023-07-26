from django.urls import path

from core.views import index, TaskCreateView

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("task_create", TaskCreateView.as_view(), name="create-task")
]
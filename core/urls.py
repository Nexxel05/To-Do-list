from django.urls import path

from core.views import index, TaskCreateView, TaskUpdateView, TaskDeleteView, task_change_status

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("create_task", TaskCreateView.as_view(), name="create-task"),
    path("<int:pk>/update", TaskUpdateView.as_view(), name="update-task"),
    path("<int:pk>/delete", TaskDeleteView.as_view(), name="delete-task"),
    path("<int:pk>/change_status", task_change_status, name="change-status-task"),
]
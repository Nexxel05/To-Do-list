from django.urls import path

from core.views import index, TaskCreateView, TaskUpdateView

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("create_task", TaskCreateView.as_view(), name="create-task"),
    path("<int:pk>/update", TaskUpdateView.as_view(), name="update-task")
]
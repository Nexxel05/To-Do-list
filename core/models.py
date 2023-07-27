from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=63)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    deadline = models.DateField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["is_completed", "deadline"]

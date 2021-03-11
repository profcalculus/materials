from datetime import datetime, timedelta

from django.db import models


def one_week_hence():
    return datetime.now() + timedelta(days=7)


class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(default=datetime.now)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        """ Returns the URL to access a specific item."""
        return reverse('item_detail', args=[str(self.id)])

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

from django.db import models
from django.utils import timezone

class ToDoList(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now()
    )
    def __str__(self):
        return self.title
# Create your models here.

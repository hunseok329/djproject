from django.db import models
from django.utils import timezone
from django.urls import reverse

class ToDoList(models.Model):
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(
        default=timezone.now()
    )
    def __str__(self):
        return self.title
# Create your models here.

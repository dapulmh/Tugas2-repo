from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskTodolist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    is_finished = models.BooleanField(default = False)

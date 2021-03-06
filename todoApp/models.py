from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL, null=True, blank=True)
    task = models.CharField(max_length=200)
    complete =models.BooleanField(default=False)


    def __str__(self):
        return self.task
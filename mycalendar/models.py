from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Exam(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    examdate = models.DateTimeField(blank=True)
    hard = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - by: ' + self.user.username

from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created = models.DateTimeField(default=timezone.now)
    body = models.TextField()

    def __str__(self):
        return str(self.first_name)+" : "+str(self.body)
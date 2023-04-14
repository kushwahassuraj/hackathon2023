from django.db import models

# Create your models here.
from django.db import models
class feed_fun(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    message=models.TextField()

# Create your models here.
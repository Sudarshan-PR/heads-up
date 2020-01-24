from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserInputs(models.Model):
    email_id = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()
    limit = models.IntegerField()
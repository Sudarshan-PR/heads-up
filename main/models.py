from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserInputs(models.Model):
    email_id = models.EmailField()
    url = models.URLField()
    limit = models.IntegerField()

class Check(models.Model):
    url = models.URLField(unique=True)
    prices = models.IntegerField()

# class Orders(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     urls = models.ForeignKey(Check, on_delete=models.CASCADE)


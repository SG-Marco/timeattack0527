# user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings



# Create your models here.
class UserModel(models.Model):
    class Meta:
        db_table = "my_user"
    
    email = models.CharField(max_length=256, default='')
    password = models.CharField(max_length=256, null=False)





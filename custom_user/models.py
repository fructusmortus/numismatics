from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
	is_director = models.BooleanField(default=False)
	is_manager = models.BooleanField(default=False)
	is_storekeeper = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)
	
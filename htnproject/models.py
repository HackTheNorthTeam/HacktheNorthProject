from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    course = models.ForeignKey(
        'Course',
        on_delete=models.CASCADE, 
        null = True
    )

class School(models.Model):
    name = models.TextField(max_length=500, blank=True)
    school_id = models.IntegerField()

class Course(models.Model):
    code = models.CharField(max_length=6, blank=True)
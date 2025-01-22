from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    summary = models.TextField(max_length=2000)
    degree = models.CharField(max_length=150)
    college = models.CharField(max_length=150)
    university = models.CharField(max_length=150)
    experience = models.TextField(max_length=1000)
    skills = models.TextField(max_length=1000)

    def __str__(self):
        return self.name 



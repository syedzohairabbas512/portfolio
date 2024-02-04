from django.db import models
from datetime import datetime


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    deploy_url = models.URLField(blank=False, null=False)
    github_url = models.URLField(blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    image = models.ImageField(upload_to='media/', blank=False, null=False)

    def __str__(self):
        return self.title

from django.db import models
from django.core.validators import EmailValidator


# Create your models here.


class Contact(models.Model):
    name = models.CharField(("Name"), max_length=120)
    email = models.EmailField(verbose_name="Email", max_length=255)
    phone = models.CharField(("Phone"), max_length=50)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

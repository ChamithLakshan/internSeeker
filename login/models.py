from django.db import models

# Create your models here.

class Intern(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

class Company(models.Model):
    companyname = models.CharField(max_length=100)
    ceoname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
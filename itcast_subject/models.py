from django.db import models


# Create your models here.
class nami_user(models.Model):
    uid = models.CharField(primary_key=True, max_length=32)
    ase_password = models.CharField(max_length=40)
    admin = models.BooleanField()
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    username = models.CharField(max_length=255)

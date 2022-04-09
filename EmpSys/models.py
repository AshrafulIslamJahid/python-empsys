from django.db import models

class Newuser(models.Model):
    Username=models.CharField(max_length=150)
    Email=models.CharField(max_length=150)
    Pwd=models.CharField(max_length=150)

class Newemployee(models.Model):
    Name=models.CharField(max_length=150)
    Phone=models.CharField(max_length=150)
    Address=models.CharField(max_length=150)
from django.db import models

# Create your models here.
class Patient(models.Model):
    id=models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    bg = models.CharField(max_length=100 , default='O+')
    gender = models.CharField(max_length=100 , default='Male')
    age = models.IntegerField(default=0)


    


    def __str__(self):
        return self.name

class Doctor(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    speacial = models.CharField(max_length=100)


    def __str__(self):
        return self.name
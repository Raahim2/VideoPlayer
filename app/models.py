from django.db import models

# Create your models here.
class Patients(models.Model):
    id=models.AutoField
    name = models.TextField
    username = models.TextField
    password = models.TextField

class Doctors(models.Model):
    id=models.AutoField
    name = models.TextField
    username = models.TextField
    password = models.TextField
    speacial = models.TextField


    def __str__(self):
        return self.name
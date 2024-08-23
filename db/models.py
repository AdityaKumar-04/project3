from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=55)
    age=models.IntegerField()
    city=models.CharField(max_length=55)
    image=models.ImageField(upload_to='',null=True)

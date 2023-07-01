from django.db import models

# Create your models here.


class Student(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    email=models.CharField(max_length=100,blank=False,null=False)
    phone=models.CharField(max_length=100,blank=False,null=False)
    created_at=models.DateTimeField(auto_now=True)





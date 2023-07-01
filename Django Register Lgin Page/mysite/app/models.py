from django.db import models

# Create your models here.


class Register(models.Model):
    username=models.CharField(max_length=100,blank=False,null=False,default="")
    email=models.EmailField(max_length=100,blank=False,null=False)
    password=models.CharField(max_length=50,blank=False,null=False)
    cpassword=models.CharField(max_length=50,blank=False,null=False)
    created_at=models.DateTimeField(auto_now_add=True)
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Images(models.Model):
    username=models.CharField(max_length=64,null=True, blank=True)
    image=models.ImageField(null=True, blank=True, upload_to='MRI')
    result=models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return (f"{self.username} {self.image} {self.result}")
    
class Chatbot(models.Model):
    username=models.CharField(max_length=64,null=True, blank=True)
    text=models.CharField(max_length=200, null=True, blank=True)
    response=models.CharField(max_length=200, null=True, blank=True)
    time=models.DateTimeField()

    def __str__(self):
        return (f"{self.username} {self.text} {self.response} {self.time}")

class XRayImages(models.Model):
    username=models.CharField( max_length=100,null=True, blank=True)
    image=models.ImageField(null=True, blank=True, upload_to='XRay')
    result=models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return (f" {self.username} {self.image} {self.result}")
    
class chest_ct(models.Model):
    username=models.CharField( max_length=100,null=True, blank=True)
    image=models.ImageField(null=True, blank=True, upload_to='CTScan')
    result=models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return (f"{self.username} {self.image} {self.result}")
    
class Diabetes(models.Model):
    username=models.CharField( max_length=100)
    OGTT=models.CharField(max_length=100)
    Blood_Pressure=models.CharField( max_length=100)
    Skin_Thickness=models.CharField( max_length=100)
    Insulin=models.CharField( max_length=100)
    BMI=models.CharField(max_length=100)
    Age=models.CharField(max_length=100)
    DiabetesPedigreeFunction=models.CharField(max_length=100)

    def __str__(self):
        return (f"{self.username} {self.OGTT} {self.Blood_Pressure} {self.Skin_Thickness} {self.Insulin} {self.BMI} {self.Age} {self.DiabetesPedigreeFunction}")
    
class contact_us(models.Model):
    username=models.CharField( max_length=100)
    phone=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.CharField(max_length=100)

    def __str__(self):
        return (f"{self.username}  {self.phone} {self.email} {self.message}")    
    
class info(models.Model):
    username=models.CharField( max_length=100)
    email=models.EmailField()
    first_name=models.CharField( max_length=100)
    last_name=models.CharField( max_length=100)
    mobile=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return (f"{self.username} {self.password} {self.first_name} {self.last_name} {self.email} {self.mobile}")
    
class user_info(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField()
    first_name=models.CharField( max_length=100)
    last_name=models.CharField( max_length=100)
    mobile=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    # user=models.OneToOneField(User,on_delete=models.CASCADE,default=id)
    # last_login=models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return (f"{self.username} {self.password} {self.email} {self.first_name} {self.last_name}  {self.mobile}")

from django.db import models
from django.contrib.auth import get_user_model



class Contact(models.Model):
    user=models.ForeignKey(get_user_model(),models.CASCADE,null=True)
    name=models.CharField(max_length=32,null=True)
    email=models.EmailField(max_length=254,null=True)
    mobile=models.IntegerField(null=True)
    address=models.TextField(null=True)
    image=models.CharField(max_length=255,null=True)
    

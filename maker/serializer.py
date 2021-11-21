from django.db.models import fields
from rest_framework import serializers
from .models import Contact

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields=('user','name','email','mobile','address','image')
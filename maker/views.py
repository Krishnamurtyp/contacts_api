from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Contact
from .serializer import PostSerializer

class ContactsList(ListCreateAPIView):
    queryset=Contact.objects.all()
    serializer_class=PostSerializer

class ContactsDetail(RetrieveUpdateDestroyAPIView):
    queryset=Contact.objects.all()
    serializer_class=PostSerializer
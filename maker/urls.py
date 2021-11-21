from django.urls import path
from .views import ContactsList,ContactsDetail


urlpatterns = [
    path('',ContactsList.as_view(),name="contacts_list"),
    path('<int:pk>/',ContactsDetail.as_view(),name="contacts_details"),
]

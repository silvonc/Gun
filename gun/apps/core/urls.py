from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-company/', views.add_company, name='add_company'),
    path('add-contact/', views.add_contact, name='add_contact'),
]
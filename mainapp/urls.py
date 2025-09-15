from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('listpage', views.listpage, name='list'),
    path('addlocation', views.addplace, name='addlocation')
]
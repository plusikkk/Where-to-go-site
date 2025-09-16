from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('listpage', views.listpage, name='list'),
    path('addlocation', views.addplace, name='addlocation'),
    path('place/<int:place_id>/', views.place_detail, name='place_detail'),
    path('random', views.random_place, name='random_place')
]
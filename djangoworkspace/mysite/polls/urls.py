from django.urls import path
from . import views, maple
urlpatterns = [
    path('', views.index, name='index'),
    path('maple', maple.index, name='maple')
]
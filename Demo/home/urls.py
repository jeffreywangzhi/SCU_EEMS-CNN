from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.home),
    path('getdata/', views.base)
]
from django.urls import include
from django.views import defaults
from django.urls import path,re_path
from . import views
urlpatterns = [
    re_path(r'test_api/$', views.test_api),
]
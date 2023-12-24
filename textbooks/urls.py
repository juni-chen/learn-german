from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index_template, name='index'),
]
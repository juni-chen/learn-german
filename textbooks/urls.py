from . import views
from django.urls import path, include

app_name = 'textbooks'

urlpatterns = [
    path('', views.index_template, name='index'),
]
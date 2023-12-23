from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.quiz_index_template, name='index'),
]
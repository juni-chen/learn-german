from . import views
from django.urls import path, include

app_name = 'wordquiz'

urlpatterns = [
    path('', views.quiz_index_template, name='index'),
]
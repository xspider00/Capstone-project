#define URL route for index() view
from django.urls import path
from . import views

urlpatterns = [
    path('restaurant/', views.index, name='index'),
]
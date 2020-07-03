from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category', views.category, name='category'),
    path('category', views.category, name='single')
]

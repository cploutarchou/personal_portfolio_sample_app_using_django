from django.urls import path
from cms import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category', views.category, name='category'),
    path('single', views.single, name='single'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact')
]

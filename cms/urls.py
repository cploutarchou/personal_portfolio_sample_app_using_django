from django.conf.urls import url
from django.urls import path
from cms import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
]

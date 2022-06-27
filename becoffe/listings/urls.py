from django import views
from django.urls import re_path as url
from listings import views




urlpatterns=[
    url(r'^users$', views.users),
    url(r'^users/([0-9]+)$', views.users)
]
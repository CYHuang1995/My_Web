from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    #path('index/', views.index),
    #path(r'^article/(?P<article_id>[0-9]+)$', views.article_page),
    url(r'^index/$', views.index),
]


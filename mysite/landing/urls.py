from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^home',views.home,name='home'),
    url(r'^landing',views.landing,name='landing'),
]

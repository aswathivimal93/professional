from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from company import views

urlpatterns = [
    path('',views.home,name='index'),
]
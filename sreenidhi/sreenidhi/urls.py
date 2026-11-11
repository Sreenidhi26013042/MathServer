    

from django.contrib import admin
from django.urls import path
from sreeapp import views

urlpatterns = [path('', views.churn_bill, name='churn_bill'),]


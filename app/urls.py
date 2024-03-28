from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index ),
    path('login' , views.login),
    path('signup' , views.signup),
    path('dashboard' , views.dashboard),
    path('report' , views.report),
    path('appoint' , views.appoint),


]
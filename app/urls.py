from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index ),
    path('login' , views.login),
    path('signup' , views.signup)
    # path('device/<str:cpy>',views.devices),
    # path('device/info/<int:my_id>',views.info),
    # path('device/info/predict' , views.predict)
]